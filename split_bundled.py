#!/usr/bin/env python3
"""把"多章塞一个文件"的 body 按 <h1 id="chN"> 边界拆开"""
import re, sys
from pathlib import Path

bundled_files = sys.argv[1:]
for bf in bundled_files:
    p = Path(bf)
    text = p.read_text(encoding='utf-8')
    parts = re.split(r'(?=<h1\s+id="ch\d+")', text)
    if len(parts) <= 1:
        print(f"{bf}: only one h1 found, skipping")
        continue
    # First part may be empty/junk before first h1
    if not re.match(r'\s*<h1', parts[0]):
        parts = parts[1:]
    for chunk in parts:
        m = re.match(r'<h1\s+id="(ch\d+)"', chunk)
        if not m:
            continue
        cid = m.group(1)
        outfile = p.parent / f'{cid}.html'
        outfile.write_text(chunk.strip() + '\n', encoding='utf-8')
        print(f"  wrote {outfile.name} ({len(chunk)} bytes)")
    p.unlink()
    print(f"  removed {p.name}")
