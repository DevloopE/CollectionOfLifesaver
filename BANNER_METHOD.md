# The Banner Method: A Complete Distillation of *The Calculus Lifesaver*

A working blueprint extracted from Adrian Banner's *The Calculus Lifesaver: All the Tools You Need to Excel at Calculus* (Princeton University Press, 2007 / Chinese 普林斯顿微积分读本, 修订版 2016). Use this document as the recipe to write a book in the same mold — for calculus or for any other technical subject.

---

## Part 0 — The One-Sentence Thesis

> A textbook should not just present the mathematics; it should externalize the mind of an expert solving problems out loud, so the student can copy the *thinking*, not just the *result*.

Every other choice in the book follows from this thesis.

---

## Part 1 — Author's Stance Toward the Reader

### 1.1 The reader is a real person, not an abstract "student"

Banner addresses the reader directly in second person ("你") on every page. He never writes *"the student"* or *"one"*. The reader is treated as:

- A capable adult who *wants* to learn (not someone being forced).
- Not necessarily strong: someone who may be cramming for a midterm next week, or someone who already passed the course but feels they didn't really understand it.
- Anxious. The book repeatedly defuses anxiety: "Wait! The exam is next week and I haven't learned anything! Where do I start?" — and then answers that question.

### 1.2 Three reader types are explicitly addressed

In the preface, Banner lists three audiences:
1. First-time learner.
2. Exam reviewer.
3. Someone who already learned calculus and wants to *truly* understand it.

The book provides a different navigation strategy for each (see Part 6, "Apparatus"). When you write your own book, name the audiences in the preface and tell each how to read the book.

### 1.3 The author is a peer, not a priest

Banner makes himself fallible and human. He says "I" and "we" rather than "the author". He admits when something is hard: *"OK, this looks scary, but..."*. He apologizes when notation is ugly. He invites email about errors. He links to a personal website.

This is the trust contract: *I will not pretend this is easy when it isn't, and in exchange you will trust me when I tell you something is straightforward.*

### 1.4 Honesty about what isn't in the book

Banner explicitly tells the reader:
- "Where are the hundreds of practice problems? Not here — buy a problem book."
- "Where are the rigorous proofs? In Appendix A. The main text uses the intuitive form."
- "Why aren't there summary boxes at the end of each chapter? Because *you* should write them — that's the learning."

Negative space matters. Decide what your book is *not* and say so.

---

## Part 2 — The Pedagogical Method

This is the operating system. Every section in the book runs the same micro-loop.

### 2.1 The "Internal Monologue" (内心独白) Principle

Banner's central pedagogical innovation. He does not show clean polished solutions. He shows the *thought process that produces* a solution. This is what every section actually does:

```
1. Pose a problem.
2. Voice the natural first reaction. ("This looks like ...")
3. Voice the doubt or correction. ("But wait, that won't work because ...")
4. Voice the reframe. ("So instead, let's try ...")
5. Carry out the reframe.
6. Verify.
7. Distill into a method.
```

Compare to a normal textbook, which does steps 5 + 7 only.

The internal monologue answers the student's universal complaint: *"I understood every step but I would never have come up with that on my own."* Banner's response: *here is what you would have come up with, in slow motion.*

### 2.2 The Concrete-Then-General Loop

Banner *never* states the general rule first. The pattern is invariably:

> **Specific number → Specific symbolic → General rule → Apply rule to new specific.**

Example from Chapter 2 (trig review):
- He computes sin(7π/6) by drawing a unit circle and labeling a specific point.
- *Then* he names the construction: "this little angle is called the *reference angle*."
- *Then* he states the ASTC rule for sign.
- *Then* he gives a numbered procedure for any sin/cos/tan of any angle.
- *Then* he runs the procedure on cos(7π/4) and tan(9π/13).

