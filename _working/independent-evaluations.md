# Two independent evaluations

*Deliberately adversarial. `05-judges-review.md` was a self-review and it inflated — an independent read finds six
substantive gaps it missed. Both reviewers below are told to assume the previous score was generous.*

---
---

# PART 1 — Senior FDE review

**Score: 7.9/10.** (Self-review claimed 8.85. The delta is the point — see the end.)

## Where it's genuinely strong

Nothing to add to what the self-review said, and I agree with most of it. *"Kept the whip and threw away the hand"*
is a real reframe. *Authority is an API scope plus a spend limit* is the correct diagnosis of why this category ships
read-only. *Neutrality can't be built in-house* is the best commercial sentence in the pack. The collective is the
only idea here that requires 50,000 users to function, which is what makes it interesting rather than merely nice.

Now the six things it missed.

## Gap 1 — It never asks whether the driver wants a manager at all

**The most damaging gap, and it's in the foundation.**

The entire submission assumes the rider wants a relationship with an agent that remembers him, coaches him, notices
his mood and checks in. But a substantial part of *why people choose gig work* is to escape exactly that. "No boss"
is a feature, not a bug. It's frequently the single thing they'll name when asked why they left a factory or a retail
job.

So there's a real possibility this design is solving for a need the user actively rejects — and that a proactive,
remembering, coaching agent lands as nagging and surveillance no matter how well-aligned its scorecard is. The
submission has an elaborate answer for *"what if the company objects"* and no answer at all for *"what if he doesn't
want it."*

**The fix isn't hard, which makes the omission worse.** Manager intensity should be his dial, not ours. Quiet mode.
"Only talk to me about money." Zero interruptions until he asks. And the adoption metric already in the submission —
*% of shifts where he voluntarily speaks to the agent* — is the right instrument, it's just not connected to a design
response.

## Gap 2 — Voice-as-identity collides with account sharing

Account renting is endemic in Indian gig work: one verified account, several people riding it. It's unauthorised, it's
widespread, and for many riders it's economically load-bearing.

Voice-as-identity doesn't just authenticate — it **breaks that practice overnight.** That is either the compliance win
the customer will pay the most for, or the thing that triggers a rider revolt in week two. Possibly both, in that
order.

Either way it's one of the most consequential second-order effects in the whole design and it isn't mentioned once.
A senior FDE would have surfaced it in the first customer conversation.

## Gap 3 — The collective is a union, and the submission tells the employer it's a productivity tool

The submission claims *"nobody has to lose"* because the warehouse delay costs the client too. True for gate delays.
Not true for the trajectory.

An agent with shared memory across 50,000 workers, that files evidenced collective grievances, will inevitably be
pointed at **rates.** The first time it aggregates 5,000 riders on pay, the contract is at risk — and "we only do
operational friction" isn't a technical constraint, it's a promise the product architecture doesn't enforce.

This needs to be an explicit, permanent, *architected* scope boundary with the reasoning stated out loud to the
customer — not an optimistic aside. Right now it reads as either naive or quietly evasive, and neither is good.

## Gap 4 — Goodhart's law on the agent's own scorecard

The best idea in the submission is scoring the agent on driver outcomes. But score an agent on **earnings per hour**
and it learns to push riders toward over-work, or to quietly prefer the drivers who make its numbers look good.
Score it on **90-day retention** and it learns to be reassuring rather than honest.

The submission is sharp about the company gaming the objective function and blind to the *agent* gaming it. Needs
counter-metrics — hours worked per driver, fatigue incidents, distribution of attention across the cohort — and an
explicit statement that the scorecard is capped, not maximised.

## Gap 5 — No regulatory surface

India's gig-worker regulation is moving (social security code, state-level platform accountability). An agent that
documents grievances, timestamps unpaid waiting, and files claims **creates a discoverable evidence trail about
working conditions.**

The customer's counsel will raise this in the first security review and it will be the hardest objection in the
deployment — harder than the write access. It isn't mentioned. For a role that sits between the vendor and the
customer's legal team, that's a notable blind spot.

