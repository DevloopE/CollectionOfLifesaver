# Collection of Lifesavers · 普林斯顿读本系列

A growing series of Chinese-language math textbooks in the **Adrian Banner / *Calculus Lifesaver* mold** — every concept developed slowly through internal monologue, every method named, every common pitfall called out.

**[📖 Read online (GitHub Pages)](https://devloope.github.io/CollectionOfLifesaver/)**

## 已出版

| 卷 | 书 | 章节数 |
|---|---|---|
| 第一卷 | 普林斯顿多元微积分读本 | 27 章 + 附录 |
| 第二卷 | 普林斯顿线性代数读本 | 25 章 + 2 附录 |
| 第三卷 | 普林斯顿微分方程读本 | 22 章 + 2 附录 |
| 第四卷 | 普林斯顿复分析读本 | 20 章 + 2 附录 |
| 第五卷 | 普林斯顿概率统计读本 | 25 章 + 2 附录 |
| 第六卷 | 普林斯顿偏微分方程读本 | 23 章 + 2 附录 |
| 第七卷 | 普林斯顿实分析读本 | 24 章 + 2 附录 |
| 第八卷 | 普林斯顿测度论与高级实分析读本 | 22 章 + 2 附录 |
| 第九卷 | 普林斯顿调和分析读本 | 20 章 + 2 附录 |
| 第十卷 | 普林斯顿代数拓扑读本 | 20 章 + 2 附录 |
| 第十一卷 | 普林斯顿代数几何读本 | 20 章 + 2 附录 |
| 第十二卷 | 普林斯顿黎曼几何读本 | 20 章 + 2 附录 |
| 第十三卷 | 普林斯顿表示论读本 | 20 章 + 2 附录 |
| 第十四卷 | 普林斯顿范畴论读本 | 20 章 + 2 附录 |

每章一个独立 HTML 文件（13–50 KB），数学符号用 MathJax 渲染（自动从 CDN 加载）。每本书都有共享的 `styles.css` 和上下章导航。

## 本地阅读

直接在浏览器打开 `index.html` 即可。无须任何依赖（MathJax 从公网 CDN 拉）。

## 仓库结构

```
.
├── index.html              # 系列封面 / 入口
├── styles.css              # （由各书目录里独立提供）
│
├── 多元微积分/             # 第一卷
│   ├── index.html          # 目录页
│   ├── ch1.html ... ch27.html
│   ├── appA.html
│   ├── subject-index.html
│   └── styles.css
│
├── 线性代数/               # 第二卷
├── 微分方程/               # 第三卷
├── 复分析/                 # 第四卷
├── 概率统计/               # 第五卷
├── 偏微分方程/             # 第六卷
├── 实分析/                 # 第七卷
│
├── BANNER_METHOD.md        # 写作方法的蒸馏文档
├── split_book.py           # 把单 HTML 切成每章一文件
└── wrap_book.py            # 把 body 片段套上头+导航变成成品
```

## 方法论

详见 [BANNER_METHOD.md](BANNER_METHOD.md) — 完整记录了 Banner 方法的内部脚手架、章节模板、声音风格、应避免的陷阱、写新书的工作流程。

## 致谢

本系列向 Adrian Banner 的 *The Calculus Lifesaver: All the Tools You Need to Excel at Calculus*（Princeton University Press, 2007）致敬。
