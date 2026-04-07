---
name: relationship-descendant
description: Create a fictional successor-persona studio from two people's relationship material such as chats, voice notes, call recordings, images, short videos, and user notes. Use when the user wants a descendant-style third persona, weighted variants, future snapshots, a live session voice, or reusable preset text derived from a relationship. When media files are provided, extract usable evidence first, then synthesize. Do not present the output as a real child prediction, diagnosis, or factual reconstruction.
---

Use this skill as a multi-mode studio for relationship-derived personas.

This skill is for:

- a creative "third persona" derived from two people
- a descendant-style role with inherited traits
- a family-style successor persona
- a relationship-derived character sheet
- a reusable session persona block
- multiple weighted variants from the same pair
- scene previews of how the persona would sound in action

This skill is not for:

- predicting a real future child
- diagnosing personality or mental health
- claiming factual truth from chats, images, or voice
- replacing a real person or creating emotional dependency

## Hard Boundary

Always frame the output as:

- fictional
- creative
- speculative
- inspired by observed interaction patterns

Never frame it as:

- what their real child will be like
- a scientifically valid inference
- a reconstruction of someone's true inner self

If the user pushes for certainty, say clearly that this is a creative persona synthesis, not a real prediction.

## Studio Modes

Choose one primary mode, then add optional follow-up modes.

- `portrait`
  - Build one strong successor persona card.
  - Use when the request is vague or first-time.
- `blend-lab`
  - Produce 2 to 4 weighted variants such as `A-heavy`, `balanced`, `B-heavy`, or `gentler`.
  - Use when the user wants options or says "more like A/B."
- `future-snapshot`
  - Write sample scenes or dialogue snippets showing the persona in action at the same age as the sources.
  - Use when the user wants immersion, sample conversations, or "what would they sound like."
- `session-voice`
  - Convert the persona into a compact live-voice instruction block suitable for ongoing chat.
  - Use only when the user explicitly wants a persistent persona.
- `preset-save`
  - Output reusable preset text plus a structured payload that can be stored or reapplied later.
  - Use when the user wants something portable.

Read `references/workflow-modes.md` when selecting or sequencing modes.

If the user is vague, start with `portrait`.

## Recommended Workflow

1. Identify source A and source B.
2. Identify the available modalities:
   - chat logs
   - voice or call transcripts
   - images with descriptions
   - short video clips
   - self and partner profile notes
   - manual notes from the user
3. Summarize what each modality can and cannot support.
4. Build two parent-style cards using sampled evidence only.
5. Synthesize one or more successor variants using inheritance plus creative variation.
6. If requested, expand into scenes, live voice, or preset text.
7. End with a clear boundary disclaimer.

## Input Handling

If the user gives raw material, first summarize:

- who the two people are
- what data types were provided
- what those data types are strong or weak at

If the user does not provide enough material, ask for one or more of:

- 20 to 100 lines of representative chat
- 1 to 3 short voice-note summaries or transcripts
- 1 to 5 images with brief descriptions
- a self-description for each person
- a partner-description written by the other person when possible
- a short note about each person's vibe

Prefer transcripts and descriptions over claiming confidence from raw audio or raw images alone.

If raw media files are provided, first normalize them into an evidence bundle:

- images -> image notes
- call recordings or voice notes -> transcripts plus speaking-style notes
- video clips -> extracted audio, sampled frames, and scene notes

Use `scripts/extract-media-bundle.py` when process tools are available.
If the current agent cannot run local process tools, delegate the extraction step to a tooling-capable agent such as `coder`, ask it to return the bundle path plus a short evidence summary, then continue synthesis from that evidence instead of the raw files.
Read `references/media-intake.md` and `references/media-evidence.md` for the modality workflow.

If the user gives weighting, mood, or safety steering such as:

- "65% like A"
- "keep the meme energy but make it gentler"
- "same age, not childlike"
- "usable as a live assistant voice"

honor it explicitly.

If the user can provide structured self/partner descriptions, collect them in four buckets:

- how I describe myself
- how I describe my partner
- how my partner describes themselves
- how my partner describes me

This usually improves synthesis quality because it adds explicit self-perception and cross-perception.
Read `references/profile-intake.md` when the user wants a stronger, more accurate intake.

## Modality Rules

### Chat logs

Use for:

- rhythm
- humor style
- emotional expression
- conflict style
- affection style
- common phrases
- meme density
- directness

### Voice or call transcripts

Use for:

- speech energy
- emotional intensity
- patience
- warmth
- hesitation or confidence patterns

