# Inheritance Rules

This file explains how to combine two parent-style cards into a successor persona.

## Core Principle

Do not simply average two personalities.

Instead use:

1. shared-trait reinforcement
2. weighted blending
3. risk softening
4. creative variation

## Step 1: Reinforce Shared Traits

If both parents strongly show the same trait, strengthen it in the successor persona.

Examples:

- both are playful -> successor is clearly playful
- both are emotionally restrained -> successor is calm and hard to read
- both use humor as repair -> successor likely uses humor to reduce tension

## Step 2: Blend Compatible Traits

For compatible traits, blend by weight.

Examples:

- one is highly online, one is moderately online -> successor has medium-high internetness
- one is warm, one is direct -> successor can become "warm but plain-spoken"

## Step 3: Soften Risky Traits

For risky or destabilizing traits, do not max out.

Always soften these when needed:

- aggression
- harsh contempt
- emotional volatility
- manipulative affection
- high-certainty dominance claims

If both parents show risky versions of a trait, the successor persona should be framed as more stable, not more dangerous.

## Step 4: Add Creative Variation

A successor persona should not be a copy.

Add one or two novel traits that plausibly emerge from the combination.

Examples:

- inherits A's speed and B's patience -> becomes a clearer explainer than either parent
- inherits A's humor and B's softness -> becomes a gentle teaser
- inherits A's reflectiveness and B's meme fluency -> becomes surreal but emotionally perceptive

Mark these as:

- `novel_traits`
- `creative variation`

Never present them as factual predictions.

## Weighting

If the user gives a weighting, follow it.

Examples:

- "60% like A, 40% like B"
- "more like her, but calmer"
- "his humor, her emotional stability"

When the user does not specify weighting:

- start from 50/50
- bias slightly toward the better evidenced source

## Conflict Resolution

### Warmth vs directness

Do not force a contradiction.

Prefer mixed outcomes like:

- blunt but caring
- soft in content, direct in delivery
- practical rather than emotionally effusive

### Playfulness vs seriousness

Combine into:

- playful on the surface, serious underneath
- serious in goals, playful in wording

### High internetness vs low internetness

Prefer moderation unless both are extremely online.

### High expressiveness vs low expressiveness

Do not claim a fixed answer.

Say things like:

- emotionally legible when comfortable
- not overly dramatic, but not fully closed off

## Output Categories

At the end, classify traits into:

- inherited_from_a
- inherited_from_b
- shared_inheritance
- novel_traits
- softened_traits

This makes the synthesis transparent and easier to trust.
