# Mechanic Trust

AI product case study for a consumer mobile app that helps drivers understand car issues, judge whether a repair quote is fair, and find trustworthy mechanics.

## Why this exists

Auto repair is a high-anxiety, high-information-asymmetry category. When a driver gets a repair quote, they usually have no reliable way to know whether the repair is necessary, whether the price is fair, or which nearby mechanic is actually trustworthy.

Mechanic Trust is designed to reduce that uncertainty through three layers: AI-powered issue assessment, transparent local price ranges, and trust-ranked shops with social proof signals.

## Product thesis

People do not just want a mechanic directory. They want confidence in a high-stakes moment.

The product is built on four beliefs:
- AI should inform, not overclaim.
- Pricing should be shown as a defensible range, not false precision.
- Trust should come from verification, review quality, and social proof.
- Multimodal input reduces friction in stressful, mobile-first moments.

## Core flow

Diagnose issue → assess urgency → show fair price range → recommend trusted shops for that repair type.

## Key product decisions

| Decision | Chosen approach | Why it matters |
|---|---|---|
| User input | Photo, voice, and text | Drivers in stressful situations may not want to type carefully. |
| Pricing | Fair price range instead of a single estimate | A range is more credible than false precision. |
| Recommendations | Repair-type-specific trusted shops | Nearby shops alone create noise; repair relevance increases signal. |
| AI UX | Confidence score and priority tier | Users need transparency about uncertainty, not overconfident outputs. |

## AI systems thinking

Quality was framed across three dimensions: relevance, calibration, and actionability. The case study also defines explicit failure modes such as confident-but-wrong diagnosis, overconfidence on ambiguous input, underspecified user input, and trust scores that do not feel earned.

The product principle is transparency over authority: the AI should help users make better decisions, not present itself as a certified mechanic.

## What this project demonstrates

- Consumer AI product thinking in a trust-sensitive category.
- Product judgment under ambiguity before live data integrations existed.
- Eval-first reasoning through confidence calibration, failure-mode design, and guardrails.
- End-to-end solo ownership across product decisions, UX, AI prompt design, and trust-scoring logic.

## Current status

Beta prototype, pre-launch. The UX and product logic were validated through walkthroughs, while live pricing, shop, and contacts integrations remain future work.

## Full case study

See [Mechanic Trust Case Study](./docs/Mechanic-Trust-Case-Study.pdf)
