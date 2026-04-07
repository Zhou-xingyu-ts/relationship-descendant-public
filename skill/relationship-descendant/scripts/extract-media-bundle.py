#!/usr/bin/env python3
"""
Extract a lightweight evidence bundle from image, audio, and video files.

This script is intentionally conservative:
- it never claims semantic understanding of images on its own
- it only extracts transcripts when `whisper` is available
- it only extracts video audio/frames when `ffmpeg` is available
"""

from __future__ import annotations

import argparse
import json
import shutil
import subprocess
from os import PathLike
from pathlib import Path

IMAGE_EXTS = {".jpg", ".jpeg", ".png", ".webp", ".bmp"}
AUDIO_EXTS = {".mp3", ".wav", ".m4a", ".aac", ".ogg", ".flac"}
VIDEO_EXTS = {".mp4", ".mov", ".mkv", ".avi", ".webm"}


def which_with_fallback(command: str, *fallbacks: str | PathLike[str]) -> str | None:
    resolved = shutil.which(command)
    if resolved:
        return resolved

    for candidate in fallbacks:
        path = Path(candidate).expanduser()
        if path.exists():
            return str(path)
    return None


def detect_modality(path: Path) -> str:
    ext = path.suffix.lower()
    if ext in IMAGE_EXTS:
        return "image"
    if ext in AUDIO_EXTS:
        return "audio"
    if ext in VIDEO_EXTS:
        return "video"
    return "unknown"


def run(command: list[str]) -> tuple[bool, str]:
    try:
        subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return True, ""
    except subprocess.CalledProcessError as exc:
        return False, exc.stderr.decode("utf-8", errors="ignore")


def ensure_dir(path: Path) -> None:
    path.mkdir(parents=True, exist_ok=True)


def extract_video_artifacts(path: Path, out_dir: Path) -> dict:
    result = {"audio": None, "frames": [], "notes": []}
    ffmpeg = which_with_fallback("ffmpeg")
    if not ffmpeg:
        result["notes"].append("ffmpeg not found; video was not split into audio or frames.")
        return result

    audio_dir = out_dir / "audio"
    frame_dir = out_dir / "frames" / path.stem
    ensure_dir(audio_dir)
    ensure_dir(frame_dir)

    audio_path = audio_dir / f"{path.stem}.wav"
    ok, err = run(
        [
            ffmpeg,
            "-y",
            "-i",
            str(path),
            "-vn",
            "-ac",
            "1",
            "-ar",
            "16000",
            str(audio_path),
        ]
    )
    if ok:
        result["audio"] = str(audio_path)
    else:
        result["notes"].append(f"audio extraction failed: {err.strip()[:300]}")

    frame_pattern = frame_dir / f"{path.stem}_%02d.jpg"
    ok, err = run(
        [
            ffmpeg,
            "-y",
            "-i",
            str(path),
            "-vf",
            "fps=1/10",
            "-frames:v",
            "6",
            str(frame_pattern),
        ]
    )
    if ok:
        result["frames"] = [str(p) for p in sorted(frame_dir.glob("*.jpg"))]
    else:
        result["notes"].append(f"frame extraction failed: {err.strip()[:300]}")

    return result


def transcribe_audio(path: Path, out_dir: Path) -> dict:
    result = {"transcript": None, "notes": []}
    whisper = which_with_fallback("whisper", "~/.local/bin/whisper")
    if not whisper:
        result["notes"].append("whisper not found; audio transcription was skipped.")
        return result

    transcript_dir = out_dir / "transcripts"
    ensure_dir(transcript_dir)
    ok, err = run(
        [
            whisper,
            str(path),
            "--output_dir",
            str(transcript_dir),
            "--output_format",
            "txt",
            "--verbose",
            "False",
        ]
    )
    txt_path = transcript_dir / f"{path.stem}.txt"
    if ok and txt_path.exists():
        result["transcript"] = str(txt_path)
    else:
        result["notes"].append(f"transcription failed: {err.strip()[:300]}")
    return result


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("inputs", nargs="+", help="Media files to ingest")
    parser.add_argument("--output-dir", required=True, help="Where to write the bundle")
    args = parser.parse_args()

    out_dir = Path(args.output_dir).expanduser().resolve()
    ensure_dir(out_dir)

    bundle = {
        "tools": {
            "ffmpeg": bool(which_with_fallback("ffmpeg")),
            "whisper": bool(which_with_fallback("whisper", "~/.local/bin/whisper")),
        },
        "entries": [],
        "limitations": [],
    }

    for raw in args.inputs:
        path = Path(raw).expanduser().resolve()
        modality = detect_modality(path)
        entry = {
            "source": str(path),
            "modality": modality,
            "usable_artifacts": {},
            "notes": [],
        }

        if not path.exists():
            entry["notes"].append("file not found")
            bundle["entries"].append(entry)
            continue

        if modality == "image":
            entry["usable_artifacts"]["image"] = str(path)
            entry["notes"].append("semantic extraction for images still requires manual notes or a multimodal model.")
        elif modality == "audio":
            entry["usable_artifacts"]["audio"] = str(path)
            entry["usable_artifacts"]["transcription"] = transcribe_audio(path, out_dir)
        elif modality == "video":
            extracted = extract_video_artifacts(path, out_dir)
            entry["usable_artifacts"]["video"] = str(path)
            entry["usable_artifacts"]["extracted"] = extracted
            if extracted.get("audio"):
                entry["usable_artifacts"]["transcription"] = transcribe_audio(Path(extracted["audio"]), out_dir)
        else:
            entry["notes"].append("unsupported file type")

        bundle["entries"].append(entry)

    if not bundle["tools"]["ffmpeg"]:
        bundle["limitations"].append("Install ffmpeg for video audio/frame extraction.")
    if not bundle["tools"]["whisper"]:
        bundle["limitations"].append("Install whisper for local audio transcription.")

    manifest_path = out_dir / "media-evidence-bundle.json"
    manifest_path.write_text(json.dumps(bundle, ensure_ascii=False, indent=2), encoding="utf-8")
    print(str(manifest_path))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
