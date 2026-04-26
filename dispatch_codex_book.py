#!/usr/bin/env python3
"""
派 N 个 codex exec 并行写一本书的若干批章节。
用法：python dispatch_codex_book.py <book_dir> <batches.json>
batches.json 是 {batch_id: prompt_string, ...}
"""
import sys, json, subprocess, os, tempfile
from pathlib import Path

if len(sys.argv) < 3:
    print("usage: dispatch_codex_book.py <book_dir> <batches.json>")
    sys.exit(1)

book_dir = Path(sys.argv[1])
batches = json.loads(Path(sys.argv[2]).read_text(encoding='utf-8'))

procs = []
for bid, prompt in batches.items():
    pf = Path(tempfile.gettempdir()) / f"codex_{book_dir.name}_{bid}_prompt.txt"
    pf.write_text(prompt, encoding='utf-8')
    log = Path(tempfile.gettempdir()) / f"codex_{book_dir.name}_{bid}.log"
    cmd = (
        f'codex exec -c model_reasoning_effort=xhigh --sandbox workspace-write '
        f'< "{pf}" > "{log}" 2>&1 &'
    )
    print(f"dispatching {bid}: {cmd}")
    subprocess.Popen(cmd, shell=True, cwd=str(Path.cwd()))
print(f"派出 {len(batches)} 个 codex exec 并行作业")
