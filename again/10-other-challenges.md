# The other four challenges — approach, trade-offs, follow-ups

You answered **Challenge 3 (Design for Illiterate Workers)**. The founder may probe any
of the other four to test range: *"How would you have approached the driver one?"* This
doc gives you a crisp, defensible take on each — not a full solution, a **10-minute
whiteboard answer** that shows your design worldview generalises.

> Terms like IVR, USSD, take-rate, funnel, sensitivity analysis, and human-in-the-loop
> are explained in plain language in `12-plain-language-glossary.md` (§7 and §8).

> **The meta-move for all four:** answer them in the *same voice* as your #3
> submission, so they see one coherent engineer, not four disconnected opinions. Your
> recurring principles:
> 1. **Deterministic core, LLM at the edge** — the consequential decision is legible;
>    AI does language, not judgment.
> 2. **The human holds final authority** — AI advises, drafts, advocates; a named
>    person decides anything that binds someone.
> 3. **Meet the user where they are** — no assumption of literacy, a smartphone, or
>    good connectivity.
> 4. **Trust is earned on money and a human exit**, not tone of voice.
> 5. **Instrument reality, don't over-model** — when unsure, measure at the gate / run
>    a pre-book, don't assert a number.
>
> If you close every answer by tying back to one of these, you win the round.

Quick reference — how each maps to Hunar and to your work:

| Challenge | One-line stance | Hunar / your-work hook |
|---|---|---|
| **1. AI as the Driver's Manager** | Invert who serves whom: the AI manages *up* for the driver, and never delivers discipline itself | Founders are ex-Locus (logistics); Hunar serves Swiggy/Zepto |
| **2. Kill the App** | The app was never the product; the workflow is. Voice/IVR/kiosk are transports | This is literally Hunar's product; your SafeSpace "voice is a transport, not a fork" |
| **4. If ChatGPT Was Never Invented** | Chat is the laziest of five interaction modes; push intelligence to the user ambiently | Hunar is voice-native, no chat window; your `mass-assessment` hides the LLM behind queues |
| **5. Mahindra BE 6 Batman Edition** | Funnel-estimate for a range, then *instrument demand with a deposit-gated drop* instead of forecasting | Structured estimation + "measure, don't assert" |

---

## Challenge 1 — AI as the Driver's Manager

*Logistics company, 50,000 delivery partners. Today the app is a dashboard: login, see
deliveries, navigate, mark delivered, raise a ticket. Redesign so the AI agent becomes
the driver's manager. Think conversations, voice, automation, proactive assistance,
intelligence, human behaviour.*

### The reframe (lead with this)
Today the driver *serves the app* — he logs in, he reads, he taps, he files a ticket
and waits. Flip it: **the AI serves the driver and manages upward on his behalf.** Ask
what a *good* human manager actually does — assigns work fairly, clears blockers, has
your back on pay, tells you where you stand, coaches you, and escalates for you — and
build that, mostly by voice, mostly proactively.

### The approach — five things a good manager does
1. **Proactive morning briefing (voice):** "18 drops today, expected ₹1,150, one
   apartment gate is tricky, rain likely after 3 — want the far cluster first?" No
   dashboard to open.
2. **In-the-moment blocker removal:** driver *says* "gate's locked, customer not
   picking up" → the AI calls the customer, reschedules, or authorises a safe drop —
   instead of a support ticket that sits in a queue while he idles.
