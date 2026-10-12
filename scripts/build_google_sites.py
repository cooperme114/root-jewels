#!/usr/bin/env python3
"""Build a standalone Root Jewels HTML file for Google Sites' Embed code."""
from pathlib import Path
import base64
import json
import re

root = Path(__file__).resolve().parent.parent
html = (root / "index.html").read_text(encoding="utf-8")
roots = (root / "roots.js").read_text(encoding="utf-8")
sprites = []
for n in range(1, 11):
    file = root / "sprites" / f"gem-{n:02d}.png"
    sprites.append("data:image/png;base64," + base64.b64encode(file.read_bytes()).decode("ascii"))

# Replace external scripts with inline data; this file works without GitHub Pages.
sprite_script = "const GEM_SPRITES = " + json.dumps(sprites) + ";"
for filename, source in (("roots.js", roots), ("gem-sprites.js", sprite_script)):
    pattern = r'<script\s+src="' + re.escape(filename) + r'"\s*></script>'
    html, count = re.subn(pattern, lambda _: "<script>\n" + source + "\n</script>", html, count=1)
    if count != 1:
        raise RuntimeError(f"Missing expected script tag for {filename}")

out = root / "dist"
out.mkdir(exist_ok=True)
(out / "root-jewels-google-sites.html").write_text(html, encoding="utf-8")
(out / "copy-into-google-sites.txt").write_text(html, encoding="utf-8")
print("Built standalone Root Jewels with all ten PNG sprites and vocabulary embedded.")
print("Download the root-jewels-google-sites artifact from this Actions run.")
