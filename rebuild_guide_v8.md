# Mechanic Trust Deck — Rebuild Guide (v8)

## Color Palette (Updated)

| Name | Hex | Usage |
|---|---|---|
| Navy Blue | `#1E3A6E` | Cover hero block, footer bar |
| Bright Blue | `#2563EB` | Section header squares, underlines, tag borders, accents |
| Text Black | `#111827` | Section headings, bold labels |
| Text Dark | `#1F2937` | All body text (much darker than previous) |
| Text Medium | `#374151` | Secondary text, metadata values |
| Text Light | `#6B7280` | Captions (still readable) |
| White | `#FFFFFF` | Page background, hero text, footer text |
| Hero Subtitle | `#CBD5E8` | Subtitle/author lines inside hero block |
| Hero Small | `#8899B8` | "Beta prototype" line inside hero |
| Card Border | `#D1D5DB` | Table borders, card outlines |
| Table Header BG | `#E5E9F0` | Table header row fill |
| Tag BG | `#EFF3FF` | Tag pill background |
| Tag Border | `#2563EB` | Tag pill border (matches bright blue) |
| Quote BG | `#F8F9FB` | Quote box fill |

## Typography

All fonts: **Helvetica** (or Helvetica Neue / Inter as web alternative)

| Element | Size | Weight | Color | Leading |
|---|---|---|---|---|
| Cover "AI PRODUCT PORTFOLIO" | 9pt | Bold | `#8899B8` | 12 |
| Cover title "Mechanic Trust" | 36pt | Bold | `#FFFFFF` | — |
| Cover subtitle | 14pt | Regular | `#CBD5E8` | — |
| Cover author line | 12pt | Regular | `#CBD5E8` | — |
| Cover "Beta prototype" | 9pt | Regular | `#8899B8` | — |
| Tag pills | 7.5pt | Bold | `#2563EB` | — |
| Metadata labels | 9pt | Bold | `#111827` | — |
| Metadata values | 8.5pt | Regular | `#374151` | — |
| Section header (■■ 01 · Title) | 20pt | Bold | `#1E3A6E` | — |
| Subsection heading | 11pt | Bold | `#111827` | 15 |
| Body text | 9.5pt | Regular | `#1F2937` | 14 |
| Bullet text | 9.5pt | Regular | `#1F2937` | 14 |
| CAPS label | 8.5pt | Bold | `#374151` | 12 |
| Table header | 8.5pt | Bold | `#111827` | 12 |
| Table cell | 8–8.5pt | Regular | `#1F2937` | 11–12 |
| Band title | 9pt | Bold | `#111827` | 12 |
| Caption | 8pt | Regular | `#6B7280` | 11 |
| Quote text | 10pt | Italic | `#374151` | 15 |
| Footer text | 8pt | Italic/Regular | `#FFFFFF` | — |

## Page Layout

| Property | Value |
|---|---|
| Page size | US Letter (8.5 × 11 in) |
| Left/Right margin | 0.6 in (43.2 pt) |
| Top margin | 0.5 in |
| Bottom margin | 0.5 in + 26pt footer bar |
| Content width | ~7.3 in (525.6 pt) |
| Footer bar height | 26pt, full-width, `#1E3A6E` fill |

## Section Header Pattern

1. Two 8×8 px squares in `#2563EB`, spaced 4px apart
2. 10px gap
3. "01 · Title" in 20pt Helvetica-Bold `#1E3A6E`
4. 1.5pt horizontal rule in `#2563EB` spanning full content width, 12pt below text

## Footer Bar (every page)

- Full-width rectangle, height 26pt, fill `#1E3A6E`
- Left text (8pt Helvetica-Italic, white): "Mechanic Trust — AI Product Portfolio"
- Right text (8pt Helvetica, white): "Ruthvik Arepelly · Page N"

## Cover Page Layout

- Hero block: `#1E3A6E` fill, spans full content width, ~480pt tall
- Inside hero (left-aligned, 24pt left padding):
  - "AI PRODUCT PORTFOLIO · CASE STUDY" at top (9pt Bold `#8899B8`)
  - "Mechanic Trust" (36pt Bold white) centered vertically
  - "Closing the Trust Gap in Auto Repair" (14pt `#CBD5E8`)
  - "Ruthvik Arepelly · AI Product Manager · Tampa, FL" (12pt `#CBD5E8`)
  - "Beta prototype · Built with v0 by Vercel · Pre-launch" (9pt `#8899B8`) at bottom
- Tag strip: 4 pills with `#2563EB` border, `#EFF3FF` fill, 7.5pt bold blue text
- Metadata row: 4 columns (Type / Stage / Built with / Domain)

## Table Styling

- Borders: 0.5pt `#D1D5DB`
- Header row: `#E5E9F0` fill, Helvetica-Bold
- Cell padding: 5pt top/bottom, 7pt left/right
- Body cells: white fill

## APP SCREENS Band Pattern

- Bold 9pt title in all caps: "APP SCREENS — [NAME]"
- Row of 3–4 screenshots, each 1.4–2.0 in wide, evenly spaced
- Caption below each: 8pt center-aligned `#6B7280`

## Per-Page Content Summary

| Page | Section(s) | Layout |
|---|---|---|
| 1 | Cover | Hero block + tags + metadata |
| 2 | 01 · Problem Statement | One-Sentence + Deeper Gap (story+$80B+why now) + 3 screenshots |
| 3 | 02 · Company Context | Two-column (Stage/Maturity/Risk | Constraints + Right Bet) |
| 4 | 03 Tech Stack + 04 Tradeoffs + 05 Metrics | Three stacked tables |
| 5 | 06 · AI Systems (screenshots) | Diagnose Flow (4 imgs) + Results (4 imgs) |
| 6 | Eval details (continuation) | Two-column text (Quality/Failures | Guardrails/Next) |
| 7 | 07 Judgment + 08 What Would Break | Two stacked tables |
| 8 | 09 · Scope Ownership | 2×2 grid + 4 screenshots + quote box |
