# Media Intake

Use this file when the user provides raw image, audio, or video files.

## Goal

Turn media files into a lightweight evidence bundle that can support persona synthesis.

## Priority Order

1. chat logs
2. call or voice transcripts
3. video-derived notes
4. image-derived notes
5. manual user interpretation

Chats and transcripts remain the strongest evidence.

## Image Intake

Best case:

- a multimodal model or image-analysis tool is available

Fallback:

- ask the user for 1 to 3 short descriptions
- ask why each image is representative

Extract only:

- style
- environment
- visible social energy
- aesthetic cues

Do not extract:

- deep personality claims
- moral character claims
- diagnostic claims

## Call Recording Intake

Best case:

- transcribe locally using whisper-like tooling

Fallback:

- ask the user for a transcript
- or ask for a short summary of speaking style

Extract:

- pacing
- warmth
- interruption style
- emotional intensity
- patience

## Video Intake

Best case:

- extract audio
- transcribe audio
- extract a few representative frames

Fallback:

- ask the user for a transcript and a short scene description

Extract:

- scene context
- visible interaction rhythm
- transcript-backed speaking style
- mood cues

Avoid:

- certainty from body language
- stable personality claims from a short clip

## Local Script Workflow

If process tools are available, use:

`scripts/extract-media-bundle.py`

What it can do:

- classify files by modality
- extract video audio if `ffmpeg` exists
- extract a small set of video frames if `ffmpeg` exists
- transcribe audio if `whisper` exists
- emit a manifest describing what was extracted and what is still missing

If required tools are missing, the script still emits a manifest and limitation notes.
