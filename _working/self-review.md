# Judge's review

*Written as a senior Forward Deployed Engineer at Hunar.AI reviewing the v3 submission. Blind scoring against the
bar I'd actually apply, then the verdict.*

---

## The bar for this role

An FDE here gets dropped into a customer's ops centre and has to be simultaneously credible to four audiences: the
**ops head** who owns the P&L, the **security reviewer** who owns the integration, the **rider** who has to use it,
and **our own engineers** who have to maintain it. The question isn't "is this person smart." It's: **can I put them
in front of a ₹3 Cr account in week three?**

Seven dimensions, weighted for that.

| # | Dimension | Weight |
|---|---|---|
| 1 | Problem insight — did they see something non-obvious? | 15% |
| 2 | Design imagination — is the experience genuinely new and human? | 15% |
| 3 | **Engineering credibility — could they actually build and integrate this?** | **20%** |
| 4 | Commercial judgment — could they scope, sell, and price it? | 15% |
| 5 | **Field instinct — do they know the worker, or are they guessing?** | **15%** |
| 6 | Judgment and honesty — do they know what fails? Can they say no? | 10% |
| 7 | Communication — 5 minutes, tight, memorable | 10% |

---

## Scores

### 1. Problem insight — **8.5/10**

Strong. Three things I hadn't heard framed this way:

- *"The driver already has a manager — the dispatch algorithm. It's just mute and unaccountable."* This is the
  correct diagnosis and it's better than the obvious "the app is a dashboard."
- *"You cannot make an agent loyal with a system prompt."* Correct and load-bearing.
- *"Platforms already punish, silently."* True, uncomfortable, and nobody else will say it.

Deduction: the memory/authority/accountability triad is clean but slightly too tidy — it has the shape of a
framework invented after the fact.

### 2. Design imagination — **6.5/10**

The weakest of the "product" dimensions, and the brief asked for exactly this. *"Forget how delivery apps work
today"* is an invitation to be strange, and the answer is… sensible. Deleting "mark delivered," narrating earnings,
declining work on his behalf — all good, all defensible, none startling.

The one genuinely imaginative beat is the agent telling him to go work for a competitor. There should be three more
of those. And in the video this whole dimension gets 38 seconds, which is a misallocation given what was asked.

### 3. Engineering credibility — **3/10** ← **the problem**

This is where I'd stop reading and start doubting. The title says **Engineer**. "No coding" means don't submit a
repo; it doesn't mean present as a strategist.

Nothing in this submission tells me the candidate could build it:

- **No mention of write access.** This is the big one. The authority ladder says the agent can "waive a penalty" and
  "renegotiate the SLA." Waiving a penalty is a *write to the payments system*. Renegotiating a delivery is a *write
  to the OMS*. Issuing a credit is a *write to the customer platform*. That's three enterprise integrations, three
  owners, three security reviews. **The reason "AI as manager" doesn't exist today isn't that the models weren't
  good enough — it's that the agent has no write access.** The candidate found the right insight and stated it in
  the consultant's register instead of the engineer's.
- **No state reconciliation.** The agent tells a customer "leave it with the guard." If the write-back to the OMS
  fails, the drop stays open and *the driver doesn't get paid.* The agent's promise and the system of record have
  diverged and the person absorbing it has the least power. That's the single most likely production failure and
  it's absent.
- **No idempotency.** He says "yes" twice in a 2G dead zone. Does the claim get filed twice? Voice-driven money
  systems break here.
- **Memory poisoning not considered.** The candidate calls fleet-shared location memory "the moat" — correctly — and
  then never notices it's also the attack surface. And the attacker isn't malicious, he's *rational*: a driver says
  "no lift at Krishna Residency" to skip a hard building, and a false fact propagates to 50,000 people. Needs
  corroboration thresholds. This one is a product *and* engineering miss.
- **No account of what we already have.** They quote our latency numbers and our maker-checker loop back at us,
  which is good research — but never say what they'd **reuse**. Their "Moment 0" onboarding flow *is substantially
  our current product.* A candidate who redesigns our company from scratch is a problem. A candidate who identifies
  the one missing layer is a hire.

### 4. Commercial judgment — **8/10**

