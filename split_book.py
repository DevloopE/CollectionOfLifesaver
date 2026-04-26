#!/usr/bin/env python3
"""
把单一 HTML 教材拆成每章一个文件 + 共享 CSS / MathJax + 上下章导航。

用法:
    python split_book.py <input.html> <output_dir> "<book title>"
"""
import sys
import os
import re
from pathlib import Path


def extract_head_pieces(html: str):
    """从原 HTML 抽出 MathJax 配置（含 src）和 <style> 内容。"""
    # MathJax 配置（第一个 <script>...</script> 内含 MathJax = {...}）
    mathjax_cfg_m = re.search(r'<script>\s*\n?\s*MathJax\s*=\s*\{.*?\}\s*;\s*</script>', html, re.DOTALL)
    mathjax_cfg = mathjax_cfg_m.group(0) if mathjax_cfg_m else ''

    # MathJax 加载脚本（含 src 的所有 script，可能多于 1）
    mathjax_loads = re.findall(r'<script[^>]+src=[^>]+mathjax[^>]+></script>', html, re.IGNORECASE)
    mathjax_load_block = '\n'.join(mathjax_loads) if mathjax_loads else \
        '<script src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>'

    # 兜底切换 CDN 脚本
    mathjax_fallback = re.search(r'<script>\s*//\s*备用 CDN.*?</script>', html, re.DOTALL)
    mathjax_fallback_block = mathjax_fallback.group(0) if mathjax_fallback else ''

    # <style>...</style> 整段
    style_m = re.search(r'<style>(.*?)</style>', html, re.DOTALL)
    style_css = style_m.group(1).strip() if style_m else ''

    return mathjax_cfg, mathjax_load_block, mathjax_fallback_block, style_css


def split_chapters(html: str):
    """
    返回 [(id, title, content_html), ...]
    第一项是 (None, '__front__', front_matter_html) — 即首个 <h1 id="chN"> 之前的所有内容（封面 + 前言 + 目录）。
    """
    # 用 <main> 内的内容
    main_m = re.search(r'<main[^>]*>(.*?)</main>', html, re.DOTALL)
    if not main_m:
        raise SystemExit('找不到 <main>')
    main_html = main_m.group(1)

    # 找所有 <h1 id="..."> 的位置
    h1_re = re.compile(r'<h1[^>]*\sid="(ch\d+|appA|appB|appC|index|preface|how-to-use|reverse-index|acknowledgments|toc|learning-habits)"[^>]*>([^<]+)</h1>')
    matches = list(h1_re.finditer(main_html))

    chunks = []
    # 找第一个 chN 的位置——此前都属于"前言+目录"
    first_ch_idx = None
    for i, m in enumerate(matches):
        if m.group(1).startswith('ch') or m.group(1) in ('appA', 'appB', 'appC'):
            first_ch_idx = i
            break

    if first_ch_idx is None:
        raise SystemExit('找不到任何 chN / appA / appB 锚点')

    front = main_html[:matches[first_ch_idx].start()].strip()
    chunks.append(('__front__', '前言与目录', front))

    # 对每个章节锚点切片
    chap_matches = matches[first_ch_idx:]
    # 只保留 chN/appX 这种"真正的章"，不要中途的 sub-h1
    chap_matches = [m for m in chap_matches if re.match(r'(ch\d+|appA|appB|appC|subject-index)$', m.group(1)) or m.group(1) == 'index']

    for i, m in enumerate(chap_matches):
        ch_id = m.group(1)
        ch_title = m.group(2)
        start = m.start()
        end = chap_matches[i + 1].start() if i + 1 < len(chap_matches) else len(main_html)
        body = main_html[start:end].strip()
        chunks.append((ch_id, ch_title, body))

    return chunks


def write_styles_css(out_dir: Path, style_css: str):
    """写共享 styles.css；若原 HTML 的 style 含 @import google fonts 则保留。"""
    (out_dir / 'styles.css').write_text(style_css, encoding='utf-8')


def head_template(book_title: str, page_title: str, mathjax_cfg: str, mathjax_load: str, mathjax_fallback: str) -> str:
    return f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{page_title} — {book_title}</title>
