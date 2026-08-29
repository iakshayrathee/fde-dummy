# Designing for 100,000 workers who can't read

**Hunar.AI · Forward Deployed Engineer · Product Thinking Challenge #3**
Companion to the 5-minute video. Read time: ~2 minutes.

Customer: multi-plant apparel manufacturer. 100,000 workers, mostly migrant women.
Wages = piece rate + attendance incentive − statutory deductions.

---

## The argument in four lines

**1. The brief holds two different problems.** 40% can't read English — that's
translation. 20% can't read *anything* — that's 20,000 people translation won't
help. Design order decides who gets a second-class product.

> **Reading is the accommodation. Listening is the baseline.**

**2. Voice alone doesn't fix it.** Odia ASR benchmarks near **35% WER** against
Hindi's **16%**. Open speech can't be trusted with anything consequential.

> **She never composes. She only confirms.**
> Except for consent, where she must **produce a number** — because a confirm-only
> interface aimed at someone who agrees with authority manufactures agreement.
> Numerals are ASR-reliable, numeracy outruns literacy, and a number can't be faked
> by nodding.

**3. Not an app, not a chatbot.** Outbound conversations at the right moment,
passive sensing at the plant, a shared screen at the line. If smartphones vanished
tomorrow, ~80% survives.

**4. Sequence decides what you've built.**

> If the first thing it does is check whether she showed up, it's surveillance. If
> the first thing it does is find her a missing ₹340, it's her manager.
> **Make it useful to her before it's useful to them.**

---

## The five answers, one line each

| | Mechanism | The move most people miss |
|---|---|---|
| **Onboarding** | A recorded disclosure, not a signed form. She keeps the recording. | Comprehension tested by **arithmetic**, not agreement: *"take two days off — how much less?"* |
| **Attendance** | A by-product of being present. She does nothing. | Every supervisor override triggers an **evening verification call to her**, making the rent-seeking path visible |
| **Salary** | Explain the **delta**, not the total. Mid-month, not on payday. | *"PF is your money, it stays in your name"* — one sentence between savings and theft |
| **Training** | Silent video, narration as a **separate audio track**. Shoot once, localise into 8 languages for 8 voice recordings. | The exam is her **defect rate over 50 pieces**. Never measure completion. |
| **Trust** | A track record on money, plus a named human exit on every call. | Once a month it **finds money in her favour**, unprompted |

**Verification, every flow.** Before any figure is spoken, the AI confirms it's her —
her voiceprint on a phone, or the same gate that marks her present at a line-side
screen, so there's no PIN to read. It runs identically on payday, absence, and
advocacy calls, so **a shared handset never hears her pay**, and she picks the channel
money reaches her on. This is what keeps the design from quietly assuming the personal
phone that the 38% figure says most women don't own.

---

## The numbers, with sources

| Fact | Figure | Source |
|---|---|---|
| Odia vs Hindi speech recognition | ~35% vs ~16% WER | [arXiv 2602.03868](https://arxiv.org/html/2602.03868v2) |
| Aadhaar biometric auth failure | ~6.5%, flat for a decade | [Policy Circle](https://www.policycircle.org/opinion/aadhaar-authentication-failures/) |
| Worn fingerprints, Telangana scheme | ~36% verification failure | HuffPost India archive |
| Face recognition demographic bias | varies **by algorithm**; FNMR driven by image quality | [NIST FRVT](https://pages.nist.gov/frvt/html/frvt_demographics.html) |
| Phone ownership, women vs men | 38% vs 71% | [Yale EGC](https://egc.yale.edu/research/pande-and-coauthors-understanding-barriers-and-impacts-womens-mobile-phone-adoption-india) |
| Help-seeking predicts *higher* digital confidence | n=604 women informal workers | [Springer 2026](https://link.springer.com/article/10.1007/s40012-026-00432-4) |
| Contract labour at 100+ worker firms | ~38% of employment | [NBER w29151](https://www.nber.org/papers/w29151) |
| Karnataka garment minimum wage | ~₹13,000/mo, ~30% below other industries | [Times of India](https://timesofindia.indiatimes.com/city/bengaluru/textile-workers-union-slams-karnataka-govt-for-exclusion-from-wage-revision/articleshow/131294323.cms) |
| Wage opacity → stoppage | Noida protests, April 2026 | [Indian Express](https://indianexpress.com/article/explained/rising-costs-stagnating-wages-why-workers-are-protesting-in-india-10636950/) |

---

## Sequencing and economics

| Phase | Scope | Gate |
|---|---|---|
| Wk 0–4 | Salary variance calls · 1 plant · ~2,000 workers | Needs only payroll data they already have |
| Wk 4–10 | Onboarding disclosure + numeric comprehension check | No hardware |
| Wk 10–20 | Attendance layers + audit loop | Needs gate hardware; goes **after** trust exists |
| Wk 20+ | Training library, line-side delivery | Needs content production |

**Cost:** ~356,000 billed min/month at ₹6/min (range ₹4–8) ≈ **₹2.6 cr/yr**, plus
~25 FTE for the human escalation layer I promised ≈ **₹0.9 cr/yr**. All-in **~₹350
per worker per year — under one day of her wages.**

**Return, stated as breakeven rather than a multiple:** this must prevent ~4,300
departures a year — roughly **4 attrition points** — to pay for itself. The ₹8,000
replacement cost and the 55% answer-rate assumption are the two figures I'd replace
with their actuals in week one; answer rate is the largest sensitivity in the model.

**Method:** holdout by plant or line. Never a big-bang rollout.

**North star:** *unaided recall* — can a randomly sampled worker state her own wage
structure and this month's expected pay, unprompted? Everything else is a proxy.

---

## What I refuse to build

No voice-read productivity leaderboards, including comparisons against her own
average — that's a leaderboard of one, and in piece-rate work it's speed-up dressed
as transparency. No AI-delivered termination or discipline. No always-on floor
audio. No salary to an unverified handset. No engagement nudges that exist to fill a
dashboard.

---

## What I don't have

Stated because a design that hides its holes isn't finished.

**Contract labour is unsolved.** ~38% of workers at large Indian factories sit on
contractor payrolls. For them the salary wedge does not function at all, and they're
the most precarious people in the building. I have a week-one discovery plan and a
fallback (attendance first) — not an answer. **This is the finding that would make me
tear up my own sequence.**

**No primary research.** All secondary sources. The comprehension check and the
audit loop came from reasoning, not from watching a shift change.

**Two invented numbers** in the economics: ₹8,000 replacement cost, 55% answer rate.

**Still missing:** shared-handset rates specific to garment factories; published
day-30 attrition for Indian apparel.

---

*Sources rephrased for compliance with licensing restrictions.*
