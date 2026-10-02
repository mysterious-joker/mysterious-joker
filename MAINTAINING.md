# Maintaining this GitHub profile

The presentation lives in README.md and eight self-contained SVGs in assets/. It is designed for GitHub Flavored Markdown; do not add external CSS, JavaScript, iframes, or live counters.

## Updating content

Edit README.md for factual changes. The user confirmed Year 2 at NUS, a current data engineering internship, and using the employer name Theme International Trading. The original profile and résumé-derived material are the source of employment dates, availability, academic history, and TechJam leadership/placement. Public project repositories supply architecture and product context. Keep development-set metrics scoped and team achievements distinct from individual contributions.

Private research projects, internal data, credentials, and the résumé PDF stay unpublished. Contact links use the existing public email and LinkedIn. Personal work belongs to mysterious-joker; school projects belong to lzc-nus.

## Regenerating artwork

Use Python with fonttools and brotli installed, then run `python scripts/generate_assets.py`. Manrope source fonts and their SIL Open Font License are bundled under scripts/fonts/. SVG lettering is outlined so assets need no external font request. All artwork is authored vector geometry; there are no third-party image services or generated photographs.

Header and Copilot assets each have desktop/mobile and light/dark variants. Keep the mobile sources before the desktop sources in picture markup. Verify at GitHub reading width and 390px viewport, in both themes. Core facts and links must remain usable without images.

## Preview and publishing

The local design repository has a separate history from the live profile at github.com/mysterious-joker/mysterious-joker. Publish approved updates from a fresh checkout of the live repository, copying the README, artwork, generator, licensed fonts, and documentation into that checkout. Commit on top of its current main branch and push normally. Preserve both histories; never force-push to connect them.

`scripts/preview.py` renders a local reading-column preview for visual inspection; it is not a deployable replacement for the README. Review screenshots and generated preview files are ignored by Git.