<link rel="stylesheet" href="styles.css">
{mathjax_cfg}
{mathjax_load}
{mathjax_fallback}
</head>
<body>
<main>
'''


def nav_bar(prev_id, prev_title, next_id, next_title, has_index=True) -> str:
    parts = []
    if has_index:
        parts.append('<a href="index.html">⌂ 目录</a>')
    if prev_id:
        parts.append(f'<a href="{prev_id}.html">← 上一章 · {prev_title}</a>')
    else:
        parts.append('<span class="nav-disabled">← 上一章</span>')
    if next_id:
        parts.append(f'<a href="{next_id}.html">下一章 · {next_title} →</a>')
    else:
        parts.append('<span class="nav-disabled">下一章 →</span>')
    return f'<nav class="page-nav">{"".join(parts)}</nav>\n'


# 额外 CSS 片段：导航栏样式（追加到 styles.css）
EXTRA_CSS = '''
/* ---------- 章节间导航条 ---------- */
nav.page-nav {
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 1rem;
  flex-wrap: wrap;
  margin: 2rem 0;
  padding: 0.85em 1em;
  background: var(--boxed-bg);
  border: 1px solid var(--boxed-border);
  border-radius: 4px;
  font-size: 0.92em;
}

nav.page-nav a {
  border: none;
  color: var(--accent);
  text-decoration: none;
}

nav.page-nav a:hover {
  text-decoration: underline;
}

nav.page-nav .nav-disabled {
  color: var(--rule);
}

/* 章节间导航条：底部那条留出与上一段间距 */
h1 + nav.page-nav,
nav.page-nav + h1 { margin-top: 0; }

/* TOC 卡片化，目录页更可读 */
nav.toc {
  margin: 2rem 0;
}

@media (max-width: 640px) {
  nav.page-nav {
    flex-direction: column;
    align-items: flex-start;
    font-size: 0.85em;
  }
}
'''


def split_book(input_html: Path, out_dir: Path, book_title: str):
    out_dir.mkdir(parents=True, exist_ok=True)

    html = input_html.read_text(encoding='utf-8')

    mathjax_cfg, mathjax_load, mathjax_fallback, style_css = extract_head_pieces(html)
    chunks = split_chapters(html)

    # 写共享 CSS
    write_styles_css(out_dir, style_css + EXTRA_CSS)

    # chunks[0] 是 front-matter, 后续都是章节
    front_matter = chunks[0][2]
    chapters = chunks[1:]

    # 把"索引"重命名为 subject-index 避免与 index.html 冲突
    chapters = [
        ('subject-index' if cid == 'index' else cid, ctitle, body)
        for cid, ctitle, body in chapters
    ]
    chap_titles = [(cid, ctitle) for cid, ctitle, _ in chapters]

    # 写 index.html（封面 + 前言 + 目录）
    index_body = re.sub(r'href="#(ch\d+|appA|appB|appC)"', r'href="\1.html"', front_matter)
    index_body = re.sub(r'href="#index"', r'href="subject-index.html"', index_body)
    index_body = (
        f'<nav class="page-nav"><a href="{chap_titles[0][0]}.html">从第一章开始 →</a></nav>\n\n'
        + index_body
        + '\n\n'
        + f'<nav class="page-nav"><a href="{chap_titles[0][0]}.html">从第一章开始 →</a></nav>\n'
    )
    index_html = (
        head_template(book_title, '目录', mathjax_cfg, mathjax_load, mathjax_fallback)
        + index_body
        + '\n</main>\n</body>\n</html>\n'
    )
    (out_dir / 'index.html').write_text(index_html, encoding='utf-8')

    # 写每一章
    for i, (cid, ctitle, body) in enumerate(chapters):
        prev_id, prev_title = (chap_titles[i - 1] if i > 0 else (None, None))
        next_id, next_title = (chap_titles[i + 1] if i + 1 < len(chap_titles) else (None, None))

        # 章节内部把 href="#chN" 之类的内部跳转也指到对应文件
        body_fixed = re.sub(r'href="#(ch\d+|appA|appB|appC)"', r'href="\1.html"', body)
        body_fixed = re.sub(r'href="#index"', r'href="subject-index.html"', body_fixed)

        nav = nav_bar(prev_id, prev_title, next_id, next_title)
        page = (
            head_template(book_title, ctitle, mathjax_cfg, mathjax_load, mathjax_fallback)
            + nav
            + body_fixed
            + '\n'
            + nav
            + '\n</main>\n</body>\n</html>\n'
        )
        (out_dir / f'{cid}.html').write_text(page, encoding='utf-8')

    print(f'已写入 {out_dir}/ ：')
    print(f'  index.html')
    for cid, ctitle, _ in chapters:
        print(f'  {cid}.html  —  {ctitle}')
    print(f'共 {len(chapters)} 章 + 索引页')


if __name__ == '__main__':
    if len(sys.argv) < 4:
        print('用法: python split_book.py <input.html> <output_dir> "<book title>"')
        sys.exit(1)
    split_book(Path(sys.argv[1]), Path(sys.argv[2]), sys.argv[3])