Example from Chapter 14 (L'Hôpital):
- A specific 0/0 limit, computed by linear approximation near a point.
- The approximation is `f(x) ≈ f'(a)(x − a)` and `g(x) ≈ g'(a)(x − a)`.
- The ratio is `f'(a)/g'(a)`.
- *Now* state the rule.
- Re-do the original limit using the rule.
- Then a harder example, then a meta-example (when do you re-apply?).

**The rule for writing**: never write a "Theorem N.M" before a numerical example demonstrates *why the theorem must say what it says*.

### 2.3 The Three Layers of Justification

Banner teaches every important fact at three layers, in this order:

| Layer | What it gives | Where it lives |
|---|---|---|
| **Numerical experiment** | "Try sin(0.1) on a calculator. Got 0.0998. So sin(x) ≈ x for small x." | Main text |
| **Geometric / visual** | "Look at the graph of sin and y = x near 0. They sit on top of each other." | Main text, with figure |
| **Algebraic derivation** | "Write tan(x) = sin(x)/cos(x). Both numerator and denominator behave..." | Main text |
| **Rigorous proof** | ε-δ argument with sandwich theorem, etc. | Appendix A |

The first three are mandatory for understanding; the fourth is optional and physically separated. This separation is the most under-imitated feature of the book. It lets the main text move at the speed of intuition without lying.

### 2.4 The "Worked Example as Proof Sketch" Move

When Banner introduces a new technique (substitution, integration by parts, partial fractions) he does not write a formal theorem and then "examples follow". He inverts the order:

1. Picks a specific integral.
2. Tries to compute it by guessing.
3. The guess fails. He explains *why* it fails.
4. Modifies the guess. It works.
5. Steps back: "What did we just do? Let me name the move."
6. *Now* abstracts the move into a method.

The reader feels they discovered the method. Compare this to "By the substitution rule, let u = ..." which requires the reader to trust an oracle.

### 2.5 Recurring Voice Moves (the rhetorical micro-toolkit)

These specific phrases recur dozens of times each. They are the conversational glue:

- "OK / 好吧" — bridges from problem statement to thinking.
- "Wait! / 等等!" — interrupts a wrong path before the reader follows it.
- "Hmm / 嗯" — admits genuine difficulty.
- "Why? Because... / 为什么? 因为..." — never a fact without a reason.
- "Notice that / 注意" — flags a subtle invariant.
- "But this means... / 但这意味着..." — turns a fact into a consequence.
- "What would happen if...? / 如果...会怎样?" — counterfactual exploration.
- "Don't worry, / 别担心," — defuses anxiety before introducing notation.
- "You might think... but actually... / 你可能会想... 但其实..." — anticipates and corrects misconception.
- "Try it yourself before reading on / 在继续阅读之前, 先自己尝试一下" — the active-learning prompt.
- "We've seen this before in Section X.Y / 我们在第X.Y节中已经见过这个" — explicit cross-reference.
- "We'll come back to this in Chapter N / 我们将在第N章再回到这个问题" — forward reference.

When you write your book, install these. They are not filler; they are the load-bearing wall of the conversational style.

### 2.6 Categorize Every Problem Type

Banner believes (correctly) that students need a *taxonomy* of problems more than they need clever tricks. Every chapter that is computational ends with a flowchart-style classifier.

Examples:
- Limit problems: "rational as x→a", "rational as x→∞", "with √", "trig ÷ x near 0", "exponential at ∞"...
- L'Hôpital types: "Type A: 0/0", "Type A: ∞/∞", "Type B1: ∞ − ∞", "Type B2: 0·∞", "Type C: 1^∞ / 0^0 / ∞^0".
- Integration techniques: substitution, by parts, partial fractions, trig sub, trig identities.
- Series convergence tests: nth term, geometric, p-series, comparison, limit comparison, ratio, root, integral, alternating, absolute.

Each type gets:
1. A name.
2. A diagnostic ("how do I know I'm in this case?").
3. A standard recipe.
4. A worked example.
5. Cross-reference back from the master flowchart.

This is the book's promise: *given any standard problem you'll see, this book has a recipe for it.* Hence the title "Lifesaver".

### 2.7 Anticipate the Misconception, Then Correct It

Whenever there is a subtle point, Banner first voices the *wrong* intuition and then corrects it. Examples:

- After defining lim, "you might think we just plug in x = a, but consider this function with a hole..."
- After ASTC, "if you got cos(7π/4) = 1/√2 you might also think it's negative; but ASTC tells us..."
- For improper integrals: "you might think that since the function is bounded on [0,1] there's no problem, but..."
- For ε-δ: "you might think δ = ε always works, but for x², it has to depend on..."

This is *inoculation*. The reader meets the wrong idea inside the safety of the book, instead of meeting it for the first time on an exam.

### 2.8 Acknowledge When Something is Hard

Banner never claims something is "obvious" unless he can show why in the next sentence. When a topic *is* genuinely difficult he labels it: "This is one of the hardest ideas in the book. Take your time."

He also marks optional sections (like 7.1.5 "Proof of an important limit") with markers in the navigation table, telling exam-crammers they may skip.

---

## Part 3 — Composition Patterns

How a chapter is built from the inside.

### 3.1 The Chapter Skeleton

Every chapter follows the same template:

```
[Chapter N: Topic Name]

  Opening paragraph (1–2 short paragraphs):
    - One concrete motivating sentence ("To talk about how fast things change, we need ...").
    - "In this chapter we will cover:"
    - Bulleted list of 4–8 sub-topics, in the order they appear.

  Section N.1, N.2, ... (typically 3–6 sections):
    Each begins with a one-sentence framing.
    Each contains 1–4 sub-sub-sections.
    Each contains 2–6 worked examples.
    Each ends by setting up the next section.

  Final section often labeled:
    "A general method", "Summary of techniques", or "How to recognize the case".
    Contains a flowchart-style decision procedure.

  No formal "Summary" or "Exercises" at chapter end.
    The reader is expected to write their own summary; problems are in a separate workbook.
```

### 3.2 The Section Skeleton

A typical numbered section contains:

```
N.M Section Title

  Framing sentence: connect to previous section.
  Concrete example or question to motivate.
  Walk through example informally.
  State the rule, definition, or theorem in a labeled block (italic or boxed).
  Re-do the example using the rule explicitly.
  Show 1–3 more examples, each with new wrinkle:
    - same rule, different surface form
    - same rule, harder algebra
    - same rule, edge case
  If applicable: "what could go wrong" warning.
  Cross-reference to where the rigorous proof lives (usually Appendix A).
  Transition sentence to next section.
```

### 3.3 The Worked Example Skeleton

Banner's worked examples are not just "Example: compute X. Solution: Y."  They follow a script:

```
"For instance, consider [problem]."

  [Problem statement, often boxed or set off.]

  "First, notice that ..."
  [Observation that begins to classify the problem.]

  "If we tried to just plug in, we'd get [ugly thing]. So that doesn't work."
  [Acknowledges a tempting wrong move and rules it out.]

  "Instead, let's try [reframe]."
  [The actual technique.]

  [Step-by-step computation, with brief verbal commentary
   between each algebraic step explaining WHY the step.]

  "And so we get [answer]."

  "Notice that we used [rule from earlier] in step 3 and [other rule]
   in step 5. Try writing this out yourself before continuing."

  "Here's another example, slightly harder..."
```

Note the interleaving: every block of math is sandwiched between two pieces of prose explaining what that block means. There is *no* equation that stands alone.

### 3.4 Figure & Equation Conventions

- Figures are numbered (图 N-K) and almost always inline, not in a "List of Figures".
- Figures depict the *current* worked example, not a generic abstract concept.
- Equations rarely get their own equation numbers — they live inline with the prose.
- The few that *are* numbered are the ones the book will reference repeatedly (FTC, Taylor series).
- No labeled "Theorem", "Lemma", "Corollary" hierarchy. Just bold text saying "the rule is" or "the statement is" inside the prose.

This deliberate lightness of formal apparatus reduces the cognitive cost of reading. The trade-off: harder to look up later. Banner solves the lookup problem with a thorough index and the master review tables (Part 6).

### 3.5 The "Tip-of-Tongue" Cross-Reference Pattern

Banner cross-references *constantly*, both backward and forward. The pattern:

- Backward: "as we saw in Section 6.2.5" — never just "as we saw earlier".
- Forward: "we'll see why in Chapter 14" — never just "later".

This builds the reader's *map* of the book. By Chapter 22 they know where Chapter 6 is and what was there.

### 3.6 The Two-Column Move

For long worked computations, Banner often uses a two-column layout:
- Left: the algebraic step.
- Right: a one-line verbal explanation of what changed and why.

This is the closest the book gets to a "lecture transcript" feel.

---

## Part 4 — The Author's "Thinking" Stance (Epistemology)

What Banner believes about mathematics and learning, distilled from how he teaches.

### 4.1 Understanding ≠ being able to follow a proof

A student who can recite the ε-δ definition has not necessarily understood limits. A student who can correctly classify a problem and pick the right technique *has* understood. Banner therefore builds *recognition* skill before *justification* skill.

### 4.2 Mechanical fluency is a precondition for insight, not its enemy

Banner is not anti-procedure. He believes you should drill the chain rule until it's reflexive, *because* freedom from arithmetic frees attention for higher-order pattern matching. The book contains many "do this 50 times" recipes, not as drudgery but as the hands learning a craft.

### 4.3 Visualization is primary

Almost every concept gets a graph before a formula. The unit circle for trig. Slope of a tangent line for derivative. Area under a curve for integral. The reason: students will retrieve the picture under exam stress when they can't retrieve the formula. The picture lets them re-derive the formula.

### 4.4 Names matter

Banner gives names to almost everything: "reference angle", "Type A/B/C limit", "the squeeze theorem", "the dummy variable". A named thing can be referenced; an un-named thing has to be re-derived every time. He even names *his own pedagogical moves* ("the internal monologue", "the small game" for ε-δ).

### 4.5 The textbook is a friend, not an oracle

A textbook should *answer the questions the student is actually asking*, not the questions the syllabus committee asked. Banner therefore writes from the student side of the desk. When he has to introduce notation, he asks "is this the most ergonomic notation? if not, why is the standard one this way? OK, here's the standard, sorry."

### 4.6 Calculus is one connected story

Banner believes the typical calculus course is fragmented (limits, then derivatives, then integrals, with no through-line). His book emphasizes *connections*:
- Linear approximation appears in differentials, in L'Hôpital, in Newton's method, in Taylor series.
- The fundamental theorem of calculus is not "section 17.2", it is the connective tissue between everything before and after.
- Improper integrals are introduced *as* limits of integrals — same idea, new domain.

### 4.7 Rigorous and intuitive are not enemies

The rigorous treatment exists, in Appendix A. Banner believes the right pedagogy is to teach intuition first, get the student fluent, then offer rigor as *deepening* — not as gatekeeping. He never sneers at the intuitive treatment as "hand-waving"; he simply marks where the proof lives for the reader who wants it.

---

## Part 5 — The Voice (Style Guide)

If you imitate only one thing, imitate the voice. Specifications:

### 5.1 Tone

- Conversational, not lecturing. Imagine a friend tutoring you in a coffee shop.
- Warm but not saccharine. Banner doesn't use exclamation marks for everything — he saves them for genuine surprises ("And that, amazingly, is the answer!").
- Mildly self-deprecating. "I'll admit, this notation is awful."
- Light humor, never forced. Cylindrical-can optimization problems get one-line setups about a cat named Junkster (Chapter 1).

### 5.2 Sentence-level rules

- Short sentences. Average 12–18 words.
- One idea per sentence.
- Active voice unless passive is technically necessary.
- Contractions allowed: "we'll", "you'd", "isn't".
- Direct address: "you" not "one" not "the reader".
- First-person plural for joint exploration: "let's try", "we get".
- First-person singular when the author has a personal opinion: "I think", "I prefer".

### 5.3 Paragraph-level rules

- A paragraph either makes one observation or works through one step.
- Paragraph breaks are frequent — averaging 3–5 sentences each.
- Math display equations break paragraphs; the next paragraph picks up the thread immediately.

### 5.4 The forbidden register

These are *banned*:

- "It is well known that..." → just say it.
- "It can be shown that..." → either show it, or say "we won't prove this here, but see Appendix X".
- "The reader will easily verify..." → if it's easy, do it; if it isn't, don't pretend.
- "Trivial" → never used.
- "Obviously" → never used unless the next clause explains why.
- "Clearly" → as above.
- Roman-numbered theorems with decorative formatting.
- Vacuous transitional phrases: "We now turn to...", "It is worth noting that...".

### 5.5 The unique Banner moves

Specific stylistic fingerprints worth borrowing wholesale:

- Italic *interjections* in the middle of a derivation: *(why? because the denominator is now zero)*.
- Footnotes not for references, but for asides: "*by the way, this same trick works for...*".
- Margin-style call-outs as separate short paragraphs: "Notice the ε here is the same ε from before."
- Worked examples named with characters when convenient ("a dog named Junkster"; an insurance broker; a cat).
- Self-referential bridges: "If you got the previous example, this next one is just the same idea with one extra step."

---

## Part 6 — The Apparatus (Navigation, Front-matter, Back-matter)

The "book object" outside the prose. Banner's design choices here are as deliberate as his prose.

### 6.1 The front matter (≤ 10 pages)

In order:

1. **Translator's foreword (in translations only).** Skipped in the original; describes target audience.
2. **Author's preface.** Five questions, answered:
   - Who should read this book?
   - What do you need to know first? (Reading the first two chapters is enough.)
   - "I have an exam next week, where do I start?"
   - Where are the worked problems? (They are *embedded*.)
   - Where are the proofs? (Appendix A.)
   - Subject not in the table of contents? (Use the index.)
3. **"How to use this book."** Visual conventions explained:
   - This icon = problem-solving process.
   - This icon = pay extra attention.
   - This icon = try yourself first.
   - Optional sections marked.
4. **Two study tips:**
   - Write out the formulas yourself for memorization.
   - Simulate exam conditions with practice problems.
5. **Acknowledgments.**
6. **Topic-to-section reverse table.** Two columns: "topic" and "where to find it (section number)". Grouped by exam unit (limits, derivatives, integration, sequences/series, etc.). This is the cramming reader's map.

### 6.2 The body

30 chapters. Three roughly equal arcs:

- **Arc 1: Prerequisites + limits + derivatives** (Chapters 1–10, ≈ 200 pages)
- **Arc 2: Applications of derivatives + integrals** (Chapters 11–21, ≈ 200 pages)
- **Arc 3: Series + advanced topics** (Chapters 22–30, ≈ 200 pages)

### 6.3 Appendix A: Rigorous proofs

Roughly 40 pages. All ε-δ work, sandwich theorem proof, MVT proof, FTC proof, etc. Mirror-organized to the chapter structure: A.1 covers the limit proofs that go with Chapter 3; A.6 covers integration proofs that go with Chapter 17. The student can reach for the proof exactly when they need it.

### 6.4 Appendix B: Estimating integrals

Numerical methods (trapezoid, Simpson's). Separated because not all instructors cover it.

### 6.5 Index

Detailed, behavior-oriented. Entries like "limit, of rational function as x → ∞" not just "limit". Lookup-friendly.

### 6.6 No glossary, no formula sheet

Deliberately. The author wants you to *make your own*. The reverse table at the front is the closest thing to a formula sheet, and it points you to where each formula is *derived*.

---

## Part 7 — The Macro Curriculum Choices

What Banner included, what he left out, and why each decision matters.

### 7.1 What he included

- Generous prerequisite chapters (Chapters 1–2). Functions, lines, trig. Calculus textbooks usually punt these to "appendix" or assume them. Banner makes them chapters because he believes most calculus failure is precalculus failure in disguise.
- One full chapter on each major integration technique (substitution, by-parts, partial fractions, trig substitution).
- Two full chapters on series convergence, divided into "concepts" and "how to solve". The split is unique to him.
- A separate chapter on Taylor & power series problem-solving (Chapter 26). Most textbooks fold this into the series chapter and the student drowns.
- A chapter on complex numbers (Chapter 28). Unusual for a calculus book; included because Euler's formula clarifies trig identities.
- A chapter on differential equations (Chapter 30). Unusual for single-variable; included as a teaser of where calculus goes next.

### 7.2 What he left out

- Multivariable calculus. (One book at a time.)
- Linear algebra.
- Most numerical methods.
- Hundreds of practice problems. (Outsourced to a separate problem book.)
- Real analysis. (Out of scope; appendix sketches what would be needed.)

### 7.3 Ordering choices

- L'Hôpital's rule in Chapter 14 (after derivatives are mastered, not earlier). Many books introduce it with limits and the student doesn't understand why it works. Banner waits.
- Inverse trig in Chapter 10 (after exponentials in Chapter 9). The pattern "exp/log are inverse pairs, also sin/arcsin are inverse pairs" then becomes one idea.
- Improper integrals introduced *before* series (Chapters 20–21 before 22+) so the comparison test for series can build on the comparison test for integrals.

---

## Part 8 — A Recipe for Writing a Book in This Mold

If you want to write the *Calculus Lifesaver* of [your subject], here is the protocol.

### 8.1 Before writing — the design phase

1. **Identify the subject's standard problem types.** Make a complete enumeration. If the subject is large, slice off a coherent piece (e.g., "differential calculus" not "all of mathematics"). The book will succeed if and only if every standard problem the reader will face has a named recipe inside.

2. **Identify the prerequisites.** Don't assume them — write them. The reader who is nervous about logarithms will not magically be calm about derivatives of logarithms. Spend 10–15% of the book on prerequisite review.

3. **Build the topic graph.** What depends on what? Order chapters by topological sort of dependencies, *and* by escalating cognitive difficulty.

4. **Decide what is rigorous-in-text vs. proof-in-appendix.** Default: rigorous arguments go in appendix unless they are short, illuminating, and the reader needs them to use the next tool.

5. **Decide what is in vs. out of scope.** Write the negative-space paragraph in the preface first.

6. **Sketch the topic-to-section reverse table.** Yes, before writing any prose. This forces you to know exactly which problem the reader can solve after each section.

### 8.2 While writing — the per-section protocol

For every section, in order:

1. Open with one motivating sentence connecting to last section.
2. Pose a concrete problem with a specific number, not a symbolic one.
3. Try the obvious naive approach and let it fail.
4. Voice the question: *what would have to be different for this to work?*
5. Introduce the new technique as the answer.
6. Apply to original problem. Get the answer.
7. State the rule in a small bold block.
8. Apply to a second example with a wrinkle.
9. (Optional) third example with the easy case.
10. (Optional) common mistake call-out: "Don't confuse this with..."
11. Cross-reference where rigor lives.
12. One transition sentence to the next section.

### 8.3 While writing — the per-chapter protocol

1. Opening: motivating paragraph + bullet list of what's covered.
2. Sections in order, escalating in difficulty.
3. Final section: explicit "how to recognize which case" flowchart or table.
4. No closing summary. Trust the reader to write their own.
5. Forward-pointer to the next chapter inside the last paragraph.

### 8.4 Voice checklist (use as a self-edit pass)

- [ ] Every paragraph passes the "would I say this out loud to a confused friend?" test.
- [ ] No "obviously", "clearly", "trivially".
- [ ] No equation stands alone; each is sandwiched between explanatory prose.
- [ ] At least one "you might think... but actually..." per section.
- [ ] At least one cross-reference to a previous section per chapter.
- [ ] At least one forward-reference per chapter.
- [ ] All worked examples follow the script in Part 3.3.

### 8.5 Apparatus checklist

- [ ] Preface answers the five reader questions (Part 6.1).
- [ ] "How to use this book" section with study tips.
- [ ] Reverse table: topic → section.
- [ ] Index is behavior-oriented ("derivative, of trig functions").
- [ ] Appendix for rigorous proofs, mirror-organized to chapters.
- [ ] Companion website mentioned for errata and supplementary material.

### 8.6 What the book *cannot* be

- It cannot be a reference manual. The whole point is the conversational scaffolding.
- It cannot be a problem book. Practice belongs in a separate volume.
- It cannot be a research monograph. The voice would be wrong.
- It cannot be encyclopedic. Banner cuts ruthlessly to the standard curriculum.

---

## Part 9 — Diagnostic Questions for Drafts

While writing your own version, audit each section against these:

1. If a tired student opened to this section at 11pm before an exam, would they get one usable thing in five minutes?
2. Is there a numerical or visual example before the first symbolic statement?
3. Does the section name the technique? Could the reader say "I used technique X" afterward?
4. Have I anticipated the wrong intuition the reader will bring?
5. Have I told the reader where to find the rigorous version?
6. Have I told the reader what comes next and why?
7. Did I use the word "obviously"? (If yes — delete.)
8. Did I write a worked example without prose between the equations? (If yes — add prose.)
9. Could the reader, having just finished this section, recognize this problem type on an exam?
10. Could they execute the recipe from memory after one re-read?

If all ten are *yes*, the section is in the Banner mold.

---

## Part 10 — The Spirit (One More Time)

Banner believes:

- Mathematics is hard, and pretending otherwise insults the reader.
- The hardest part is learning to *think*, not learning to *compute*.
- Thinking is teachable if you externalize it as conversation.
- Visual + numerical + algebraic + (optional) rigorous, in that order.
- Every standard problem should have a named recipe and a worked example.
- The textbook should leave the student feeling capable, not subordinate.
- Practice is essential, but practice is not the textbook's job.
- Names, cross-references, and recipes are the bones of usable knowledge.
- A real human voice, with humor and humility, beats the formal register every time.

If you write a book that embodies these nine commitments, in the structure of Parts 3 + 6, with the voice of Part 5, executing the per-section protocol of Part 8.2, and using the diagnostic of Part 9 — the result will not be a copy of *The Calculus Lifesaver*. It will be the *X Lifesaver*, where X is your subject. That is the goal.

---

## Appendix: A Concrete Section Template You Can Type Into

```
N.M  [Section Title]

[1 sentence connecting to the previous section.]

For example, [concrete problem with a specific number].

[1–2 sentences walking up to the obvious approach.]

If we tried [naive move], we'd get [bad outcome]. So that doesn't work directly.

Here's the trick. [State the reframing in plain language.]

[Carry out the reframing on the example. Use display equations, with one-sentence
prose between each line that says what just happened.]

So the answer is [result].

In general, the rule is:

    [Boxed or italic statement of the rule.]

Let's try this on a slightly harder example. [Second example with new wrinkle.]

[Worked solution, again with prose between equations.]

A common mistake here is to [wrong move]. The fix is [right move], because [reason].

For the rigorous proof of this rule, see Section A.[X] of the appendix.

In the next section, we'll see how this connects to [next topic].
```

Use this template *literally* for the first 10 sections you write. After 10 sections, the rhythm is internal and you can vary.

---

*End of distillation.*
