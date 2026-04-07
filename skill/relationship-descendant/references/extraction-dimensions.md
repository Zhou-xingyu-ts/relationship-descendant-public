# Extraction Dimensions

Use this file to turn relationship data into structured style cards.

## Goal

Extract interaction style, not objective truth.

Every estimate should be framed as:

- "appears"
- "suggests"
- "tends toward"
- "in this sample"

Do not claim certainty.

## Parent Style Card Schema

Use this schema for both source personas.

```text
parent_style_card:
  label:
  evidence_sources:
  warmth: 1-10
  directness: 1-10
  humor: 1-10
  internetness: 1-10
  emotional_expressiveness: 1-10
  patience: 1-10
  playfulness: 1-10
  social_energy: 1-10
  abstraction: 1-10
  meme_density: 1-10
  conflict_style:
  affection_style:
  language_texture:
  recurring_signals:
  caveats:
```

## Dimension Definitions

### warmth

- 1-3: distant, dry, restrained
- 4-7: moderate warmth, selective softness
- 8-10: openly warm, nurturing, reassuring

### directness

- 1-3: indirect, buffered, cautious
- 4-7: balanced
- 8-10: blunt, immediate, highly explicit

### humor

- 1-3: rarely jokes
- 4-7: occasional light humor
- 8-10: humor is a core interaction mode

### internetness

- 1-3: plain, offline-style wording
- 4-7: some online rhythm or slang
- 8-10: strongly shaped by internet language and culture

### emotional_expressiveness

- 1-3: restrained
- 4-7: readable but controlled
- 8-10: highly open or emotionally legible

### patience

- 1-3: quickly frustrated or terse
- 4-7: moderate tolerance
- 8-10: calm, explanatory, durable

### playfulness

- 1-3: serious or literal
- 4-7: some teasing or improvisation
- 8-10: playful energy is common

### social_energy

- 1-3: low-key, quiet, low stimulation
- 4-7: moderate
- 8-10: energetic, expansive, animated

### abstraction

- 1-3: plain, concrete
- 4-7: mixed
- 8-10: metaphorical, stylized, abstract, literary, or memetic

### meme_density

- 1-3: almost no meme references
- 4-7: moderate meme awareness
- 8-10: meme culture strongly shapes expression

## Qualitative Fields

### conflict_style

Choose a short phrase such as:

- avoids conflict and softens
- argues directly but cools down fast
- jokes through tension
- withdraws first, explains later
- escalates fast, repairs later

### affection_style

Choose a short phrase such as:

- teasing affection
- practical care
- verbal reassurance
- quiet consistency
- high-energy praise

### language_texture

Describe the feel of the language:

- short and clipped
- soft and repetitive
- meme-heavy and jumpy
- reflective and literary
- teacher-like and structured

## Evidence Rules by Modality

### Chats

Best evidence for:

- directness
- humor
- meme density
- conflict handling
- affection style
- language texture

### Voice

Best evidence for:

- social energy
- emotional expressiveness
- patience
- warmth

### Images

Best evidence for:

- aesthetic cues
- visible energy
- shared taste hints

Do not infer deep personality from images alone.

### Manual User Notes

High priority.

If the user gives explicit interpretation, include it, but still mark it as user-provided context rather than objective evidence.