## Gap 6 — Scoping

They asked for a five-minute video. The response is nine files and roughly fifteen thousand words, including a
self-scored rubric that re-weights the employer's own hiring criteria.

The core skill of a Forward Deployed Engineer is delivering **the smallest thing that moves the customer.** This is
the opposite instinct. The content is good, and producing this much of it against a 5-minute brief is itself a
judgment signal — and not a flattering one.

## Revised scores

| Dimension | Self-review | Independent | Why |
|---|---|---|---|
| Problem insight | 9.5 | **9.0** | Gap 1 is a hole in the problem framing itself |
| Design imagination | 9.5 | **9.0** | Seven strong ideas; Gap 2 is a first-order miss |
| Engineering credibility | 9.5 | **8.0** | No data model, no regulatory surface, Goodhart unaddressed |
| Commercial judgment | 9.5 | **8.0** | Gap 3 is a contract-termination risk treated as an aside |
| Field instinct | 5.5 | **5.5** | Unchanged. Still invented. |
| Judgment and honesty | 9.5 | **8.5** | Six unexamined risks after claiming thoroughness |
| Communication | 9.0 | **7.5** | Gap 6 |
| **Weighted** | **8.85** | **7.90** | |

## Verdict

**Advance. Strong candidate, and I'd argue for them.** But the lesson in the delta is the useful part:

> **A self-review scored this 8.85. An adversarial review scores it 7.9.** The submission's own best instinct —
> publish the falsifiable metric, name what will fail — stopped one layer short of being applied to itself. Six
> substantive risks were available to anyone reading with intent to break it, and the author found none of them
> because by draft five they were arguing *for* the design rather than against it.

That's not a knock on the thinking. It's the most common failure mode in this job: you become the customer's advocate
so effectively that you stop being the design's adversary. Worth naming in the interview, because the candidate will
recognise it.

---
---

# PART 2 — Senior recruiter review, Hunar.AI

Different question entirely. I don't care whether the design is right. I care whether this person clears the loop,
what level they come in at, and whether I can sell them to the founders in a two-minute Slack message.

## Scorecard

| Criterion | Score | Note |
|---|---|---|
| **Instruction compliance** | **6/10** | Brief said one challenge, five-minute video. They picked one — good. Then produced a nine-file repo. Over-delivery reads as enthusiasm to some founders and as *can't scope* to others. |
| **Signal of thinking quality** | **9.5/10** | Top of the pipeline. The write-access reframe and the neutrality argument are things our own team says. |
| **Company-specific effort** | **10/10** | Named both founders. Cited the two-years-as-a-recruitment-agency origin story *and* mirrored it in their plan. Prototyped in our own playground. I see maybe one candidate a quarter do this. |
| **Authenticity risk** | **5/10** | ⚠️ **My main concern.** In 2026 this level of polish reads as heavily AI-assisted. Not disqualifying — everyone uses the tools — but it changes the interview. |
| **Culture fit** | **7/10** | Values line up. But our founders spent two years doing unglamorous fieldwork, and this candidate wrote eloquently about riding pillion without having ridden pillion. That distinction matters here more than at most companies. |
| **Communication** | **9/10** | Timed to the second, one repeatable thesis, opens with a demo instead of a preamble. |
| **Interview readiness** | **Unknown** | The single biggest variable. See below. |

## The over-polish problem — read this twice

The submission sets a bar the candidate then has to clear **live, without notes, on a video call.**

If they can defend the ROI model under pressure, argue the collective's scope boundary, and explain why they'd concede
audit rights but never the objective function — this becomes an exceptional hire and the polish is irrelevant.

If they hesitate on their own numbers, **the submission actively damages them**, because the gap between the artifact
and the person becomes the story of the interview. I have watched strong candidates fail exactly this way.

**Practical instruction:** the candidate should be able to reconstruct every number in the pack from memory, and
should be comfortable saying *"I don't know, here's how I'd find out."* That one sentence resolves the authenticity
concern in about four seconds.

