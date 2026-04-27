# 普林斯顿抽象代数读本 — 写作 SPEC

## 总体定位
- 系列第 9 卷
- 受众：本科 / 研究生预备代数课
- 风格：Adrian Banner 内独白、concrete-then-general、动机先于定义
- 全书 24 章 + 附录 A、B + 主题索引

## 章节风格强制项（每章必须）
- 中文（简体），无纯英文段
- 每章一个独立 HTML 文件
- **长度：14K-22K 字节 HTML（≈ 5K-9K 中文字符内容）**
- 结构：nav → h1 → 开头 2-3 段 motivating prose → `<ul>` outline list → ≥6 个 `<h2 id="secN-K">N.K 标题</h2>` 节 → 结尾段（forward-reference 下一章）→ nav
- ≥6 节，≥4 例题（散在正文，不写"例 4.2.1"标签），≥4 个 `\boxed{...}` display 公式
- `<ul>` 列表频繁使用（章首 outline + 节内 bullet 总结）
- 你 / 我们 大致平衡，"我们"略多
- 跨卷链接用 `../book/chN.html`，前面 8 卷书名：多元微积分 / 线性代数 / 微分方程 / 复分析 / 概率统计 / 偏微分方程 / 实分析 / 泛函分析

## 严禁
- 脚手架小标题：本章地图 / 本章目标 / 本章导览 / 学习要点 / 本节小结 / 关键要点
- AI 腔："让我们一起" / "首先我们要" / "总结一下" / "综上所述"
- HTML 实体写重音字符：用直接 UTF-8 (é 而不是 `&eacute;`)
- 编号例题标签

## HTML 模板（每章必须用这个 head）
```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>第 N 章 {标题} — 普林斯顿抽象代数读本</title>
<link rel="stylesheet" href="styles.css">
<script>
  MathJax = {
    tex: {
      inlineMath: [['\\(', '\\)'], ['$', '$']],
      displayMath: [['\\[', '\\]'], ['$$', '$$']],
      processEscapes: true,
      tags: 'none',
      packages: {'[+]': ['boldsymbol', 'cases', 'ams']},
      macros: {
        oiint:  ['\\mathop{\\vphantom{\\int}\\unicode[Times]{x222F}}\\nolimits', 0],
        oiiint: ['\\mathop{\\vphantom{\\int}\\unicode[Times]{x2230}}\\nolimits', 0]
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
</script>
</head>
<body>
<main>
<nav class="page-nav"><a href="index.html">⌂ 目录</a><a href="chN-1.html">← 上一章 · 第 N-1 章 上一章标题</a><a href="chN+1.html">下一章 · 第 N+1 章 下一章标题 →</a></nav>
<h1 id="chN">第 N 章 {标题}</h1>

{正文内容：开头段 + ul + 6+ h2 节 + 结尾段}

<nav class="page-nav"><a href="index.html">⌂ 目录</a><a href="chN-1.html">← 上一章 · 第 N-1 章 上一章标题</a><a href="chN+1.html">下一章 · 第 N+1 章 下一章标题 →</a></nav>
</main>
</body>
</html>
```

第 1 章 prev nav: `<span class="nav-disabled">← 上一章</span>`
第 24 章 next nav: `<span class="nav-disabled">下一章 →</span>`
appA prev: ch24, next: appB
appB prev: appA, next: subject-index
subject-index prev: appB, no next (or omit)

## 全书章节列表（每章可正确 prev/next nav 与 forward-reference）

| # | 标题 |
|---|---|
| 1 | 引论：从对称到代数结构 |
| 2 | 群的定义与基本例子 |
| 3 | 子群、陪集、Lagrange 定理 |
| 4 | 同态与正规子群 |
| 5 | 商群与三大同构定理 |
| 6 | 群作用、轨道、稳定子 |
| 7 | Sylow 定理 |
| 8 | 有限交换群的结构定理 |
| 9 | 对称群 \(S_n\) 与置换 |
| 10 | 自由群、生成元与关系 |
| 11 | 环：定义与基本例子 |
| 12 | 理想与商环 |
| 13 | 整环、域、商域 |
| 14 | 主理想环与唯一分解 |
| 15 | 多项式环 |
| 16 | 模的入门 |
| 17 | PID 上有限生成模的结构定理 |
| 18 | 域的扩张 |
| 19 | 代数扩张与最小多项式 |
| 20 | 分裂域与正规扩张 |
| 21 | Galois 理论基本定理 |
| 22 | 应用 Galois：尺规作图与五次方程不可解 |
| 23 | 应用：编码理论与有限域 |
| 24 | 应用：晶体学与表示论入门 |
| appA | 集合、关系、等价类速查 |
| appB | 范畴论一瞥 |
| subject-index | 主题索引 |

## 章首 outline list 模板（在 h1 后立即用 ul）
```html
<p>开头第一段：直接进入主题，给出本章的核心问题或动机。</p>
<p>第二段：把本章要做的事情说穿，可以做对比（"X 在 ch5 是 Y，本章我们要把它推到 Z"）。</p>
<ul>
  <li>第一节做什么。</li>
  <li>第二节做什么。</li>
  <li>...（共 6+ 条对应 6+ 个 h2 节）</li>
</ul>
```

## 节内常用结构
- 定义后立刻给一个具体例子
- 例子前后用 prose 连接，不用"例 1.2"标签
- 重要公式或定理结论放 `\boxed{...}`：`\[\boxed{...}\]`
- 长定理证明分小节或用编号步骤
- 跨章引用："详见<a href='chN.html'>第 N 章 N.K 节</a>"
- 跨卷引用："详见<a href='../线性代数/chN.html'>《线性代数读本》第 N 章</a>"

## 写作示范段（参考 已写好的 第 1-7 卷 的 ch1.html，特别是 实分析/ch1.html 与 泛函分析/ch1.html）
- 你 / 我们 平衡：每章 你 出现 20-50 次，我们 出现 15-50 次
- 不要"换句话说"过度（< 5 次/章）
- 抒情笔调要有但克制（1-3 个 metaphor / 章）
- ul 列表多用：每章 5-15 个 ul

## 已经写好的（不要重写）
- index.html（前言 + 目录）
- styles.css

## 你要写的：见 batch 各自的指令，输出到 `C:/Users/Devlo/Desktop/Princeton/抽象代数/<file>.html`
