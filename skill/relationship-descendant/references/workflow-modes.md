# Workflow Modes

Use this file to choose the right mode for the request.

## Mode Selection

### portrait

Choose when:

- the request is the first pass
- the user says "generate one persona"
- the user has not decided how they want to use it

Output:

- one strong successor persona
- parent cards
- inherited traits
- disclaimer

### blend-lab

Choose when:

- the user wants options
- the user says "more like A/B"
- the user wants several versions before deciding

Output:

- 2 to 4 variants
- clear naming
- one recommendation

### future-snapshot

Choose when:

- the user wants immersion
- the user asks "what would they sound like"
- the user wants dialogue or scenes

Output:

- short scene pack
- not a full story
- grounded in the selected variant

### session-voice

Choose when:

- the user wants to chat with the persona
- the user wants an active assistant style
- the user wants rules for ongoing conversation

Output:

- a compact system-style instruction block
- speaking rules
- soft boundaries

### preset-save

Choose when:

- the user wants a reusable version
- the user wants to store, copy, or reapply the persona
- the user wants something that can later be refined

Output:

- preset name
- preset text
- structured payload

## Recommended Sequences

Default sequence:

1. portrait
2. blend-lab only if the user wants alternatives
3. future-snapshot only after a variant exists
4. session-voice or preset-save only after the user confirms they want persistence

Fast sequence for advanced users:

1. portrait
2. session-voice
3. preset-save

## Quality Control

Before finalizing any mode:

- restate the evidence basis
- mark unclear areas as low-confidence
- keep the persona same-age unless the user explicitly asks otherwise
- keep novelty plausible, not random
- keep the disclaimer visible
