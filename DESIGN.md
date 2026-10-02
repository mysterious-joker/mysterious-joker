---
name: Lim Zi Chao — Engineering Monograph
description: GitHub-native engineering profile with authored mathematical vector artwork.
colors:
  burnt-orange: "#CD3A19"
  warm-coral: "#FF865F"
  glacier: "#E5F0F0"
  petroleum: "#102C35"
  pale-ink: "#F0F5F2"
  slate-ink: "#405E66"
  mist-ink: "#BCD2D5"
typography:
  display:
    fontFamily: "Manrope"
    fontWeight: 800
  annotation:
    fontFamily: "Manrope"
    fontWeight: 600
rounded:
  square: "0px"
components:
  artwork-light:
    backgroundColor: "{colors.glacier}"
    textColor: "{colors.petroleum}"
    rounded: "{rounded.square}"
  artwork-dark:
    backgroundColor: "{colors.petroleum}"
    textColor: "{colors.pale-ink}"
    rounded: "{rounded.square}"
  fusion-light:
    backgroundColor: "{colors.burnt-orange}"
    textColor: "{colors.glacier}"
    rounded: "{rounded.square}"
  fusion-dark:
    backgroundColor: "{colors.warm-coral}"
    textColor: "{colors.petroleum}"
    rounded: "{rounded.square}"
---

# Design System: Lim Zi Chao — Engineering Monograph

## Overview

**Creative North Star: "Engineering Monograph"**

An engineering monograph pairs an unmistakable name with inspectable work. Original nested mathematical contours bring authorship to the opening; a literal retrieval diagram makes the same visual language useful inside the project evidence. Glacier and deep petroleum surfaces carry warm orange geometry, with outlined Manrope lettering giving the artwork a precise, substantial voice.

The surrounding document belongs to GitHub. Selectable prose, real links, headings, tables, and native disclosures carry the factual story. The artwork is static and self-contained. This record refreshes the obsolete graphite/cobalt 3D-banner direction to match the implemented README and eight repository-owned SVGs.

**Key Characteristics:**
- Authored vector geometry with a finite visual vocabulary.
- A large typographic identity followed by readable, selectable evidence.
- Theme-specific artwork and deliberately recomposed mobile layouts.
- Native GitHub links and disclosure instead of simulated application controls.

## Colors

### Primary

Burnt orange defines contours, connector strokes, and fusion blocks on light artwork. Warm coral performs those same roles on dark artwork. These are paired theme accents, not independent categories or status colors.

### Neutral

Glacier is the light artwork ground, with petroleum primary lettering and slate secondary annotation. Petroleum becomes the dark ground, with pale primary lettering and mist secondary annotation. Fusion-block text takes the artwork's ground color. Native prose and link colors remain controlled by GitHub rather than by these artwork tokens.

**The Paired Theme Rule.** Every artwork has light and dark variants; change the surface, ink, annotation, and accent together.

## Typography

**Display Font:** Manrope, outlined from the bundled weight-800 font.
**Annotation Font:** Manrope, outlined from the bundled weight-600 font.
**Body Font:** GitHub's native reading interface; the README does not ship a body font or stylesheet.

The artwork uses a deliberately discontinuous hierarchy: a very large name, a modest sentence, and smaller contextual text. Diagram headings and stage names share the heavy display voice; explanatory labels use the annotation voice. All SVG lettering is path geometry, so no browser font fallback or external request is required.

Sizes are composition coordinates, not a reusable CSS type scale. The desktop name uses 162 and 160 SVG units; mobile uses 99 and 112. Diagram lettering spans 23–38 units on desktop and 22–32 on mobile. The rendered size follows the selected SVG's scale. The frontmatter therefore records shared family and weights without inventing global font-size or line-height tokens.

**Name grouping.** Lim is the surname; Zi Chao is the complete given name. Keep Zi Chao together on one line and preserve the family-name-first display order.

**The Selectable Evidence Rule.** Keep core identity, employment, project claims, and destinations in Markdown; outlined image lettering is supplementary.

## Layout

The README is one native reading column. Project sections use headings, prose, a compact stack line, and source links; secondary evaluation, earlier experience, academic foundation, tools, experiments, and availability sit inside native disclosures. No CSS grid, app shell, or custom viewport container ships in the README.

Artwork uses a full-width image with proportional height. Header viewBoxes are 1280 × 500 on desktop and 640 × 780 on mobile; retrieval diagrams are 1280 × 365 and 640 × 630. At a maximum viewport width of 600px, picture sources choose mobile artwork. Source order is dark-mobile, light-mobile, dark-desktop, then the light-desktop image fallback. Preserve that ordering so a general dark source does not preempt the mobile source.

