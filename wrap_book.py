#!/usr/bin/env python3
"""
把 _bodies/ 里的 body 片段套上头部+上下章导航，写成成品的 ch1.html、ch2.html 等。

用法:
    python wrap_book.py <book_dir> "<book title>"
"""
import sys
import re
from pathlib import Path

MATHJAX_CONFIG = '''<script>
  MathJax = {
    tex: {
      inlineMath: [['\\\\(', '\\\\)'], ['$', '$']],
      displayMath: [['\\\\[', '\\\\]'], ['$$', '$$']],
      processEscapes: true,
      tags: 'none',
      packages: {'[+]': ['boldsymbol', 'cases', 'ams']},
      macros: {
        oiint:  ['\\\\mathop{\\\\vphantom{\\\\int}\\\\unicode[Times]{x222F}}\\\\nolimits', 0],
        oiiint: ['\\\\mathop{\\\\vphantom{\\\\int}\\\\unicode[Times]{x2230}}\\\\nolimits', 0]
      }
    },
    svg: { fontCache: 'global' }
  };
</script>
<script src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js" id="mathjax"></script>
<script>
  document.getElementById('mathjax').onerror = function() {
    var s = document.createElement('script');
    s.src = 'https://cdnjs.cloudflare.com/ajax/libs/mathjax/3.2.2/es5/tex-mml-chtml.js';
    document.head.appendChild(s);
  };
</script>'''


def head_block(book_title, page_title):
    return f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{page_title} — {book_title}</title>
<link rel="stylesheet" href="styles.css">
{MATHJAX_CONFIG}
</head>
<body>
<main>
'''


def nav_bar(prev_id, prev_title, next_id, next_title):
    parts = ['<a href="index.html">⌂ 目录</a>']
    if prev_id:
        parts.append(f'<a href="{prev_id}.html">← 上一章 · {prev_title}</a>')
    else:
        parts.append('<span class="nav-disabled">← 上一章</span>')
    if next_id:
        parts.append(f'<a href="{next_id}.html">下一章 · {next_title} →</a>')
    else:
        parts.append('<span class="nav-disabled">下一章 →</span>')
    return '<nav class="page-nav">' + ''.join(parts) + '</nav>\n'


def chapter_order(bodies_dir: Path):
    """决定章节顺序：ch1, ch2, ..., chN, appA, appB, subject-index"""
    order = []
    # ch1, ch2, ...
    ch_files = sorted(
        [f for f in bodies_dir.glob('ch*.html')],
        key=lambda f: int(re.match(r'ch(\d+)', f.stem).group(1))
    )
    order.extend(ch_files)
    # appA, appB ...
    app_files = sorted(bodies_dir.glob('app*.html'))
    order.extend(app_files)
    # subject-index 最后
    si = bodies_dir / 'subject-index.html'
    if si.exists():
        order.append(si)
    return order


def extract_h1_title(body_html: str):
    """从 body 里抽出 <h1>...</h1> 文本作为页面标题"""
    m = re.search(r'<h1[^>]*>(.*?)</h1>', body_html, re.DOTALL)
    if m:
        text = re.sub(r'<[^>]+>', '', m.group(1)).strip()
        return text
    return '正文'


def wrap_book(book_dir: Path, book_title: str):
    bodies_dir = book_dir / '_bodies'
    if not bodies_dir.exists():
        raise SystemExit(f'找不到 {bodies_dir}')

    # 章节有序列表
    files = chapter_order(bodies_dir)
    titles_by_id = {}
    for f in files:
        body = f.read_text(encoding='utf-8')
        titles_by_id[f.stem] = extract_h1_title(body)

    print(f'共 {len(files)} 章/附录待包装')

    # 写 index.html（前言+目录）
    index_body_file = bodies_dir / 'index_body.html'
    if index_body_file.exists():
        index_body = index_body_file.read_text(encoding='utf-8')
        first_id = files[0].stem if files else None
        nav_top = ''
        if first_id:
            nav_top = f'<nav class="page-nav"><a href="{first_id}.html">从第一章开始 →</a></nav>\n\n'
        index_html = (
            head_block(book_title, '目录')
            + nav_top
            + index_body
            + '\n\n'
            + nav_top
            + '\n</main>\n</body>\n</html>\n'
        )
        (book_dir / 'index.html').write_text(index_html, encoding='utf-8')
        print(f'  写入 index.html')

    # 写每一章
    for i, f in enumerate(files):
        cid = f.stem
        body = f.read_text(encoding='utf-8')
        title = titles_by_id[cid]

        prev_id = files[i - 1].stem if i > 0 else None
        prev_title = titles_by_id.get(prev_id, '')
        next_id = files[i + 1].stem if i + 1 < len(files) else None
        next_title = titles_by_id.get(next_id, '')

        nav = nav_bar(prev_id, prev_title, next_id, next_title)

        # body 内可能含 href="#chN" 形式的内部链接，转换成 chN.html
        body_fixed = re.sub(r'href="#(ch\d+|appA|appB|appC)"', r'href="\1.html"', body)
        body_fixed = re.sub(r'href="#index"', r'href="subject-index.html"', body_fixed)

        page = (
            head_block(book_title, title)
            + nav
            + body_fixed
            + '\n'
            + nav
            + '\n</main>\n</body>\n</html>\n'
        )
        (book_dir / f'{cid}.html').write_text(page, encoding='utf-8')
        print(f'  写入 {cid}.html  ({title})')

    print('完成')


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('用法: python wrap_book.py <book_dir> "<book title>"')
        sys.exit(1)
    wrap_book(Path(sys.argv[1]), sys.argv[2])
