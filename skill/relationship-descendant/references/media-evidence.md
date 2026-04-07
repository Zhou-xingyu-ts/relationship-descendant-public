# Media Evidence

Use this file after raw media has been normalized into notes, transcripts, or extracted artifacts.

## Evidence Card

Convert each media source into a compact evidence card:

```text
media_evidence:
  source_label:
  modality:
  direct_artifacts:
  extracted_artifacts:
  confidence_level:
  usable_for:
  not_usable_for:
  notes:
```

## Modality Strengths

### image

Usable for:

- aesthetic style
- visible energy
- scene context
- presentation cues

Not usable for:

- inner motives
- stable mental traits
- diagnosis

### audio

Usable for:

- pacing
- warmth
- intensity
- patience

Not usable for:

- hidden truth
- exact emotional state
- diagnosis

### video

Usable for:

- transcript-backed interaction rhythm
- scene-level chemistry
- visible energy and environment

Not usable for:

- strong certainty from gestures alone
- deep relationship truths from a short clip

## Conversion Rule

When a media source is weak or partial:

- lower confidence
- keep the note short
- do not let one weak source dominate the synthesis

## Best Practice

Summarize media findings into the same parent cards used for chats and manual notes.

Media should enrich the portrait, not overrule stronger textual evidence.