## What I'd tell them to submit, and to withhold

**Submit:** the 5-minute video. Nothing else, unless asked.

**Link once, on the final frame:** the one-pager. A single-page technical leave-behind after a pitch is FDE behaviour
and it reads as restraint rather than volume.

**Withhold:** the self-scored rubric. Keep it as prep. Assigning weights to our hiring criteria and grading yourself
against them is a coin-flip — half our panel will read it as exceptional self-awareness and half as presumptuous. Not
a risk worth taking when the video already carries the argument.

**Withhold:** the full answer document and the critique log. Nobody is reading fifteen thousand words to fill one
role, and offering them invites the scoping criticism above.

## Level and pipeline

- **Pipeline percentile:** top 5% of submissions for this role.
- **Level:** the commercial instinct — ROI model, pricing aligned to the product thesis, pre-handled in-house
  objection — is above the FDE band. That's founding-solutions-lead territory. The engineering is credible but
  unevidenced.
- **Recommendation: fast-track to founder conversation, skip the screening round.** Hunar is small enough that
  founders review everything and this is the kind of submission a founder wants to argue with.
- **Flight risk:** moderate. Someone this commercially fluent has options in AI-native sales engineering at higher
  comp. **Sell the mission and the frontier, not the package.** The neutrality argument in their own submission is
  the hook — they clearly find the worker-side problem genuinely interesting, and that's rarer than talent.

## Interview brief I'd send the panel

1. **Probe depth, not breadth.** Pick two numbers from their ROI model and make them rebuild them live.
2. **Ask what they got wrong.** They self-critiqued four times on paper — see if they can do it conversationally, and
   whether they name the gap about *whether drivers even want a manager.*
3. **Ask if they spoke to a rider.** If yes, the loop gets much shorter. If no, ask why not — the answer tells you
   everything about whether they'll actually get on the bike in week one.
4. **One adversarial question:** *"The collective is a union in software. What happens the first time it files against
   our client on rates?"* Watch whether they defend the design or update it.

## Verdict

**Advance — fast-track. Contingent on the live conversation matching the artifact.**

> Best-written submission I've seen for this role. The only question I actually have is whether the person is as good
> as the document, and there's exactly one thing that would settle it in advance: **evidence they went outside and
> talked to a rider.** With that, I'd push hard for an offer. Without it, this is an excellent document by someone who
> has still only thought about the problem.

---
---

# Where the two reviewers disagree

The interesting output isn't either score. It's that they want opposite things:

| | Senior FDE | Recruiter |
|---|---|---|
| Volume | Wants **more** — data model, regulatory analysis, the six gaps closed | Wants **less** — video only, one linked page |
| The self-scored rubric | Useful; shows the candidate reasons about their own weaknesses | Withhold; coin-flip on how it lands |
| The polish | Neutral — judge the content | **A risk** — it sets a bar you must clear live |
| What decides it | Whether the design survives contact with a customer | Whether the person survives contact with the panel |

**The resolution, and the actual advice:** *submit small, prepare deep.* The recruiter governs what you send — video,
one linked page, nothing more. The FDE governs what you must be able to say when questioned, which is everything in
`01-the-answer.md` plus the six gaps above.

And both reviewers converge on one thing, which is the only instruction that matters:

> **Go and talk to a rider.** The FDE scores it 5.5/10 and it's the lowest number on the board. The recruiter says it's
> the single piece of evidence that would move them from *advance* to *push for an offer.* It costs two hours.


---
---

# ROUND 2 — re-evaluation after the six gaps were closed

*Both reviewers re-read the submission after the gap closures and the reorganisation. Instructed again to assume the
previous score was generous.*

---

# PART 1 — Senior FDE, round 2

**Score: 8.55/10 as delivered · 9.15 with fieldwork.** (Round 1: 7.90. Gap closure earned +0.65.)

## What genuinely improved

