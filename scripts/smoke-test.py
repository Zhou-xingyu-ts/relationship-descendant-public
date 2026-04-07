#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path


def which_with_fallback(command: str, *fallbacks: str) -> str | None:
    found = shutil.which(command)
    if found:
        return found
    for fallback in fallbacks:
        path = Path(fallback).expanduser()
        if path.exists():
            return str(path)
    return None


def require(path: Path, failures: list[str]) -> None:
    if path.exists():
        print(f"[ok] {path}")
    else:
        print(f"[missing] {path}")
        failures.append(str(path))


def run_media_check(skill_dir: Path, failures: list[str], strict: bool) -> None:
    ffmpeg = which_with_fallback("ffmpeg")
    whisper = which_with_fallback("whisper", "~/.local/bin/whisper")
    if not ffmpeg or not whisper:
        message = "media check skipped: ffmpeg or whisper not found"
        if strict:
            failures.append(message)
            print(f"[fail] {message}")
        else:
            print(f"[warn] {message}")
        return

    extract_script = skill_dir / "scripts" / "extract-media-bundle.py"
    with tempfile.TemporaryDirectory() as tmp:
        tmp_path = Path(tmp)
        audio_path = tmp_path / "sample.wav"
        out_dir = tmp_path / "output"
        subprocess.run(
            [ffmpeg, "-y", "-f", "lavfi", "-i", "anullsrc=r=16000:cl=mono", "-t", "1", str(audio_path)],
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        subprocess.run(
            [sys.executable, str(extract_script), str(audio_path), "--output-dir", str(out_dir)],
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        manifest = out_dir / "media-evidence-bundle.json"
        transcript = out_dir / "transcripts" / "sample.txt"
        if not manifest.exists():
            failures.append("media-evidence-bundle.json was not created")
            print("[fail] media-evidence-bundle.json was not created")
            return
        data = json.loads(manifest.read_text(encoding="utf-8"))
        if not data["tools"].get("ffmpeg") or not data["tools"].get("whisper"):
            failures.append("media tools were not reported as available")
            print("[fail] media tools were not reported as available")
            return
        if not transcript.exists():
            failures.append("transcript file was not created")
            print("[fail] transcript file was not created")
            return
        print("[ok] media extraction pipeline")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--skill-dir", default=None)
    parser.add_argument("--check-media", action="store_true")
    parser.add_argument("--require-media", action="store_true")
    args = parser.parse_args()

    repo_root = Path(__file__).resolve().parent.parent
    skill_dir = Path(args.skill_dir).resolve() if args.skill_dir else repo_root / "skill" / "relationship-descendant"

    failures: list[str] = []
    require(skill_dir / "SKILL.md", failures)
    require(skill_dir / "agents" / "openai.yaml", failures)
    require(skill_dir / "scripts" / "extract-media-bundle.py", failures)
    require(skill_dir / "references" / "media-intake.md", failures)
    require(skill_dir / "references" / "media-evidence.md", failures)
    require(repo_root / "README.md", failures)
    require(repo_root / "INSTALL.md", failures)
    require(repo_root / "PRIVACY.md", failures)
    require(repo_root / "SECURITY.md", failures)
    require(repo_root / "LICENSE", failures)

    if args.check_media or args.require_media:
        run_media_check(skill_dir, failures, strict=args.require_media)

    if failures:
        print("\nSmoke test failed.")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print("\nSmoke test passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