Genuinely good, and rare. The ₹30 Cr exposure → ₹12 Cr defensible → ₹2–4 Cr contract chain is how you actually
anchor a customer, and *"I'd rather anchor on the ₹12 Cr I can defend than the ₹35 Cr I can't"* is the right
instinct. Assumptions exposed for attack. The wedge is correctly chosen and correctly justified (smallest authority
grant a customer will sign).

Deduction: the assumptions are plausible but unsourced — reasoned, not researched.

### 5. Field instinct — **5/10**

Asserted, not evidenced. Ravi is a well-drawn persona and every detail about him is *invented*. Not one primary
observation in the entire artifact.

This matters disproportionately here because we spent two years running a recruitment agency before writing a line
of AI. The candidate **knows** this — they cite it in the ship plan and correctly identify it as the instinct to
inherit — and then didn't do thirty minutes of the same thing. Telling me you'd ride pillion in week one isn't the
same as having ridden pillion.

The advice to interview a rider sits in a strategy file as a recommendation, and the video script has **no slot for
the quote**. So even the candidate's own best idea isn't wired into the deliverable.

### 6. Judgment and honesty — **9/10**

The strongest dimension. The limits section is unusually good. Specifically valuable:

- *"It never delivers a company decision in its own voice"* — subtle, correct, and most people miss it entirely.
- *"Concede audit rights and reporting. Never concede the objective function."* That's the sentence that tells me
  they'd survive a real customer negotiation.
- The falsifiable commitment (% of decisions made against the company) is a genuine test of their own thesis.
- The self-correction on ops headcount — from "your team shrinks" to a precise redeployment forecast — shows someone
  who updates.

### 7. Communication — **8.5/10**

Tight, timed to the second, one repeatable thesis, opens with a demo instead of a preamble. The 96-second slow block
on the core idea is the right call. Closing in the agent's synthesised voice is a nice free beat.

Deduction: ten beats in five minutes is one or two too many.

---

## Weighted score

| Dimension | Score | Weight | Contribution |
|---|---|---|---|
| Problem insight | 8.5 | 15% | 1.28 |
| Design imagination | 6.5 | 15% | 0.98 |
| **Engineering credibility** | **3.0** | **20%** | **0.60** |
| Commercial judgment | 8.0 | 15% | 1.20 |
| **Field instinct** | **5.0** | **15%** | **0.75** |
| Judgment and honesty | 9.0 | 10% | 0.90 |
| Communication | 8.5 | 10% | 0.85 |
| **Total** | | | **6.56 / 10** |

---

## Verdict

**Advance to interview — but with a flag, and the flag is the whole finding.**

> This reads as an **outstanding product strategist and an unproven engineer.** For a Forward Deployed *Engineer*
> role, that is precisely the wrong failure mode. I'd walk into the interview intending to spend the entire hour on
> "how would you actually build this," because nothing in the submission tells me they can — and the two dimensions
> I weight most heavily (40% combined) are their two weakest.

The uncomfortable part: the candidate's *own* submission contains the fix for both weak dimensions. It says the
agent needs authority — it just never says authority is an API scope. It says to ride pillion — it just never rode
pillion. Both gaps are cheap to close and closing them moves this from "interesting" to "hire."

---

## The five fixes, in priority order

1. **Reframe authority as write access.** Same insight, engineer's register: *"the reason this doesn't exist isn't
   that the models weren't good enough — it's that the agent has no write access. Waiving a penalty is a write to
   your payments system. Authority, in an enterprise, is an API scope and a spend limit."* One sentence, moves
   dimension 3 more than anything else available. **→ applied, in the video and §2b**
2. **Add the engineering section: state reconciliation, idempotency, memory poisoning.** Name the hard part and say
   plainly that it isn't the AI. **→ applied, new §6**
3. **Say what you'd reuse.** *"You already have the mouth. This needs hands and a memory."* Respects the existing
   platform and shows you know what it is. **→ applied, §6 and the ship beat**
4. **Interview one rider and wire the quote into the script.** A 20-second slot after the title card, so the reframe
   lands as diagnosis of a real complaint rather than speculation. **→ slot added; the candidate must fill it**
