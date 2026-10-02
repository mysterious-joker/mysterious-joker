"""Generate self-contained profile artwork. Requires fonttools and brotli.

Geometry is original, deterministic vector work; no third-party image service.
Display text is outlined from the bundled, OFL-licensed Manrope fonts.
"""
from pathlib import Path
from html import escape
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
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" role="img" aria-labelledby="title desc">
<title id="title">{escape(title)}</title><desc id="desc">{escape(desc)}</desc>
<!-- Original mathematical vector artwork. Typography: Manrope, SIL OFL. Regenerate with scripts/generate_assets.py. -->
<rect width="{width}" height="{height}" fill="{background}"/>
{content}
</svg>"""

def monogram(left, top, size, color):
    # L is the family initial; Z and C stay grouped as the given-name initials.
    # A shared 32-unit module ties the straight L/Z to the rounded, open C.
    paths = [
        'M16 16H48V272H80V304H16Z',
        'M88 16H304V48L148 112H304V144H88V112L244 48H88Z',
        'M304 176H152C116.65 176 88 204.65 88 240C88 275.35 116.65 304 152 304H304V272H152C134.33 272 120 257.67 120 240C120 222.33 134.33 208 152 208H304Z',
    ]
    return (f'<g data-artwork="lzc-monogram" fill="{color}" '
            f'transform="translate({left} {top}) scale({size / 320:.6f})" '
            'aria-label="LZC: Lim Zi Chao">' +
            ''.join(f'<path d="{path}"/>' for path in paths) + '</g>')

for theme in ('light', 'dark'):
    dark = theme == 'dark'
    ground = '#102C35' if dark else '#E5F0F0'
    ink = '#F0F5F2' if dark else '#102C35'
    muted = '#BCD2D5' if dark else '#405E66'
    accent = '#FF865F' if dark else '#CD3A19'
    for mobile in (False, True):
        if mobile:
            width, height = 640, 780
            parts = [text('LIM', 36, 112, 99, ink, 800, -3), text('ZI CHAO', 35, 224, 112, ink, 800, -3)]
            parts += [text('Making information useful.', 39, 280, 26, ink)]
            parts += [monogram(140, 322, 360, accent)]
            parts += [f'<path d="M40 698H600" stroke="{ink}" opacity=".28"/>', text('SEARCH / DATA / AI SYSTEMS', 40, 738, 22, ink)]
        else:
            width, height = 1280, 500
            parts = [text('LIM', 46, 173, 162, ink, 800, -5), text('ZI CHAO', 49, 335, 160, ink, 800, -5)]
            parts += [text('Making information useful.', 54, 402, 28, ink)]
            parts += [monogram(810, 48, 356, accent)]
            parts += [f'<path d="M54 440H1226" stroke="{ink}" opacity=".28"/>', text('SEARCH / DATA / AI SYSTEMS', 54, 478, 21, ink), text('NUS / SINGAPORE', 995, 478, 18, muted)]
        name = f'profile-header-{"mobile" if mobile else "desktop"}-{theme}.svg'
        (ASSETS / name).write_text(svg(width,height,'Lim Zi Chao — Making information useful.','Search, data, and AI systems. An original geometric LZC monogram groups the surname initial L with the given-name initials ZC.', ''.join(parts), ground))

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