The desktop header balances the name against the contour field; mobile stacks name, sentence, contour, and discipline line. The retrieval diagram moves from side-by-side convergence into vertically arranged stages. Artwork margins are authored per composition rather than instances of a shared spacing scale. GitHub controls the prose spacing and available reading width.

**The Recomposition Rule.** Below the picture breakpoint, select the dedicated mobile composition instead of shrinking the desktop artwork into a narrow column.

## Elevation & Depth

All art is flat. Forty-two nested parametric contours make a dense plotter field through line spacing and overlap. They are original two-dimensional geometry, not a measured performance graph. Thin rules separate contextual information. The retrieval illustration uses literal connector geometry and a solid fusion block. There are no custom hover elevations or animations.

**The Flat Geometry Rule.** Use line density, contrast, and negative space for structure; the artwork has no shadows, gradients, or simulated 3D material.

## Shapes

Artwork bounds and fusion blocks are square rectangles. The header's fluid closed contours contrast with the diagram's orthogonal branching connectors. The field uses a 1.7-unit stroke; diagram connectors use 3-unit strokes in SVG coordinates. Directional arrowheads in the technical diagram are drawn paths that explain data flow. They are distinct from the removed outbound-link glyphs.

## Components

### Identity artwork

Four header SVGs pair theme and viewport variants. Their composition contains the two-line name (LIM / ZI CHAO), sentence, original contour field, and discipline line; the desktop version also includes the NUS/Singapore annotation. The diagram and header share the artwork palettes and outlined font weights. Images have meaningful alt text, while each SVG also includes a title and description. They are static images with no hover or focus states.

### Retrieval illustration

Four Copilot SVGs show lexical and semantic retrieval converging through reciprocal-rank fusion. Stage labels name SQLite FTS5/BM25 and BGE-small/INT8 ONNX. The diagram's arrow paths express architecture, not a clickable action. Light and dark fusion blocks use their matching accent and ground-color lettering.

### Text navigation and project entries

The opening portfolio link is bold, followed by LinkedIn, Email, and NUS work. Slash separators are plain text. Project headings are actual links followed by short evidence and explicit source destinations. There are no custom buttons, card containers, badge systems, or input fields to inherit. Native GitHub link hover and keyboard focus behavior apply.

### Evidence disclosure

A real details/summary element hides secondary material until requested. Summary text is strong; the platform's disclosure marker communicates state. Earlier experience uses its own disclosure with roles in reverse chronology, separate from academic foundation. The current internship remains visible, with completed infrastructure work distinguished from ongoing exploration. Contents remain ordinary selectable Markdown. The toolkit is a native two-column table, not a custom dashboard.

**The Native Interaction Rule.** Links navigate and disclosures reveal deeper evidence; GitHub supplies their live interaction styling.

The sidecar includes exact inline SVG specimens and native HTML specimens. CSS attached to native specimens only reproduces the local reading preview for the design panel; it does not ship in README.md. Static SVG specimens deliberately have no interaction states.

## Do's and Don'ts

### Do:

- Do regenerate all eight SVGs from scripts/generate_assets.py after artwork changes.
- Do retain bundled Manrope source fonts and their SIL Open Font License under scripts/fonts/.
- Do verify desktop and 390px mobile reading in both themes, including picture selection and disclosure behavior.
- Do keep factual Markdown and descriptive image alt text usable when artwork is unavailable.
- Do keep the public employer name Theme International Trading consistent with the current user instruction.

### Don't:

- Don't introduce external CSS, JavaScript, iframes, live counters, or simulated website controls into the README.
- Don't replace actual technical evidence with decorative metrics or present development-set measurements as production guarantees.
- Don't reintroduce outbound arrow glyphs as link icons; the implemented links use text labels.
- Don't treat the preview wrapper, its typography, or its GitHub-like CSS as a project-owned web design system.
- Don't treat a local preview as verification of the live GitHub profile; check the published README separately.

Implementation evidence: README.md, scripts/generate_assets.py, assets/*.svg, PRODUCT.md, .impeccable/profile-brief.md, and MAINTAINING.md. Regenerate artwork with Python plus fonttools and brotli. No raster asset or image-generation provenance is required for this deterministic vector implementation.

Verification scope: the complete README was rendered and inspected locally, with desktop/mobile and light/dark screenshots. A generic GitHub picture-markup test passed; that is not a live render of the finished profile. No remote is configured. The final scored finish verdict is tracked separately from this design record.

Not canonized: the obsolete 3D-banner direction, removed outbound arrow glyphs, and preview-only wrapper styles. The small uppercase discipline footer describes the engineer's actual subject areas; it is not a general eyebrow or kicker pattern for future sections.