3. **Earnings transparency + advocacy:** it explains today's pay, why an incentive
   didn't trigger, and flags when *he* was underpaid. The manager that has your back on
   money. (This is your #3 "explain the delta" and trust-on-money principle, reused.)
4. **Automation of the boring 80%:** wrong address, COD mismatch, customer unreachable
   — auto-resolved so he keeps moving; only the novel 20% reaches a human.
5. **Coaching, not surveillance:** "your evenings run slow in Sector 12 — reroute?"
   framed as help he can decline, never as a scorecard.

### The one boundary that is the whole product
This is the one prompt where **the AI holds authority *over* a human** — it assigns,
evaluates, can reward or penalise. So the hard rule, same as your #3: **the AI can
assign, inform, coach and advocate, but it never delivers discipline, deactivation, or
termination — that always routes through a named human.** State this unprompted; it's
the maturity signal.

### Trade-offs to name before they do
- **Proactive vs. annoying:** every interruption must earn its place; over-notifying
  destroys trust. Budget the driver's attention like money.
- **Manager vs. panopticon:** the exact telemetry that enables coaching enables a
  surveillance machine. Design choice: **the driver sees everything the AI sees about
  him first**, and advocacy ships before employer-benefit features.
- **Automation vs. hidden systemic failure:** auto-resolving "wrong address" 400 times
  hides that one warehouse mislabels everything. Auto-fix for the driver **and**
  aggregate upward for the ops team.
- **Voice in the real world:** traffic noise, helmets, 2G dead zones, code-switching
  across languages. Assume degraded conditions (your #3 instinct).
- **Gig-labour reality:** "algorithmic management" of 50k gig workers is politically and
  ethically loaded; a manager that only ever extracts will be gamed and resented.

### Likely follow-ups → how to answer
- *"How is this more than better notifications?"* → It inverts who serves whom and it
  *closes loops* (resolves, not just informs). A notification tells you the gate is a
  problem; a manager gets the gate opened.
- *"How do you stop it being surveillance?"* → Driver-first transparency, an advocacy
  metric on the dashboard, and a refusal to make punitive action the default path.
- *"Why would a driver trust it's on his side?"* → Same trust ladder as my #3: a track
  record on getting his money right, a named human he can reach, and visible wins that
  benefit *him* before they benefit the employer.
- *"What breaks first in production?"* → The blocker-resolution features need real
  telephony + warehouse/customer data integrations, and address data quality. I'd
  instrument that in week one rather than assume it.

---

## Challenge 2 — Kill the App

*Most workforce apps are Dashboard → Tasks → Notifications → Settings. Imagine
smartphones disappear tomorrow. Design a workforce-management product and explain how
workers interact with it.*

### The reframe
The smartphone app is a **UI accident of this decade**, not the product. The product is
the *workflow* — attendance, tasks, pay, coordination, support. Strip the phone and the
durable substrate underneath is **conversation**. (This is Hunar's actual thesis —
Krishna's line that 80% of HR is calling — so say it and mean it.)

### The approach — channel-agnostic agent, many transports
Build **one agent core, many transports** (this is exactly your SafeSpace pattern:
"voice is a transport layer, not a fork of the agent logic"). Transports that survive
without smartphones:
- **Voice call / IVR** on any feature phone or landline — inbound and outbound.
- **Missed-call and SMS/USSD** for zero-cost triggers and confirmations.
- **Shared devices at the worksite** — a gate kiosk, a badge reader, a supervisor's
  tablet — for the rare thing that truly needs a screen.
- **The supervisor as a human relay**, with an audit trail.

Interaction model:
- **Outbound at the right moment:** the AI *calls* — shift reminder, schedule change,
  "you're not clocked in, everything okay?"
- **Inbound on demand:** worker gives a missed call → gets a call back → handles
  attendance, leave, pay questions, grievances by voice.
- **Attendance without a personal device:** voice check-in with voice-print, or a
  shared gate device, or supervisor attestation logged for audit.
- **Anything complex (a payslip) is decomposed** into confirmable chunks — your #3
  rule: *she never composes, she only confirms — except she must produce a number* for
  anything that binds her.

### Trade-offs to name
- **Identity/auth without a personal device** is the hardest problem — voice-print
  (noisy, imperfect), shared-device PINs, or supervisor vouching (collusion risk).
- **Shared devices vs. privacy** — reuse your #3 shared-handset privacy gate.
- **Voice conveys sequence poorly** — you can't "scan" a payslip by ear; you must
  restructure information, not just narrate it.
- **IVR rigidity vs. LLM-voice flexibility vs. cost/latency** of always-on voice.
- **Connectivity:** design for 2G and dropped calls (resumable conversations — like
  Hunar's audio-regenerative approach to interruptions).

### Likely follow-ups → how to answer
- *"Isn't this just a call centre?"* → No. A call centre is inbound and reactive. This
  is an autonomous agent that *initiates*, remembers context across calls, closes
  loops, and escalates to a human — a manager, not a helpdesk.
- *"How does a worker trust a phone number?"* → Consistent caller identity, a named
  human backstop, and value on the first call (your trust ladder again).
- *"What's genuinely hard here?"* → Identity without a device, and conveying money/
  complex state by voice. I'd prototype those two first because everything else is
  easy by comparison.
- *"Doesn't this describe Hunar?"* → Largely, yes — which is why I believe in it. The
  extension is treating attendance, pay and grievance as first-class voice workflows,
  not just hiring.

---

## Challenge 4 — If ChatGPT Was Never Invented

*You still have LLMs, but there is no chat window. Design the product without a
traditional chat interface.*

### The reframe
Chat is the **laziest** thing you can do with an LLM: it dumps the burden of prompting
onto the user. For a busy, non-literate, or frontline user that's exactly backwards —
**the intelligence should come to them**, structured, at the right moment. The LLM's
value is understanding + generation + reasoning, none of which requires a text box.

### The approach — five interaction modes, chat is the worst of them
1. **Voice / conversation** — the LLM as a caller and listener (no typing).
2. **Ambient / proactive ("zero-UI")** — the LLM watches state and acts or nudges at
   the right moment, with no prompt at all. (Your #3 "outbound at the right moment.")
3. **Structured / one-tap** — the LLM *pre-computes* the likely options; the user
   confirms or picks. (Your "confirm, don't compose.")
4. **Invisible LLM-in-the-loop** — it parses documents, classifies tickets, drafts for
   a human to approve. The user never "chats"; they just see a better output. (Your
   `mass-assessment` tier-rationale and `assessment-tool` approval workflow — exactly
   this.)
5. **Self-filling forms / self-writing reports** — the artifact updates itself.

The reframe sentence: *"Chat asks the user to know what to ask. I'd rather the system
already know, and bring the answer to them."*

### Trade-offs to name
- **Proactive needs good triggers** — a wrong nudge is worse than silence; you need
  reliable state to act on.
- **Removing the open text box removes flexibility** — you can't ask arbitrary things;
  mitigate with a **voice fallback** for the long tail.
- **Invisible decisions need explainability + a human check** — reuse deterministic-
  core/LLM-edge and the approval step, or you've built an unaccountable black box.
- **Pre-compute cost vs. on-demand latency.**

### Likely follow-ups → how to answer
- *"So you just mean voice?"* → Voice is one mode. The deeper idea is **ambient +
  structured**; chat is one of five modes and usually the worst for this user.
- *"Concrete example in Hunar's world?"* → Onboarding. Instead of a chatbot, the AI
  *calls* the new hire, walks them through step by step, confirms understanding by
  asking them to state a number back, and files the record — LLM throughout, zero chat.
- *"Isn't a text box sometimes just the right tool?"* → Yes, for a literate power user
  at a desk. For Hunar's user it's the exception, not the default — which is my whole
  point.

---

## Challenge 5 — Mahindra BE 6 Batman Edition (estimation)

*Estimate how many people would buy the BE 6 Batman Edition, so you manufacture only a
limited number. Explain approach, assumptions, data points, methodology.*

> This one tests **structured estimation** — labelled assumptions, a funnel, a
> sensitivity check — and business judgment. The standout move: **don't just forecast a
> number, instrument demand.** (And note the real-world answer below — it's a gift.)

### Approach — a funnel, then a cross-check, then the meta-insight

**Top-down funnel** (state every assumption as an assumption):
1. **Base model volume.** Mahindra's three EVs (BE 6, XEV 9e, XEV 9S) sold ~65,000
   combined over ~16 months (Jan 2025–Apr 2026). So BE 6 alone is on the order of
   **~1,500–2,000/month → ~20,000/year** *(assumption, since Mahindra reports them
   combined)*.
2. **Special-edition take-rate.** A cosmetic trim usually pulls ~1–5% of a model's
   volume. A **licensed collector edition at a big premium** behaves differently — it's
   not "how many BE 6 buyers want this trim," it's "how many superfans want *this
   object*." So the base-volume funnel gives a floor, not the answer.
3. **The premium filter.** Batman Edition is **₹27.79 lakh** vs a ~₹18.9 lakh base —
   roughly a **47% premium**. That narrows the pool to affluent buyers who are *also*
   Batman/DC superfans *and* collector-minded *and* EV-willing.

**Bottom-up cross-check:** intersect {can spend ~₹28L on an EV} ∩ {Batman superfan, not
casual} ∩ {wants a themed/collector car} ∩ {comfortable being an EV early adopter}. In a
country of 1.4B, that intersection is small but real — realistically **low thousands**
of genuinely willing buyers, of whom only a fraction convert in any given window.

**Estimate:** a defensible limited run is **~1,000–2,500 units**, and for a *collector*
edition you deliberately cap **below** true demand to preserve exclusivity and resale
value.

### The real-world answer (use this — it's current and it validates the method)
Mahindra actually ran this experiment. The Batman Edition launched at **₹27.79 lakh**,
capped at **999 units** — and **sold out in 135 seconds** (Aug 2025). Demand so
obviously exceeded supply that they **reopened for ~300 more**. Two lessons:
- The **999 cap was a scarcity/brand decision, not a demand forecast** — true demand was
  several multiples higher.
- The right instrument isn't a spreadsheet, it's a **deposit-gated limited drop**:
  ₹21,000 refundable booking, let the waitlist reveal real demand, then manufacture to
  committed pre-orders plus a small buffer.

### The meta-insight to deliver (this is what impresses)
> "For a limited collector edition, the number isn't really a demand-forecasting
> problem — it's a scarcity-strategy problem. I'd size a range with the funnel to sanity-
> check tooling economics, then **instrument demand with refundable pre-orders rather
> than commit factory capacity to a guess.** Set the founding run at a symbolic,
> scarcity-preserving number — 999, or something Batman-coded — and keep a second drop
> in reserve to capture overflow without diluting the first. Which, it turns out, is
> almost exactly what Mahindra did."

That is your #3 principle transplanted onto a business question: **when you're unsure,
measure reality at the gate; don't over-assert a number.**

### Trade-offs / sensitivities to name
- **Scarcity vs. revenue:** cap too low = hype + resale markup but money left on the
  table; too high = unsold inventory and diluted exclusivity.
- **The estimate is dominated by two assumptions** — base volume and take-rate. Show the
  range: at a 1% take-rate you're near ~200; at "collector superfan" demand you're past
  2,000. Quote the range, not false precision.
- **A licensed tie-in adds a royalty cost** per unit (Warner Bros.), which pushes toward
  a higher price and a smaller, higher-margin run.
- **Deposits change behaviour:** a refundable ₹21k filters tyre-kickers far better than a
  survey — which is why it's the right instrument.

### Likely follow-ups → how to answer
- *"What's the single biggest driver of your number?"* → The take-rate assumption. I'd
  de-risk it with deposit-based pre-bookings before committing tooling.
- *"How would you validate before spending on production?"* → A landing page with
  refundable deposits, dealer interest polling, and social-listening on the reveal —
  cheap signals before expensive commitments.
- *"Why make it limited at all?"* → Scarcity economics, collector positioning, and the
  licensing terms all point to a small, premium, numbered run over mass volume.
- *"Your number differs from Mahindra's 999 — why?"* → 999 was a brand/scarcity choice,
  and the 135-second sellout proves latent demand was higher. My funnel estimates
  *willingness*; their cap reflects *strategy*. Both are right answers to different
  questions.

---

## Closing note for the round

If asked *"why did you pick #3 and not these?"* — you have the answer in
`00-pick-decision.md` and `08` §6.1: #3 rewarded homework over imagination, and for a
company built on two years of fieldwork you bet homework was the higher-signal choice.
But being fluent on all five shows the founder your design principles aren't specific to
one prompt — they're how you think.

---

*Data points for Challenge 5 (current as of the interview window): BE 6 Batman Edition
price ₹27.79 lakh, first run 999 units sold out in ~135 seconds, reopened for ~300 more,
₹21,000 booking amount — [Mahindra press release](https://booking.mahindra.com/press-releases/be6-batman-edition-returns.html),
[Hindustan Times](https://www.hindustantimes.com/car-bike/mahindra-be-6-batman-edition-deliveries-begin-heres-whats-special-about-it-101758867333075.html).
Mahindra EV volumes (BE 6 / XEV 9e / XEV 9S ~65,000 combined, Jan 2025–Apr 2026) —
[Autocar Professional](https://www.autocarpro.in/analysis-sales/mahindra-be-6-xev-9e-xev-9s-sales-cross-65000-mm-e-pv-retail-share-jumps-to-21-percent-132716).
Content rephrased for compliance with licensing restrictions.*
