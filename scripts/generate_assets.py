"""Generate self-contained profile artwork. Requires fonttools and brotli.

The banner embeds the existing portfolio sculpture PNG unchanged.
The retrieval diagram is deterministic vector work; no third-party image service.
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
    ground = '#102C35' if dark else '#E5F0F0'
    ink = '#F0F5F2' if dark else '#102C35'
    muted = '#BCD2D5' if dark else '#405E66'
    accent = '#FF865F' if dark else '#CD3A19'
    header_ground = '#121212' if dark else '#EEEDE9'
    header_ink = '#F1F0EC' if dark else '#191919'
    header_muted = '#C2C0BA' if dark else '#52514D'
    for mobile in (False, True):
        if mobile:
            width, height = 640, 200
            parts = [text('Lim Zi Chao', 32, 90, 52, header_ink, 800, -1)]
            parts += [text('Search, data & AI systems.', 34, 132, 24, header_muted)]
            parts += [sculpture(398, -12, 224)]
        else:
            width, height = 1280, 200
            parts = [text('Lim Zi Chao', 44, 96, 64, header_ink, 800, -1.3)]
            parts += [text('Search, data & AI systems.', 47, 141, 27, header_muted)]
            parts += [sculpture(988, -20, 240)]
        name = f'profile-header-{"mobile" if mobile else "desktop"}-{theme}.svg'
        (ASSETS / name).write_text(svg(width, height, 'Lim Zi Chao — Search, data and AI systems.', 'A compact identity banner using the original chrome sculpture from limzichao.com. The full name stays together on one line.', ''.join(parts), header_ground))

    # A literal retrieval diagram, not an illustrative performance chart.
    for mobile in (False, True):
        if mobile:
            w,h = 640, 630
            parts = [text('Two ways to find the answer.',32,62,31,ink,800)]
            parts += [text('Lexical retrieval',32,148,28,ink,800), text('SQLite FTS5 / BM25',32,184,22,muted)]
            parts += [text('Semantic retrieval',32,286,28,ink,800), text('BGE-small / INT8 ONNX',32,322,22,muted)]
            parts += [f'<path d="M480 153H562V380H320V414 M480 291H562" fill="none" stroke="{accent}" stroke-width="3"/>',f'<path d="m312 404 8 10 8-10" fill="none" stroke="{accent}" stroke-width="3"/>']
            parts += [f'<rect x="32" y="433" width="576" height="91" fill="{accent}"/>',text('Reciprocal-rank fusion',54,491,32,ground,800)]
            parts += [text('Combined evidence. Ranked products.',32,589,24,ink)]
        else:
            w,h = 1280,365
            parts = [text('Two ways to find the answer.',44,62,35,ink,800)]
            parts += [text('Lexical retrieval',44,142,29,ink,800),text('SQLite FTS5 / BM25',44,181,23,muted)]
            parts += [text('Semantic retrieval',44,260,29,ink,800),text('BGE-small / INT8 ONNX',44,299,23,muted)]
            parts += [f'<path d="M412 148H527V219H626 M412 266H527V219" fill="none" stroke="{accent}" stroke-width="3"/>',f'<path d="m614 211 12 8-12 8" fill="none" stroke="{accent}" stroke-width="3"/>']
            parts += [f'<rect x="655" y="150" width="579" height="100" fill="{accent}"/>', text('Reciprocal-rank fusion',680,214,38,ground,800),text('Combined evidence. Ranked products.',657,298,25,ink)]
        name=f'copilot-{"mobile" if mobile else "desktop"}-{theme}.svg'
        (ASSETS/name).write_text(svg(w,h,'Shopping Copilot: hybrid retrieval','SQLite FTS5 BM25 lexical retrieval and BGE-small INT8 ONNX semantic retrieval converge through reciprocal-rank fusion into a combined ranking.', ''.join(parts),ground))

print('Generated eight self-contained SVG assets.')