- **"Can he tell it to shut up?"** is the best single line in the pack now, and the boss/staff distinction it produces
  — *he's not getting a manager, he's getting a manager of his own* — makes the thesis stronger than it was before the
  objection was raised. That's the rare case where a patch improves the original.
- **The collective's boundary reasoning.** Pareto vs. distributive, and *scoping it narrowly is what protects it*. That
  reads like someone who has lost an enterprise deal before.
- **Honesty audit and appeal rate** as Goodhart counter-metrics. Specific, cheap, and genuinely unusual.
- **The deliberate "I don't know"** on city-graph ownership. Correct instinct, correctly placed.
- **Scoping fixed** by reorganisation rather than argument.

## Five new problems

### N1 — The design has quietly become a three-year platform while the plan claims one wedge

Seven radical things, a memory graph, an authority layer, an agent-to-agent market, a collective grievance engine,
dead-time training, portable credentials. §12 says *one wedge, 200 drivers* — correct — but the **video showcases the
ambition, not the discipline.**

That mismatch reads as a founder pitch rather than an FDE pitch, and it works against the exact gut-check the role
turns on: *can I put this person in front of a customer without them over-promising?* Right now I'm not sure. The
candidate has demonstrated they can imagine a platform; they haven't demonstrated they can resist selling it.

### N2 — None of the seven new ideas has a business case

§8 prices attrition, support and throughput — all consequences of the *original* design. Not one rupee of the ROI model
comes from voice-as-identity, the agent market, the collective, dead-time training or portable records.

So §3 is imagination without arithmetic and §8 is arithmetic without the imagination, and they never meet. The obvious
question — *which of the seven actually pays, and which are features you'd never get funded?* — has no answer. My guess
is dead-time training and voice-as-identity are fundable, the agent market is a research project, and the collective is
funded by risk reduction rather than revenue. But that's my guess, not their answer.

### N3 — Quiet mode partly breaks the two best ideas

The Gap 1 fix sets default intensity to minimal: money and exceptions only, everything else opt-in. Good answer to that
objection — and it quietly undermines §2a and §3.5, both of which depend on riders *talking* to the agent. The
collective needs 400 people to mention the warehouse. The city graph needs someone to say the gate is locked.

If most riders choose quiet mode, the moat doesn't accumulate. There's a clean resolution available — the city graph can
be built largely from **passive telemetry**, dwell times and geofence patterns, without conversation, and conversation
only enriches it — but the submission doesn't say so, and the tension is visible to anyone reading the two sections
together.

### N4 — The crib sheet trains defence, not updating

Ten questions, ten prepared answers, exactly one admitting ignorance. That's optimised for surviving an interrogation.
The job is not an interrogation.

The thing I most want to observe is a candidate being **moved** by a good argument, and this preparation actively works
against that. If they deliver ten polished rebuttals, I learn that they prepared; I learn nothing about how they think
when they're wrong. **There should be at least one question where the right answer is "you've changed my mind, and here's
what I'd change."**

### N5 — Still zero primary evidence, and the asymmetry is now the story

Unchanged from round 1, and *more* glaring precisely because everything around it improved. Every other dimension is
8.5–9.5. This one is 5.5.

The submission is now a monument to reasoning about people the author has never met. Blunt version: **I trust this
person's thinking and not their instincts, and instincts are what the job is.**

## Scores

| Dimension | R1 | R2 | Weight |
|---|---|---|---|
| Problem insight | 9.0 | **9.5** | 15% |
| Design imagination | 9.0 | **9.5** | 15% |
| Engineering credibility | 8.0 | **9.0** | 20% |
| Commercial judgment | 8.0 | **8.5** | 15% |
| Field instinct | 5.5 | **5.5** | 15% |
| Judgment and honesty | 8.5 | **9.0** | 10% |
| Communication | 7.5 | **9.0** | 10% |
| **Weighted** | **7.90** | **8.55** | |

*With fieldwork (field instinct → 9.5): **9.15**.*

## Verdict — and a recommendation to stop

**Strong hire-track. I'd advocate for them.**

But the important observation is about the trajectory, not the score:

