"""Render a local GitHub-style reading-column preview. Requires markdown-it-py."""
from pathlib import Path
from markdown_it import MarkdownIt

root = Path(__file__).resolve().parents[1]
body = MarkdownIt('commonmark', {'html': True}).enable('table').render((root / 'README.md').read_text())
css = """
:root { color-scheme:light dark; --bg:#fff; --fg:#1f2328; --muted:#59636e; --line:#d1d9e0; --link:#0969da; --code:#818b981f; }
@media(prefers-color-scheme:dark) { :root { --bg:#0d1117; --fg:#f0f6fc; --muted:#9198a1; --line:#3d444d; --link:#4493f8; --code:#656c7633; } }
* { box-sizing:border-box; }
body { margin:0; padding:40px 24px; background:var(--bg); color:var(--fg); font:16px/1.5 -apple-system,BlinkMacSystemFont,'Segoe UI',Arial,sans-serif; }
.profile { max-width:896px; padding:24px 32px 32px; margin:auto; border:1px solid var(--line); border-radius:6px; }
.file-label { font-size:12px; color:var(--muted); margin:0 0 20px; }
article { overflow-wrap:break-word; }
article > :first-child { margin-top:0; }
p,ul,ol,table,details { margin-top:0; margin-bottom:16px; }
a { color:var(--link); text-decoration:none; }
a:hover { text-decoration:underline; }
a:focus-visible,summary:focus-visible { outline:2px solid var(--link); outline-offset:3px; }
h1,h2,h3,h4 { margin-top:24px; margin-bottom:16px; line-height:1.25; font-weight:600; }
h1 { font-size:2em; }
h2 { font-size:1.5em; padding-bottom:.3em; border-bottom:1px solid var(--line); }
h3 { font-size:1.25em; }
h4 { font-size:1em; }
strong { font-weight:600; }
img { max-width:100%; height:auto; vertical-align:middle; }
picture { display:block; margin-bottom:16px; }
ul,ol { padding-left:2em; }
li+li { margin-top:.25em; }
details summary { cursor:pointer; }
details[open] summary { margin-bottom:16px; }
table { border-spacing:0; border-collapse:collapse; display:block; max-width:100%; overflow:auto; }
th,td { padding:6px 13px; border:1px solid var(--line); }
th { font-weight:600; }
code { font-size:85%; background:var(--code); padding:.2em .4em; border-radius:6px; }
hr { height:1px; border:0; background:var(--line); margin:24px 0; }
@media(max-width:600px) { body { padding:16px; } .profile { padding:16px; } }
"""
page = '<!doctype html><html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1"><base href="/"><title>Lim Zi Chao — GitHub profile preview</title><style>' + css + '</style></head><body><main class="profile"><p class="file-label">mysterious-joker / README.md</p><article>' + body + '</article></main></body></html>'
(root / 'output').mkdir(exist_ok=True)
(root / 'output/preview.html').write_text(page)
print('Preview: output/preview.html')