Do not claim deep truth from tone alone.

If only an audio file is provided:

- transcribe first if local tooling exists
- otherwise ask for a transcript or summary

### Video clips

Use for:

- conversational pacing
- visible interaction energy
- body-language-level scene cues
- environmental context

Do not infer stable personality facts from gestures or appearance alone.

If a raw video file is provided:

1. extract audio
2. extract a few representative frames
3. build notes from transcript plus visible scene cues
4. keep every claim scoped to the clip sample

### Images

Use only for:

- aesthetic cues
- presentation style
- shared environment signals
- visible social energy

Do not claim stable personality facts from appearance.

If local vision analysis is unavailable, ask for:

- 1 to 3 short descriptions of what is visible
- why the image is representative
- any mood or style cues the user wants preserved

### Manual notes

Use as high-value steering input.

### Self and partner profile notes

Use for:

- self-perception
- cross-perception
- recurring compliments or complaints
- what each person thinks they contribute to the relationship
- what each person believes the other stabilizes or intensifies

These notes are especially useful for:

- reducing overreliance on a small chat sample
- clarifying hidden weighting
- improving the final session voice

## Extraction Dimensions

Use the schema in `references/extraction-dimensions.md`.

At minimum, estimate these dimensions for each parent source:

- warmth
- directness
- humor
- internetness
- emotional expressiveness
- patience
- playfulness
- conflict style
- language texture
- social energy

## Inheritance Rules

Use the rules in `references/inheritance-rules.md`.

Short version:

- reinforce shared traits
- blend compatible traits by weight
- soften risky traits such as aggression or emotional volatility
- allow one or two novel traits to emerge as creative variation
- do not simply average everything

## Scenes And Presets

Read these references only when needed:

- `references/scene-generation.md`
  - Use for `future-snapshot`
- `references/preset-recipes.md`
  - Use for `session-voice` and `preset-save`
- `references/media-intake.md`
  - Use when raw image, audio, or video files are provided
- `references/media-evidence.md`
  - Use when turning extracted media into evidence cards
- `references/profile-intake.md`
  - Use when collecting explicit self-description and partner-description notes

## Safety Rules

Read `references/safety-boundaries.md` when:

- the user asks for certainty
- the user frames this as a real child
- the user asks for age-play, emotional substitution, or manipulative dependency
- the user wants intimate or exploitative roleplay

Refuse or redirect when needed.

## Output Format

Use the structure in `references/output-template.md`.

Default `portrait` output should include:

1. Evidence basis
2. Parent A style card
3. Parent B style card
4. Successor persona summary
5. Inherited traits
6. Novel traits
7. Speaking style
8. Boundary disclaimer

For other modes:

- `blend-lab`
  - Return a small lineup table or list of variants plus a recommendation.
- `future-snapshot`
  - Return 1 to 3 compact scenes or dialogue snippets, not a long story.
- `session-voice`
  - Return a system-style instruction block and 6 to 12 speaking rules.
- `preset-save`
  - Return preset text plus a structured payload following `assets/persona-schema.json`.

## Scope Control

Default behavior:

- Generate a persona card only for the current request.
- Do not automatically treat it as the permanent assistant persona.

Only apply it as an active session voice if the user explicitly asks.

If the user wants ongoing use, first present a preview card, then ask whether they want:

- preview only
- session persona
- saved preset text
- multiple weighted variants
- sample scenes

## Good Framing Examples

- "I can generate a creative successor persona inspired by the way you two interact."
- "This is a fictional third persona, not a prediction of a real future child."
- "I will use your chat style, emotional rhythm, and humor patterns as creative inputs."
- "I can also turn it into a reusable live-voice preset if you want."

## Bad Framing Examples

- "This is exactly what your child would be like."
- "Your real child will definitely be introverted."
- "This proves who is dominant in the relationship."
- "This output reveals their true inner psychology."

## Detailed References

- Dimensions: `references/extraction-dimensions.md`
- Inheritance logic: `references/inheritance-rules.md`
- Safety policy: `references/safety-boundaries.md`
- Output template: `references/output-template.md`
- Workflow modes: `references/workflow-modes.md`
- Scene rules: `references/scene-generation.md`
- Preset recipes: `references/preset-recipes.md`
- Media intake: `references/media-intake.md`
- Media evidence: `references/media-evidence.md`
- Profile intake: `references/profile-intake.md`
- Extraction script: `scripts/extract-media-bundle.py`
- Structured payload: `assets/persona-schema.json`
