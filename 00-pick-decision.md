# Decision: which challenge to answer

**Pick: Challenge #3 — Design for Illiterate Workers**

Deadline: 31 Aug 2026, 09:00 IST. Deliverable: 5-minute video, format open.

---

## 1. What is actually being evaluated

Forward Deployed Engineer at Hunar.AI means embedding with a customer (factory,
warehouse, retail chain, logistics fleet), understanding their hiring and
workforce workflow, configuring multilingual voice AI agents to it, and handling
everything that breaks on contact with reality.

Company context that drove the pick:

- Multilingual conversational **voice** AI agents for India's frontline /
  blue-collar workforce. Surface spans hiring, screening, onboarding, training,
  engagement, retention.
- Founded 2022 by Krishna Khandelwal and Shantanu Bhattacharyya.
- They ran an actual recruitment agency for roughly two years *before* building
  product, specifically to learn how these conversations happen on the ground.

Sources (content rephrased for licensing compliance):
- https://inc42.com/startups/why-hunar-ai-thinks-indias-frontline-workforce-needs-ai-agents/
- https://hunar.ai/
- https://pitchbook.com/profiles/company/519656-95

**Implication:** this is a company whose origin story is fieldwork. They do not
need convincing that voice matters. The question is not "which prompt is most
interesting" but "which prompt best demonstrates fieldwork instinct."

---

## 2. Steelman of each option

### #1 AI as the Driver's Manager
For: the only prompt where the AI holds *authority* over a human — assign,
evaluate, correct, escalate, reward, discipline. That is the real frontier of
"AI HR", which is Hunar's literal positioning. Explicitly names "human
behaviour" as a lens, inviting behavioural insight. Scenario is fully specified
and universally legible, so zero of the 300 seconds go to establishing context.
Against: open canvas, no structure. "Redesign everything for 50,000 drivers in
5 minutes" pushes toward superficiality or overrun. Most submissions will land
on a voice assistant bolted onto the existing app.

### #2 Kill the App
For: strongest forcing function in the set. Removing smartphones eliminates every
lazy answer and forces IVR, missed-call, feature phones, NFC cards, biometric
terminals, kiosks, supervisor-mediated flows. Genuinely FDE-flavoured — that is
how you deploy on a plant floor where phones are banned.
Against: sci-fi premise, so it drifts toward thought experiment rather than a
product someone buys. Largely a subset of a good #3 answer with less scaffolding.

### #3 Design for Illiterate Workers
For: five named sub-questions = a rubric. Two of them (how salary is explained,
how AI builds trust) are the highest-emotion, highest-attrition moments in
frontline work and will likely be treated as afterthoughts by most submissions.
Contains a structural insight most will miss: 40% cannot comfortably read
*English* vs 20% who struggle with *any* language — two different populations,
two different solutions, and the hard one is the 20%.
Against: the prompt where the evaluator knows vastly more than the candidate.
Shallow claims get spotted instantly. Empathy theatre is the default failure.

### #4 If ChatGPT Was Never Invented
For: quietly the most intellectually interesting and probably least picked of
1–4. Attacks something true and unfashionable — chat is a poor interface for most
work and terrible for frontline workers. Elegantly aligned with Hunar, whose
product *calls you*; there is no chat window in it.
Against: dominated. "Chat is the wrong interface" is one sentence; the remaining
4.5 minutes still need a concrete product, domain and structure, at which point
you have answered #1 or #3 with extra setup cost. Highest variance.

### #5 Mahindra BE 6 Batman Edition
For: almost nobody will pick it. Only prompt that fits 5 minutes comfortably.
Clean top-down/bottom-up triangulation with stated assumptions and a sensitivity
band is very legible competence. Estimation is real FDE work (pilot sizing, call
volume forecasting, ROI cases).
Against: the set is called a Product Thinking Challenge and this is not product
thinking. Off-axis for a role about designing and deploying workforce products.
Can read as routing around the four harder, role-relevant prompts.

---

## 3. Arguments discarded from the first draft

Recorded so they don't get reused.

- **"#3 has the most overlap with Hunar's product surface."** Overstated.
  Onboarding, training and trust are squarely theirs; attendance and payroll are
  usually HRMS territory (Keka / Darwinbox / customer's own system). So #3 is
  roughly 60% on-surface — and #1 is about the same, since dispatch and routing
  aren't Hunar's either. Relevance does not separate them.
- **"#3 has lower competition."** A guess, not a fact. No visibility into what
  candidates pick, and there is a real counter: #3 is the most scaffolded prompt,
  which makes it the *safe* pick, which could make it crowded too.

---

## 4. The actual tiebreaker

**#1 rewards imagination. #3 rewards homework.**

#1 explicitly says "imagine AI has become good enough" and "forget how delivery
apps work today." That grants license to speculate, so a vivid imagination can
carry a thin answer.

#3 grants no such license. It hands you a population and dares you to know
something real about them:

- what a wage-slip dispute actually sounds like
- which deductions workers do not understand, and why
- how often a handset is shared, borrowed, or registered to someone else
- why face/biometric attendance fails at 6am shift change
- why a synthetic voice earns less trust than a supervisor's recorded one
- why "vernacular" is not the same as the language written on their form

Those are findable in two days. Most candidates will not bother. A company
founded on two years of exactly that fieldwork will spot the difference
immediately.

**So: #3, because the deliverable itself becomes a demonstration of the job.**
The risk (they know more than you) is precisely what converts into the
differentiator, if the work actually gets done.

---

## 5. Decision rule for switching to #1

Switch if either is true:

1. There is a specific non-obvious insight about algorithmic authority over gig
   workers that is unlikely to appear in other submissions.
2. Imposing your own structure on an open prompt is preferable to working inside
   someone else's five questions.

#1's ceiling is slightly higher. Its floor is a lot lower.

---

## 6. Guardrails for the #3 answer

- every principle must be followed by a concrete mechanism
- separate the 80% (low English literacy — solvable with vernacular) from the
  20% (non-literate — the actual design problem)
- name failure modes out loud: voice AI mishears dialects, shared phones break
  identity, face auth fails on worn hands and poor light
- state how success is measured, not just what is built
- no screens-first thinking; no assumption of one smartphone per worker
- ground every claim in something real, not something plausible
