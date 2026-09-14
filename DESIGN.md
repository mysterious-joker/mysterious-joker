# Developer Studio design system

## Purpose and hierarchy

A recruiter-facing, code-led portfolio for **mysterious-joker**. Personal work leads; **lzc-nus** is the secondary NUS archive. The first viewport pairs a large editorial headline with an open, interactive developer desk. A project selector connects the desk to direct repository links. Shopping Copilot appears first and explicitly identifies the team implementation and competition-kit fork; school work follows in its own section. Preserve source attribution and account distinctions. Do not add unsupported identity, degree, employment, or contact claims.

## Color and material

| CSS token | Value | Role |
| --- | --- | --- |
| `--bg` | `#14171c` | Graphite page background |
| `--ink` | `#f2f1ed` | Main text and primary CTA |
| `--muted` | `#a6afbd` | Supporting copy and metadata |
| `--blue` | `#91b5ff` | Links, focus, headline accent |
| `--line` | `#343b45` | Fine section separators |
| `--panel` | `#1c222b` | NUS introduction panel |

Selected project buttons use `#28374e` with `#bed3ff` text; hover uses `#252d38`. Long project descriptions use `#c7ced7`; hero copy uses `#bcc4cf`. Rounded corners are restrained: 7px selectors, 8px CTA/navigation, 12px school panel. Avoid adding decorative cards around the open project rows.

The procedural Three.js desk uses graphite/slate surfaces, silver hardware and cobalt equipment. Project screen accents are blue `#719eff`, gold `#d6bb84` and green `#99d7ad`. Screen typography mixes sans-serif project names with monospace commands and technical details. Cool hemisphere/key/fill lighting, soft shadows and ACES filmic tone mapping give the hardware volume without obscuring the page.

## Typography and layout

Locally hosted Manrope provides genuine 400 and 700 weights, `font-display: swap`, sans-serif fallback and disabled font synthesis. Desktop H1 is `clamp(52px, 6.5vw, 94px)`, 700, 1.02 line height, −0.04em tracking. H2 is 40px/1.2 with −0.03em tracking; project H3 is 32px/1.2, 400. Body descriptions use 15px/1.85 and a 68ch maximum. Metadata and technology labels use 11–12px; navigation is 13px.

Page content caps at 1440px with 64px desktop gutters. The hero uses a 41%/59% split, 620px minimum height and a 540px scene. The selector is a horizontal ruled strip, followed by its live description. Main section spacing is 80px. Repository rows use 40%/60% columns with 20px gaps and 40px/48px vertical padding. The school introduction is a single quieter panel; the footer caps at 1312px.

At 1000px and below, gutters become 32px, the hero becomes 43%/57%, H1 is 65px and the scene is 485px. At 700px and below, the hero stacks with copy first, content gutters become 24px (header 22px), H1 becomes 58px, and the scene becomes 380px. Project buttons occupy a full second selector row; their small NUS suffixes hide while full account context remains in the document. Project rows, school introduction and footer stack. Secondary header anchor links hide; GitHub remains visible. Main H2 becomes 31px and project H3 30px.

## Controls and resilient behavior

Native project buttons update selected styling, `aria-pressed`, the source URL, live description and monitor contents together. Shopping Copilot is the default. Clicking the monitor cycles projects; books select their associated project. These scene gestures supplement the ordinary buttons and repository links.

Pointer drag rotates within bounded horizontal and vertical angles. Touch drag changes horizontal angle while retaining vertical page scrolling (`touch-action: pan-y`). Auto-rotation starts off and requires the explicit toggle; its label changes to “Stop rotation.” Reset restores the initial camera and stops rotation. Pixel ratio caps at 1.5; rendering skips hidden/offscreen views. Optional diagnostics exist only with `?inspect`.

WebGL construction failures show a plain-language fallback and disable camera controls. Context loss pauses the scene with recovery guidance. Repository links and document content remain available independently of rendering. Project selector wiring is established before WebGL initialization.

## Accessibility rules

Keep semantic header/navigation/main/sections/articles/footer, the ordered heading hierarchy, skip-to-projects link, accessible navigation labels and real anchors. Decorative SVGs and arrow glyphs are hidden from assistive technology. The scene has a descriptive image label; keyboard users use the native project and camera buttons. Selected states use both appearance and `aria-pressed`; descriptions announce changes through `aria-live="polite"`.

Interactive focus uses a 2px cobalt outline with 6px offset. Project and camera buttons have 44px minimum height. Underlined contextual/source links remain visibly identifiable. Reduced-motion preference removes smooth anchor scrolling and camera interpolation; rotation stays opt-in. Preserve readable muted text and the unanimated, fully linked project content when extending the scene.

## Shipping scope

This document records the implementation in `dist/index.html`, `dist/style.css` and `dist/studio.js`. The visual system is an open graphite/cobalt developer studio with restrained panels and immediate source access. Continue to verify desktop/mobile layout, keyboard controls, project/source synchronization and WebGL fallback before shipping changes; do not replace repository evidence with unsupported promotional claims.