| Draft | Independent score |
|---|---|
| v3 | 7.90 |
| v5 + gap closures | 8.55 |
| *projected v6, v7…* | *~8.7, ~8.8, asymptotic* |

**Each adversarial pass finds new gaps, and the returns are now clearly diminishing.** Round 1 found six real holes.
Round 2 found five, three of which (N1, N2, N3) are *tensions created by the previous round's fixes* rather than
original omissions. That's the signature of a document being polished past its useful point.

> **9.5 is probably not reachable by writing, and further drafts are now net-negative** — every pass adds words, and
> words have become the liability. The two things standing between 8.55 and ~9.2 are (a) two hours outside, and (b) the
> candidate's live delivery. Neither improves by editing.

**My advice to the candidate would be: stop. Go outside. Then record.**

---

# PART 2 — Senior recruiter, round 2

**Verdict: advance, fast-track to founder. Two flags now, where there was one.**

## What improved

| Criterion | R1 | R2 | Note |
|---|---|---|---|
| Instruction compliance | 6/10 | **8.5/10** | The `1-submit / 2-produce / 3-prep` split is exactly right. One video, one linked page. Fixed. |
| Thinking quality | 9.5 | **9.5** | Unchanged, top of pipeline |
| Company-specific effort | 10 | **10** | Founders by name, origin story mirrored, prototyped in our own playground |
| Communication | 9 | **9.5** | Timed, structured, one repeatable thesis |
| Culture fit | 7 | **7** | Unchanged, and it won't move until they get on a bike |

## Flag 1 — authenticity risk is now *worse*, not better

**4/10, down from 5.**

More polish means more suspicion, and the crib sheet makes it concrete: my specific fear is a candidate reading
prepared answers off a second screen. I have seen it, it is obvious within ninety seconds, and it is fatal.

The single thing that resolves it is already in their own prep — the deliberate *"that's the gap in my thinking"* on
city-graph ownership. **They should use it early, not hold it in reserve.** One unforced admission in the first five
minutes buys credibility for the remaining fifty.

## Flag 2 — velocity, which is new

Five drafts of a five-minute video. At an early-stage company I need people who ship at 80% and move on. A candidate
capable of iterating this many times on a take-home might be a perfectionist who can't let go — and that's a real
failure mode on a two-week customer deadline.

**Brief for the panel:** ask what they'd have cut if given half the time. If they can answer instantly and
unsentimentally, the concern evaporates. If they defend everything, it doesn't.

## Level, pipeline, and how I'd sell it internally

- **Top 3% of submissions for this role** (up from top 5%).
- **Level:** the commercial fluency is above the FDE band — founding-solutions-lead territory — but the FDE gut-check
  ("would I put them in front of a customer unsupervised in month two?") is now the open question, because of the
  reviewer's N1: the design has grown into a platform pitch.
- **Slack message I'd actually send the founders:** *"Take-home for the FDE role — worth ten minutes. Reframes the
  problem as 'the gig economy automated the disciplinary half of management and deleted the supportive half', and argues
  the blocker was never model quality, it's that the agent has no write access. Cited your recruitment-agency origin
  story and built the demo in our own playground. Two flags: heavily polished, and they haven't actually spoken to a
  rider. Worth an hour of your time."*
- **Flight risk: moderate.** Sell the frontier and the mission. Their own neutrality argument is the hook.

## The one thing that would change my recommendation

> If they open the video with fifteen seconds of a real rider's voice, I stop hedging and push for an offer.
>
> Without it, my honest read is: **an excellent document by someone who has still only thought about the problem** — and
> at a company whose founders spent two years running a recruitment agency before writing a line of AI, that specific
> gap is the one our panel is least likely to forgive.

---

# Round 2 synthesis

Both reviewers now agree on the same two-line conclusion, from opposite directions:

**The FDE says:** further writing is net-negative; the remaining points are fieldwork and live delivery.
**The recruiter says:** the polish is now a liability; the fix is one unforced admission and one real rider.

**Neither of them is asking for another draft.**
