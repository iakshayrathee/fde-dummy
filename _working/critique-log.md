# Critique log

Two rounds. **[Iteration 2](#iteration-2--critique-of-the-rewrite) is the one that matters** — it found a flaw in
the v2 thesis that the first round created.

---

# Iteration 1 — critique of the first draft

Six problems, roughly in order of severity.

---

### 1. I wrote a pitch to impress a founder without researching the founder

The worst of the six. I asserted the answer was "Hunar-aligned" on the basis of the company's name meaning
*skill* in Hindi. Actual research changes the advice substantially — see §2.

**Sources:** [Inc42 on Hunar](https://inc42.com/startups/why-hunar-ai-thinks-indias-frontline-workforce-needs-ai-agents/),
[hunar.ai](https://hunar.ai/), [ElevenLabs case study](https://elevenlabs.io/blog/hunar),
[CB Insights](https://www.cbinsights.com/company/hunar). *Content rephrased for compliance with licensing
restrictions.*

- Founded 2022 in Bengaluru by **Krishna Khandelwal** and **Shantanu Bhattacharyya**.
- The product is **conversational voice AI for frontline workforce management** — hiring, onboarding, training,
  retention. They call them "AI HRs." 10M+ candidate engagements claimed.
- Their published engineering focus is startlingly specific: interruption models trained on how human recruiters
  handle being cut off, a model that finds the right *resumption point* after an interruption, deliberately
  engineered 700–900ms latency, and a maker-checker second agent that reviews completed calls to hold extraction
  accuracy at 90–95%. Built for code-mixed, noisy phone calls.
- **They ran an actual recruitment agency for ~2 years before building any AI**, specifically to learn ground
  truth about frontline hiring and attrition.
- Sectors served include logistics and supply chain — so the "50,000 delivery partners" prompt is probably close
  to a live account.

### 2. My headline principle was their existing product

My draft led with "voice-first, not voice-added" as though it were an insight. To this company, voice-first is
**table stakes** — it's what they already sell. Worse, talking about voice *abstractly* to a team that publishes
about interruption-resumption points and 700ms latency budgets reads as naive.

The insight has to sit at a level they haven't already solved. It does now: **authority, not intelligence** (§3).

### 3. The ideas were good-generic, not memorable

Strip my draft down and it says: voice-first, vernacular, proactive, no screens, agent handles exceptions,
coaching, career ladder, guardrails on firing. Every strong candidate will submit approximately that. It is
competent and forgettable. Nothing in it was *arguable* — and a product thinking answer that nobody could
disagree with hasn't said anything.

### 4. Zero numbers

For a **Forward Deployed** engineering role — someone who sits in front of an enterprise customer — I produced
no business case. No attrition cost, no support cost, no ROI, no price anchor. This is the single easiest place
to separate from the field, and I skipped it entirely.

### 5. Three real design blind spots

- **Multi-apping.** I designed as though Ravi works only for this company. He doesn't. He runs three apps and
  allocates his day by ₹/hour. The agent isn't managing a workforce, it's *competing for share of shift*.
- **The agent becomes the face of every bad decision.** I treated it as universally welcome. In reality it's the
  only "person" a driver can shout at when earnings drop — and if it delivers company decisions in its own
  voice, the loyalty claim collapses within a week.
- **Their own accuracy number.** 90–95% is excellent for post-call data extraction in hiring. Applied to an agent
  that auto-closes deliveries and approves money, it means 5–10% of *financial* decisions are wrong across
  millions of events. That demands a design response, and I didn't have one.

### 6. Two pieces of bad advice

- **I offered to draft a second challenge.** The brief says choose one. Two decent answers is a worse signal than
  one excellent one — it reads as hedging.
- **I never told them to go talk to an actual delivery driver.** Given that Hunar's founders spent two years
  running a recruitment agency to get ground truth, this is the highest-leverage 30 minutes available and it
  mirrors the founders' own values exactly. It should have been my first recommendation, not an omission.


---
---

# Iteration 2 — critique of the rewrite

The v2 rewrite fixed the research gap and found a genuinely sharp idea. In doing so it introduced a subtler and
more dangerous problem.

### 1. v2 drifted off the brief

Re-read what was actually asked: *"design a completely new **experience**… think in terms of conversations, voice,
automation, proactive assistance, intelligence, human behaviour."*

That's a request for imaginative design. V2 answered a slightly different question — enterprise deployment
strategy — and did it well enough that I didn't notice the substitution. In restructuring the video around the
spending-limit idea I **cut the most on-brief material I had**: deleting "mark delivered," narrating the money, the
career ladder. Those were the concrete, imaginative, human-behaviour parts.

V1 was on-brief but forgettable. V2 was memorable but partly answered a different exam. The fix isn't to split the
difference — it's to make the authority idea **load-bearing for the experience** rather than a substitute for it.
Every moment in the day should be shown as an act of authority. Then one idea powers both halves.

### 2. "What's the agent's spending limit?" is a constraint insight, not a product insight

It's a very good observation about what *blocks* the product. It doesn't say what the product *is*. A founder
could reasonably reply: "Sharp point about enterprise sales. But you didn't design me anything."

Pushing further, there's a deeper question underneath it. Authority is what the agent can *do*. But what makes a
human manager fight for you isn't only that he can act — it's that **he has skin in the game.** His own review
depends on your outcomes.

Which exposes the real hole in v2: I asserted "the agent works for the driver" and then never said how that's
enforced. You cannot make an agent loyal with a system prompt. If its objective function is company throughput,
"be on the driver's side" is cosplay, and he will feel it within a fortnight even if he can't name why.

**Loyalty has to live in the scorecard, not the prompt.** That's the missing mechanism, and it's a better idea
than the spending limit because it subsumes it.

### 3. The frame needed to be repeatable, and wasn't

The real test of a product frame: *can the founder describe your answer to a colleague tomorrow, in one sentence?*
"He talked about giving the agent a spending limit" — half-passes. So the thesis becomes a triad instead:

> **Memory, authority, accountability.** An app has features. A manager knows you, can act for you, and answers
> to you. Today's app has none of the three.

Each maps to a concrete mechanism (driver + location graph / the authority ladder / the agent's scorecard), the
spending limit survives as the middle term, and the whole thing is repeatable.

### 4. I designed an advocate, not a manager

Serious gap. Every version so far has the agent taking the driver's side. But management's hardest work is
confrontation — and an agent that only ever advocates is a **lawyer**, not a manager. The obvious founder probe:
*"what happens when the driver is the problem?"* I had no answer.

And there's a genuinely strong idea sitting right there, which I walked past twice: **today's platforms already
punish — silently.** Algorithmic deprioritisation. Your orders quietly dry up, nobody tells you why, there's
nothing to appeal. It's the cruelest mechanism in the gig economy precisely because it's invisible. So the biggest
humane upgrade an AI manager offers isn't nudges or praise. It's that **punishment becomes spoken, specific and
appealable instead of silent.** That's on-brief (human behaviour) and it's the answer to the probe.

### 5. I mistook bluntness for integrity on the ops headcount point

I advised leading with "your ops team shrinks." But the person signing this may well *be* the ops leader whose
team I'm describing, and the claim is probably factually wrong anyway: Indian logistics is growing 20–30% a year,
so the realistic outcome is that the ops team stops *growing* and gets redeployed — dispatchers become exception
handlers, auditors, and new-city launch staff. Precision beats performative honesty. Being accurate is the
integrity move; being brutal was a pose.

### 6. The script wasn't usable as a script

726 words interleaved with visual directions can't be read off a teleprompter. Added `04-teleprompter.md` — just
the words, timed.
