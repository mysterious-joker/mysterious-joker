"""Generate self-contained profile artwork. Requires fonttools and brotli.

The banner embeds the existing portfolio sculpture PNG unchanged.
No third-party image service is used.
Display text is outlined from the bundled, OFL-licensed Manrope fonts.
"""
from pathlib import Path
from html import escape
import base64
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / 'assets'
ASSETS.mkdir(exist_ok=True)
FONTS = {w: TTFont(Path(__file__).parent / f'fonts/manrope-{w}.woff') for w in (600, 800)}

def text(value, x, y, size, color, weight=600, tracking=0):
    font = FONTS[weight]
    glyphs = font.getGlyphSet()
    cmap = font.getBestCmap()
    scale = size / font['head'].unitsPerEm
    out = []
    for char in value:
        name = cmap.get(ord(char), '.notdef')
        pen = SVGPathPen(glyphs)
        glyphs[name].draw(pen)
        if pen.getCommands():
            out.append(f'<path d="{pen.getCommands()}" transform="translate({x:.2f} {y}) scale({scale:.6f} {-scale:.6f})"/>')
        x += glyphs[name].width * scale + tracking
    return f'<g fill="{color}" aria-label="{escape(value)}">' + ''.join(out) + '</g>'

def svg(width, height, title, desc, content, background):
    provenance = ("Typography: Manrope, SIL OFL. Banner raster provenance: assets/portfolio-sculpture-chrome.asset.json."
                  if 'data-artwork="portfolio-sculpture"' in content else
                  "Original mathematical vector artwork. Typography: Manrope, SIL OFL.")
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" role="img" aria-labelledby="title desc">
<title id="title">{escape(title)}</title><desc id="desc">{escape(desc)}</desc>
<!-- {provenance} Regenerate with scripts/generate_assets.py. -->
<rect width="{width}" height="{height}" fill="{background}"/>
{content}
</svg>"""

SCULPTURE = base64.b64encode((ASSETS / 'portfolio-sculpture-chrome.png').read_bytes()).decode('ascii')

def sculpture(x, y, size):
    return (f'<image data-artwork="portfolio-sculpture" x="{x}" y="{y}" '
            f'width="{size}" height="{size}" href="data:image/png;base64,{SCULPTURE}"/>')

for theme in ('light', 'dark'):
    dark = theme == 'dark'
    header_ground = 'none'
    header_ink = '#F1F0EC' if dark else '#191919'
    header_muted = '#C2C0BA' if dark else '#52514D'
    for mobile in (False, True):
        if mobile:
            width, height = 640, 200
            parts = [text('Lim Zi Chao', -4.16, 90, 52, header_ink, 800, -1)]
            parts += [text('Search, data & AI systems.', -0.876, 132, 24, header_muted)]
            parts += [sculpture(418, -12, 224)]
        else:
            width, height = 1280, 200
            parts = [text('Lim Zi Chao', -5.12, 96, 64, header_ink, 800, -1.3)]
            parts += [text('Search, data & AI systems.', -0.986, 141, 27, header_muted)]
            parts += [sculpture(1040, -20, 240)]
        name = f'profile-header-{"mobile" if mobile else "desktop"}-{theme}.svg'
        (ASSETS / name).write_text(svg(width, height, 'Lim Zi Chao — Search, data and AI systems.', 'A compact identity banner using the original chrome sculpture from limzichao.com. The full name stays together on one line.', ''.join(parts), header_ground))

print('Generated four self-contained profile banners.')