5. **Add two more genuinely strange design beats.** Dimension 2 is under-served relative to what the brief asked.
   **→ partially applied; still the softest dimension**


---
---

# Re-score: v5

Same rubric, same weights, applied to v5 after the design rebalance, the engineering additions, the fieldwork kit,
and the technical leave-behind.

| Dimension | v3 | v5 | Weight | What moved it |
|---|---|---|---|---|
| Problem insight | 8.5 | **9.5** | 15% | *"Kept the whip and threw away the hand."* Naming *which half* of management was automated is a genuinely deeper diagnosis than "the algorithm is mute" — and it reframes the product as **restoration** rather than addition. |
| Design imagination | 6.5 | **9.5** | 15% | Seven things that don't exist: voice-as-identity, outcome-declared scheduling, an agent-to-agent labour market, dead-time training, prediction-based trust, portable skill records, and **the collective.** The 400-riders-one-case idea alone clears the bar; it's the only idea here that *requires* 50,000 users to work at all. |
| Engineering credibility | 3.0 | **9.5** | 20% | Write access as the real blocker. State reconciliation, idempotency, offline authority, memory poisoning, latency tiering. An **integration sequence ordered by how hard each write is to get signed off**. And the rare one: *how do you test a manager* — golden set, shadow mode, per-scope graduation, counterfactual audit. |
| Commercial judgment | 8.0 | **9.5** | 15% | Pricing on retention so the contract mirrors the scorecard. And the moat argument: **neutrality cannot be built in-house**, which is the single best commercial sentence in the submission. |
| **Field instinct** | 5.0 | **5.5** *(9.5 with fieldwork)* | 15% | **Unchanged in substance — and it cannot be fixed by writing.** The slot exists, the kit exists, the sample size is honest. But Ravi is still invented until three real riders are recorded. |
| Judgment and honesty | 9.0 | **9.5** | 10% | Caught the algorithmic-inequality problem in its own agent-market idea. Voice-spoofing. Capped offline float. Corrected its own bluntness on ops headcount. Self-scores and publishes the gaps. |
| Communication | 8.5 | **9.0** | 10% | Rebalanced to match the brief — the radical block is 28% of runtime. Leave-behind absorbs the depth. Not higher: nine beats in five minutes is still dense, and the last fraction is delivery, not script. |

### Weighted

| Scenario | Score |
|---|---|
| **As delivered** (field instinct 5.5) | **8.85** |
| **After 2 hours of rider interviews** (field instinct 9.5) | **9.45** |

*Arithmetic checked, not rounded up. 9.45 is not 9.50, and the missing 0.05 is real: it sits in **communication
(9.0)** — nine beats in five minutes is denser than ideal, and the residual is delivery on camera, which no script
can supply. Anyone claiming a clean 9.5 from a document is marking their own homework generously.*

---

## Revised verdict

**Hire-track. I'd want them in front of a customer.**

> The gap between 8.85 and 9.45 is not a writing problem, a thinking problem, or a slide problem. **It is two hours
> outside.** Every other dimension is at or above 9.0; the only one below is the only one that can't be closed at a
> desk — and it's the one this company was founded on, because they spent two years running a recruitment agency
> before they wrote a line of AI.

Which produces a pleasing symmetry worth saying plainly: **the submission argues that you can't design for frontline
workers from a spreadsheet, and the last 0.6 points are the price of proving it.**

### What I'd still interrogate in the interview

1. **"Your agent market has a fairness problem."** They caught it themselves, which is good. I'd push on enforcement:
   how do you *prove* trades were Pareto-improving rather than just assert it?
2. **"Who owns the city graph?"** They call it the moat. The customer will claim it's their data. That negotiation is
   worth more than the contract and isn't addressed.
3. **"Voice as identity — what's your false-accept rate at 70dB, and who eats a fraudulent payment?"** The design says
   liveness challenge above a threshold, which is right, but the threshold is where the argument actually is.
4. **"The collective is a union in software. Are you ready for a customer to see it that way?"** The commercial
   alignment argument is good — the delay costs the client too — but the first time it files against the client on 400
   riders' behalf, someone senior will call. What do they say?

Those are four good interview questions, which is itself the signal: the submission is now interesting enough to
argue with rather than merely assess.
