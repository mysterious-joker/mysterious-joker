---
name: Lim Zi Chao — Compact Portfolio Signature
description: GitHub-native engineering profile with a compact banner using the original portfolio sculpture.
colors:
  header-ink-light: "#191919"
  header-ink-dark: "#F1F0EC"
  header-muted-light: "#52514D"
  header-muted-dark: "#C2C0BA"
typography:
  display:
    fontFamily: Manrope
    fontWeight: 800
  annotation:
    fontFamily: Manrope
    fontWeight: 600
---

# Compact portfolio signature

The banner follows the user's explicit direction: reuse the original chrome sculpture from limzichao.com and spend substantially less vertical space on the name. It is a short identity strip followed immediately by the portfolio link, current role, and inspectable engineering work. The previous abstract contour, custom monogram, two-line name, and oversized cover composition are superseded.

## Banner

Desktop uses a 1280 × 200 viewBox; mobile uses 640 × 200. At the tested reading widths this is approximately 130px tall on desktop and 100px on mobile. Keep Lim Zi Chao on one line: Lim is the surname, Zi Chao the given name. Use title case and weight-800 outlined Manrope at 64 SVG units on desktop and 52 on mobile. The weight-600 descriptor uses 27 and 24 units respectively. All factual profile text remains selectable Markdown.

The banner background is transparent so the header shares GitHub’s reading surface. The visible left edge of the name and descriptor aligns exactly with the native biography, navigation, headings, and project paragraphs. Their first-glyph side bearings are compensated in the SVG coordinates. The complete chrome sculpture sits on the right. Do not add a second logo, an uppercase discipline footer, a location tag, or decorative contours.

The sculpture is the existing transparent PNG at assets/portfolio-sculpture-chrome.png, copied unchanged from the portfolio's public/images/projects/portfolio-sculpture-chrome.png. Its adjacent .asset.json records the source and SHA-256. It is embedded into each SVG as PNG data, allowing the complete header to render as one self-contained GitHub image. It is an existing Three.js render, not generated or redrawn artwork. The transparent image bounds extend beyond the banner, but the visible sculpture remains complete.

## Native reading structure

GitHub owns the body font, prose spacing, link states, focus treatment, and reading column. README.md ships no stylesheet or JavaScript. The opening portfolio link leads to limzichao.com. Selected projects use actual source links and concise evidence. Native details/summary elements expose evaluation context, earlier experience, academic foundation, tools, experiments, and availability. The current employer remains Theme International Trading; completed infrastructure work and ongoing exploration remain distinct.

## Project structure

Every selected project uses the same left-aligned native structure: heading, short metadata line, description, technology line, and source links. Shopping Copilot has no extra architecture image or panel. Its SQLite FTS5/BM25 and BGE-small INT8 ONNX retrieval explanation remains selectable text inside the engineering disclosure. Do not regenerate the removed Copilot SVGs.

## Sources and responsive behavior

The four header variants pair desktop/mobile with light/dark. Picture source order is dark-mobile, light-mobile, dark-desktop, then light-desktop fallback. The mobile breakpoint is max-width: 600px. Keep image alt text meaningful and the core biography usable without images. Update the header URL version when replacing artwork so the revised asset receives a new browser cache key.

Regenerate with scripts/generate_assets.py using fonttools and brotli. Licensed Manrope source fonts and SIL OFL remain under scripts/fonts/. Header PNG provenance is recorded alongside the source asset. scripts/preview.py is a local GitHub-style preview, not a deployed site; its wrapper CSS does not define the profile's design system.

Verification covers local desktop/mobile light/dark views, image loading, complete sculpture visibility, and the compact header height. Verify the published GitHub image separately because local rendering does not prove GitHub's image delivery.
