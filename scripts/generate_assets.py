"""Generate self-contained profile artwork. Requires fonttools and brotli.

Geometry is original, deterministic vector work; no third-party image service.
Display text is outlined from the bundled, OFL-licensed Manrope fonts.
"""
from pathlib import Path
from html import escape
import math
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

def field(left, top, width, height, color):
    # Closed, smoothly rounded contours share one silhouette and a clear aperture.
    # Fit the complete Bezier control hull to a reserved artwork box: no cropping.
    count = 64
    points = []
    for j in range(count):
        t = 2 * math.pi * j / count
        radius = 1 + .16 * math.cos(3 * t + .45) + .04 * math.sin(t)
        angle = t - math.pi / 10
        points.append((radius * math.cos(angle), radius * math.sin(angle)))
    segments = []
    for j in range(count):
        previous, start, end, following = [points[k % count] for k in (j - 1, j, j + 1, j + 2)]
        control_a = tuple(start[k] + (end[k] - previous[k]) / 6 for k in (0, 1))
        control_b = tuple(end[k] - (following[k] - start[k]) / 6 for k in (0, 1))
        segments.append((control_a, control_b, end))
    hull = points + [p for segment in segments for p in segment]
    min_x, max_x = min(p[0] for p in hull), max(p[0] for p in hull)
    min_y, max_y = min(p[1] for p in hull), max(p[1] for p in hull)
    center_x, center_y = (min_x + max_x) / 2, (min_y + max_y) / 2
    def position(point, scale):
        return (left + width / 2 + (point[0] - center_x) * scale * width / (max_x - min_x),
                top + height / 2 + (point[1] - center_y) * scale * height / (max_y - min_y))
    paths = []
    for i in range(34):
        scale = .30 + .70 * i / 33
        x, y = position(points[0], scale)
        commands = [f'M {x:.2f},{y:.2f}']
        for segment in segments:
            coordinates = ' '.join(f'{x:.2f},{y:.2f}' for x, y in (position(point, scale) for point in segment))
            commands.append(f'C {coordinates}')
        paths.append(f'<path d="{" ".join(commands)} Z"/>')
    return f'<g data-artwork="contour-mark" fill="none" stroke="{color}" stroke-width="2" stroke-linejoin="round">' + ''.join(paths) + '</g>'

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
            parts += [field(89, 330, 462, 324, accent)]
            parts += [f'<path d="M40 698H600" stroke="{ink}" opacity=".28"/>', text('SEARCH / DATA / AI SYSTEMS', 40, 738, 22, ink)]
        else:
            width, height = 1280, 500
            parts = [text('LIM', 46, 173, 162, ink, 800, -5), text('ZI CHAO', 49, 335, 160, ink, 800, -5)]
            parts += [text('Making information useful.', 54, 402, 28, ink)]
            parts += [field(768, 48, 426, 356, accent)]
            parts += [f'<path d="M54 440H1226" stroke="{ink}" opacity=".28"/>', text('SEARCH / DATA / AI SYSTEMS', 54, 478, 21, ink), text('NUS / SINGAPORE', 995, 478, 18, muted)]
        name = f'profile-header-{"mobile" if mobile else "desktop"}-{theme}.svg'
        (ASSETS / name).write_text(svg(width,height,'Lim Zi Chao — Making information useful.','Search, data, and AI systems. Original nested mathematical contours accompany the typography.', ''.join(parts), ground))

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
