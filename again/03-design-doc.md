# Design doc — Challenge #3: Design for Illiterate Workers

Customer: multi-plant apparel manufacturer, 100,000 workers, migrant-heavy,
majority women. Wages = piece rate + attendance incentive − statutory deductions.

Field facts and sources: `02-research-notes.md`. Every claim below traces there.

---

## Part 1 — Reframing the brief

### The two populations are not one problem

The brief gives two numbers and most readers will blur them together.

- **40% cannot comfortably read English.** This is a *translation* problem.
  Use their language. Well-understood, cheap, not interesting.
- **20% struggle to read in any language.** At 100,000 workers that is
  **20,000 people**, and translation does nothing for them. Reading has to leave
  the critical path entirely.

The two need opposite treatment, and the order you design in decides who gets a
second-class product.

### The inversion

> **Reading is the accommodation. Listening is the baseline.**

Design the non-literate path as the *default*, and text becomes an optional
enhancement for those who want it. Do it the other way round — build the normal
product and bolt on accessibility — and the 20,000 get a degraded side entrance
forever. This is the one structural decision that everything else follows from.

It also happens to make the product better for the other 80,000, because nobody
actually enjoys reading a payslip.

### What she is not

She is unlettered, not incapable. **Numeracy substantially outruns literacy** in
this workforce: a worker who cannot read the word "deduction" will tell you to
the rupee what she is owed and how many days she worked. That is an asset to
design *with*.

So: rupees and days, spoken aloud. Never percentages, never pro-rata, never
"statutory".

### Assumptions I am refusing to make

The brief says design without making assumptions. Listing them explicitly, because
each one is load-bearing and each one is commonly made:

| Common assumption | Why it fails here |
|---|---|
| she owns a phone | ~38% of Indian women own a mobile vs ~71% of men |
| the phone is a smartphone | women ~20% less likely to own one |
| the number on file is hers | access ≫ ownership; handsets are borrowed from male relatives |
| the language on her form is the language she speaks | Odia/Bengali/Hindi speakers working in Kannada and Tamil states |
| speech recognition understands her | Odia ASR ~35% WER vs Hindi ~16% |
| her fingerprint works | the work wears the fingerprint away |
| a thumbprint means consent | it means a thumb was pressed |
| silence means understanding | silence means silence |
| she will ask when confused | she will agree with authority instead |
| she uses the product alone | assisted use is the norm, and it is healthy |

---

## Part 2 — The design rule

Everything reduces to one rule, and the rule is derived, not asserted.

The hardest thing for a non-literate user is not *understanding* information.
Listening comprehension is intact and near-perfect. The hard thing is
**producing** structured information — writing, typing, navigating a menu,
speaking a sentence cleanly enough for an ASR model that is wrong a third of the
time in her language.

So:

> ## The worker never composes. She only confirms.
>
> Every interaction is: the system already knows → states it in her language →
> she confirms with one word, one keypress, or silence.

### The exception that keeps the rule honest

A confirm-only interface has a defect, and it is the *same* defect as the problem
it solves: **when the only affordance is agreeing, the system manufactures
agreement.** She already agrees with authority. Give her a design whose sole verb
is "yes" and you have industrialised acquiescence.

So the rule is deliberately two-tier:

| What is happening | What she does |
|---|---|
| Information delivery, routine operations | **Confirm.** One word, one key, or silence. |
| Consent, or any legally operative term | **Produce a number.** |

For anything that binds her, confirmation is not evidence of comprehension. She
has to state a **quantity** back:

> *"If you take two days off next month, how much less will you get?"*

That works for three reasons that all come from the constraints. Numerals are the
most reliable class in Indian-language ASR, so recognition is not the weak link.
**Numeracy substantially outruns literacy** in this workforce, so the question is
answerable by someone who cannot read a word of it. And a number cannot be
produced by nodding along — it is the one answer acquiescence cannot fake.

Three principles fall out of the rule.

**P1 — The system speaks first.** If she has to initiate, she has to compose a
request. So the product is proactive by necessity, not by fashion. There is no
inbox, no menu, no dashboard, and no place to get lost.

**P2 — Nothing consequential rides on recognition.** At 35% WER, open speech
cannot be allowed to touch a record. Closed vocabulary, repeat-back before every
commit, keypad and missed-call as *equals* rather than fallbacks. Open speech is
permitted only where a mistake is cheap and recoverable.

**P3 — Assistance is a feature, not a leak.** Help-seeking predicts *higher*
confidence, not deficit. So make assistance safe and auditable rather than
designing it away.

And one product-shape consequence worth stating out loud: **this is not an app,
and it is not a chatbot.** It is a set of outbound conversations that happen at
the right moment, plus passive sensing at the plant, plus a shared screen at the
line. If smartphones vanished tomorrow, roughly 80% of this design still works.

---

## Part 3 — The five answers

Each one: mechanism, then the failure mode I expect, then the metric.

---

### 3.1 Onboarding

**The problem.** Onboarding today is a stack of forms she cannot read, signed
with a thumbprint, on top of a verbal promise from a recruiting agent. Research
on Bengaluru garment workers documents exactly this — pay that turned out lower
than the agent promised once rent, water and electricity came out. **The lie is
installed at hiring and detonates on payday.** Onboarding and salary are the
same problem, six weeks apart.

**Mechanism — onboarding is a recorded disclosure, not a signed form.**

1. **The deal, spoken.** An outbound call before day one, in her spoken language.
   Not form-filling — *disclosure*. The AI states: role, shift, base wage, piece
   rate, attendance incentive, every deduction and what it is for, supervisor's
   name, and an estimate of her actual first-month take-home in rupees. She
   confirms each material term with one word or one key.
2. **The recording is the artifact.** Timestamped, stored, and *retrievable through
   the channel she chooses at onboarding* (§3.3) — her handset if she controls one, a
   line-side kiosk if she does not — so she can replay it for her husband, her
   father, or a friend before she commits. The word is *retrievable*, not "kept on
   her phone": this design cannot assume a personal device it elsewhere says most
   women lack. A contract she can hear beats a contract she signs blind.
3. **Documents without typing.** She never keys an Aadhaar number. Photo capture
   at the plant kiosk, OCR extracts it, the AI reads it back digit by digit, she
   confirms. Production becomes confirmation.
4. **Identity enrolled correctly from day one.** Voiceprint plus a face photo at
   the kiosk. Explicitly *not* fingerprint. The voiceprint captured here is exactly
   what every later call uses to confirm it is her before it says a word about money
   (§3.3) — so enrolment and the privacy gate are one investment, not two. And one
   question that shapes everything downstream: *"Is this phone yours, or do you share
   it?"*
5. **Language detected, not declared.** Her language comes from the first ten
   seconds of speech, not from the form. Dialect stored separately from language.

**Failure mode.** She agrees with everything, because when a stranger with
authority asks if you understand, you say yes.

**Countermeasure — the numeric comprehension check.** At the end of the
disclosure, the AI asks her to compute, not to confirm:

> *"If you take two days off next month, how much less will you get?"*
> *"How many pieces do you need to finish to earn your incentive?"*

If the number is right, comprehension is real. If it is wrong or absent, the call
routes to a human and the disclosure is redone in person. Aggregate check-failure
rate becomes an onboarding-quality metric the employer can act on.

> **Rejected alternative, and why.** My first version had the AI state one term
> *wrongly* on purpose to see whether she would correct it — an attention check
> borrowed from survey research. I killed it. If the recording is the contract
> artifact, then deliberately misstating a material term of employment puts a
> false statement inside a legally operative document during contract formation.
> Survey attention checks do not live inside contracts. The numeric check gets the
> same signal with none of that exposure, and it is a better test besides: a wrong
> number is unambiguous, whereas a failure to correct could just be politeness.

**Metrics.** Unaided recall at day 7 — can she state her own wage structure
without prompting. Comprehension-check failure rate. Day-30 attrition. Volume of
"this is not what I was promised" grievances.

---

### 3.2 Attendance

**The problem.** Fingerprints fail because the work destroys them — roughly 6.5%
of Aadhaar biometric authentications fail nationally and have for a decade, and
in one Telangana scheme worn fingerprints were behind about 36% verification
failure. Cards get proxied. Supervisor-marked attendance creates dependency, and
dependency on a supervisor for your wages is a rent-seeking opportunity.

Attendance is not a UX event. **It is a wage event.**

**Mechanism — attendance is a by-product of being present, not a task she
performs.** If she walked through the gate, she is present. Her job is nothing.

**But I will not name the modality from here.** In an earlier draft I demolished
fingerprints with hard numbers and then endorsed face recognition on assertion.
That was the weakest move in this document, and the evidence does not support it.
NIST's FRVT programme documents demographic differentials that **vary
substantially between algorithms**, with false non-match rates driven largely by
image quality and ageing — and a 6am shift change in poor light, with headscarves,
is close to a worst case for image quality.

So the deliverable is not a modality. It is a **selection procedure**:

> Instrument the gate for two weeks. Measure false non-match rate disaggregated by
> cohort and by shift hour. Choose on measured performance, never on a datasheet.
> Guarantee a non-biometric path regardless of which option wins.

I pick the modality from two weeks of measurement at their gate, not from a
brochure. What I *can* commit to before measuring: **not fingerprint**, because
the mechanism of failure is already established, and **never a single modality
alone.**

Layered, and failure is never hers to solve:

- **Layer 1 — passive, dual-signal.** Whichever modality survives measurement,
  paired with a cheap NFC badge tap. A badge alone is proxyable; a biometric alone
  fails; the pair is defensible.
- **Layer 2 — discretion.** If both fail, the supervisor's tablet shows her photo
  and one tap marks her present. Necessary, and dangerous.
- **Layer 3 — the audit loop, which is the actual design.** Every
  supervisor-marked entry triggers an automatic evening call to the worker:
  *"The gate did not recognise you today and your supervisor marked you present.
  Is that right?"* One key. This makes the discretionary path visible and
  expensive to abuse without removing it.
- **Layer 4 — self-repair.** Three gate failures for the same worker in a
  fortnight auto-schedules re-enrolment. The system fixes itself instead of
  blaming her.

**Absence, handled as a manager would.** No leave form. She did not appear, so
the system calls: *"You are not at the gate. Are you taking leave, or is
something wrong?"* One key. And critically, it tells her the money consequence
*before* she decides: *"If today is unpaid leave, your attendance incentive drops
by about ₹250 this month."* A dashboard tells you after the fact. A manager tells
you while you can still change your mind.

**Failure mode.** Recognition fails unevenly, and the average hides it. Whatever
modality wins the bake-off will have cohorts it serves badly — by skin tone, by
head covering, by age, by shift hour.

**Countermeasure.** **Never report the average.** Track failure rate
disaggregated by cohort and by shift hour, treat a rising per-cohort rate as a
**system defect under SLA** rather than worker error, and let the badge silently
become primary for any cohort that crosses a threshold. The system absorbs its own
unfairness instead of passing it to the worker as a lost day's pay.

**Metrics.** Share of attendance records requiring human discretion (drive it
down). Disputes per 1,000 wage records. Gap between gate-recorded days and
payroll-credited days. Per-cohort recognition failure rate as a standing
guardrail.

---

### 3.3 Salary — the centrepiece

**The problem.** She does not want her payslip. She wants to know why this month
is less than last month. Piece rate + attendance incentive − PF − ESI − advance
− canteen − hostel is not reconstructable by anyone, literate or not. The "why is
₹360 taken from me every month" question about ESI recurs endlessly in public.
And unexplained wage variance is not a soft issue — during the April 2026 Noida
protests a worker told PTI his payslip did not reflect his hours: 12 to 14 hour
days, overtime paid on three of them, about ₹13,000 a month.

**Mechanism — explain the delta, not the total. Before she asks.**

The payday call, in her language and her arithmetic:

1. "This month you will receive ₹12,480."
2. "Last month it was ₹13,100. **It is ₹620 less.**"
3. "Here is why. Two days absent — that is ₹520. And ₹100 more went into your PF,
   because you worked more overtime."
4. **"PF is your money. It stays in your name. You can take it out."**
5. "Do you want any part again? Press 1."

Four things are load-bearing there:

- **Delta first, never totals first.** People reason about change, not absolutes.
  The change *is* the story.
- **Her units.** Rupees and days. Not percentages, not pro-rata, not "statutory
  deduction".
- **Deductions reframed as ownership.** The difference between a deduction
  understood as savings and one understood as theft is the difference between
  trust and a protest. This costs one sentence and almost nobody says it.
- **Nothing is read out until she is verified** (see privacy gate below).

**Mid-month variance alerts, which matter more than the payday call.** *"You have
been absent three days this month. If it stays like this, your pay will be about
₹500 lower than last month."* She can still act. This is the single clearest
expression of manager-instead-of-dashboard in the whole design.

**Piece-rate feedback — cut, on review.** An earlier draft had a daily call:
*"Today you finished 340 pieces, your average is 310, that's about ₹40 more."* I
have removed it, because it contradicts my own refusal list. I refuse voice-read
productivity leaderboards as humiliation at scale, and a comparison against her
own rolling average is a leaderboard of one. In piece-rate garment work, where
speed-up and self-exploitation are documented harms, an earnings-per-piece nudge
delivered daily by an employer's system is a productivity-pressure mechanism
wearing transparency's clothes.

What survives: **on request only, never pushed, and never comparative.** She can
ask what she has earned so far this month and get a rupee figure. No average, no
trend, no ranking, no unprompted call. The wage-effort link stays available to her
and stops being a lever aimed at her.

**Informal debt, surfaced.** Advances taken from supervisors and contractors are
invisible and compounding. Read the outstanding balance and repayment schedule
aloud monthly, and informal debt becomes visible to both sides.

**The privacy gate — direct consequence of shared handsets.** Before any figure
is spoken, verify it is her, by whichever channel she is on: a **voiceprint** match
on her first sentence on a phone, a keyed **PIN** if she prefers one, or — at a
line-side screen — **the same measured gate that marks her present** at attendance,
so the kiosk needs no PIN she would have to read. Identity reuses the attendance
modality rather than standing up a second one; the voiceprint itself is enrolled
during the onboarding disclosure (§3.1).

**This gate is not specific to payday.** *Every* proactive call runs it first — the
absence call (§3.2), the monthly advocacy call (§3.5), the dispute callback. A shared
handset therefore never hears a rupee figure, whichever flow placed the call, because
verification lives at the channel rather than inside any one feature.

If verification fails, the AI says only *"I have information about your work"* and
**nothing** about money. Note what it does **not** say. An earlier draft had it
add *"please call back from somewhere private"* — which is a mistake, because in a
household where a male relative controls the handset, an instruction to seek
privacy is itself a signal that there is something to hide. The fallback message
has to be **flat and uninteresting**, carrying no hint that the content is
sensitive.

**Delivery is her choice, not her exclusion.** My first version said salary is
simply never pushed to a shared handset, and she hears it at the plant kiosk
instead. That inverts my own principle: the workers with least control over a
phone would get the worst experience, which is precisely the side-entrance failure
this whole design exists to avoid.

So at onboarding she picks where money information reaches her:

| Option | Suits |
|---|---|
| Her handset, PIN-gated | she controls the phone |
| A named alternate handset and time window | shared phone, predictable private moment |
| **Line-side screen or kiosk at her workstation** | no reliable private phone access |
| A printed voice-QR she can replay at the plant | wants a record to keep |

The kiosk sits **at her line, not in an HR office**, so choosing it is convenience
rather than a summons. Any option can be changed later by one keypress on any
call. The point is that no delivery channel is a downgrade, and she is the one
choosing.

**Dispute path.** *"This is wrong — press 2."* That opens a ticket with the call
recording attached, routes to payroll, and guarantees a voice callback with the
outcome **whether or not she was right**. Closing the loop out loud is the part
that builds trust; being correct is only half of it.

**Failure mode.** She disputes, payroll turns out to be right, and she feels
dismissed. Or she disputes correctly and the fix arrives silently.

**Countermeasure.** Every resolution is read back as a line-by-line
recomputation, and it carries **a human name** — *"Lakshmi in HR checked this
herself."* Attribution to a person matters more than the arithmetic.

**Metrics.** Payroll query volume per 1,000 workers. Share of workers who can
state their expected take-home *before* payday. Dispute rate, and dispute
*resolution* time. Day-90 attrition for the cohort receiving variance alerts
**against a holdout that does not** — run it as an experiment, not a rollout.

---

### 3.4 Training

**The problem.** Classroom instruction, in a language she may not speak, from a
trainer reading slides, assessed by a quiz. Meanwhile the actual skill —
attaching a collar, setting a seam — is physical and visual. **Non-literate is
not non-skilled.**

**Mechanism — demonstration and correction on the line, not instruction in a
room.**

1. **Silent-first video.** Shot over the shoulder at the machine. No on-screen
   text. One operation per clip, 40 to 90 seconds. Narration is a *separate audio
   track*, which means you shoot once and localise into eight languages for the
   cost of eight voice recordings. That is a production-economics insight, not
   just a UX one — it is what makes multilingual training affordable at 100,000
   workers.
2. **Delivered where she is, not on a phone she may not own.** Shared tablet at
   the line, or a wall screen during the shift-change window. WhatsApp voice note
   is a *bonus* channel for those who have it, never the primary.
3. **Assessment is demonstration, never a quiz.** She performs the operation. The
   pass signal is the measured defect rate on her next 50 pieces. The garment is
   the exam.
4. **Voice reinforcement the next day, 30 seconds.** *"Yesterday you learned
   collar attach. What is the one thing to check before you start?"* Open speech
   is fine here — this is precisely the case where a recognition error is cheap,
   so P2 permits it.
5. **Peer-taught content.** Record the best operator on that line explaining the
   operation in her own dialect, and ship that as the asset. Cheaper than studio
   production, better dialect coverage, and authority from a peer lands harder
   than authority from a corporate voice.
6. **Help without literacy.** A call button at the station. A voice agent asks
   what is happening and either plays the right 40-second clip or pages the
   supervisor. Triage with no reading and no navigation.

**Failure mode.** Training completion becomes a number the plant games. Everyone
is marked trained, nothing changes on the line.

**Countermeasure.** **Never measure completion.** Measure time-to-standard-output
and defect rate. If those do not move, the training did not happen, regardless of
what the report says.

**Metrics.** Days from joining to standard hourly output. First-pass defect rate
by operation. Rework hours. Supervisor pages per operator per shift, falling over
time.

---

### 3.5 Trust — how AI earns the right to manage her

**Start from the truth.** She has already been lied to by a recruiting agent. She
has no reason to trust an automated voice, and an AI that manages her is an AI
with power over her income. **Her distrust is rational and correct.** Any answer
that treats trust as a tone-of-voice problem is wrong.

> Trust is not a feeling to design for. It is a **track record on money**, plus a
> **visible way out of the machine**.

Five mechanisms, ordered by actual impact:

**1. Be right about her pay, out loud, before she asks — repeatedly.** If the AI
tells her on the 20th what will arrive on the 30th, and it is right, it has
standing. Nothing else moves trust remotely as much. *This is why salary is the
wedge, not onboarding.*

**2. Borrow authority before earning it.** In month one the AI is introduced *by*
someone she already trusts: her line supervisor plays the first call beside her,
or the first message is her supervisor's own recorded voice saying "this system
will call you about your pay — and if it is ever wrong, come to me." Trust
transfers along existing relationships. Same reason training content uses a
peer's voice, not a synthetic one.

**3. Always offer a human, and never hide the exit.** Every call ends with one
key to a **named** person. An AI that cannot be escaped is not trusted, it is
endured. And a hard architectural rule:

> **The AI never delivers termination, disciplinary action, or the rejection of a
> grievance.** Ever.

Bad news from a machine is a betrayal. Bad news from a named human is a decision.
Knowing what the AI is *not allowed to do* is part of the design, not a caveat.

**4. Say what you are.** The agent identifies itself as automated in the first
sentence of every call — not for compliance, but because being caught pretending
is unrecoverable. And it never performs certainty it lacks: *"I am not sure. I
will have a person call you"* is a trust-building sentence, not a failure.

**5. Advocate for her at least once a month.** Run a standing check for
under-credited entitlements — an unclaimed incentive, a missed overtime entry, a
PF balance she does not know about, a statutory benefit she is eligible for — and
call her about it unprompted.

> An AI that only ever enforces is a supervisor. An AI that sometimes advocates
> is a manager.

That one behaviour changes what the system *is* in her mind, and it is the
cheapest thing on this list to build.

**Plus: make assistance safe.** An explicit "play this for my friend" mode. She
can hand the phone over. The system logs that assistance occurred and **refuses
consequential confirmations while in assisted mode**, scheduling a callback to
her alone instead. Help is welcome. Impersonation is not.

**Failure mode.** Trust dies in a single event — one confidently spoken wrong
salary figure.

**Countermeasure.** Calibrated confidence, and a kill switch. Where payroll data
is unconfirmed the AI gives a range or marks it provisional; it never states a
confident wrong number. And if payroll data quality drops below threshold,
salary calls **suspend automatically** rather than degrade.

**Metrics.** Call **pick-up rate over time** — revealed preference, and the
truest trust signal available. Share choosing human escalation (should fall, then
plateau — never zero; zero means they have given up asking). Unaided recall of
wage terms. Day-90 retention.

---

## Part 4 — Two structural facts that constrain all of the above

Neither of these is a design idea. Both are features of the customer's reality
that decide whether the design is deployable, and both were missing from my first
pass. A senior reviewer would find them before finding anything else.

---

### 4.1 Roughly a third of the workforce isn't on the customer's payroll

By 2015, contract workers made up about **38% of total employment at Indian
manufacturing firms with more than 100 workers**, up from ~20% in 2000. Research
also finds firms use contract labour as **strategic leverage against unionised
regular workers**, to hold bargaining power down. In textile specifically, contract
workers have been described as effectively invisible — with neither industry nor
government keeping proper records.

**On a 100,000-worker customer that is ~38,000 people whose payroll a contractor
holds, not the buyer.**

This does not inconvenience the design. **It breaks the salary wedge for them.**
The AI cannot read out a figure the principal employer does not compute, and the
population it fails is the most precarious one in the building. Every warm claim
about dignity in Part 3 applies least to the people who need it most.

I am not going to pretend that resolves neatly. What it changes:

- **The pilot runs on directly employed workers only**, stated as a limitation up
  front rather than discovered in month three.
- **Contractor payroll data access becomes a contractual precondition for phase
  two** — a commercial term negotiated by the customer with its contractors, not a
  technical problem I can engineer around.
- **Week-one discovery has to establish the contract share and whether that data
  is reachable at all.** If most of the roster is contract labour and their data is
  unreachable, the sequencing in Part 5 is wrong and attendance should go first,
  because gate presence is observable even when payroll is not.

That last point matters more than anything else in this document: it is the one
finding that would make me tear up my own recommended plan.

---

### 4.2 There is a union, and it should be an ally

The Garment and Textile Workers Union is an organised presence in Bengaluru's
garment industry. GATWU reports roughly **4 lakh Karnataka garment workers on
about ₹13,000/month — close to 30% below several other industries** — with wage
revisions unfair for nearly 40 years. Reported gains on harassment, wages and
maternity and overtime enforcement have come **wherever union presence is strong**.
GATWU, with Alternative Law Forum, has documented **forced resignations** in the
sector.

Three consequences:

**The trust rule stops being my preference and becomes a commitment.** "The AI
never delivers termination, discipline, or the rejection of a grievance" now has
an evidence base: forced resignation is a documented practice here. A system that
cannot be pointed at a worker to pressure an exit is a **safeguard**, and it should
be written down where a union can hold the employer to it. Voluntary self-restraint
that no one can enforce is marketing.

**Brief them before launch, not after.** Give the union **aggregate** visibility —
wage-query volumes, grievance counts, resolution times — and never individual-level
data. Aggregate transparency buys legitimacy; individual data would make the system
a surveillance instrument for a second party.

**Their interest and the product's interest coincide.** An AI whose core function
is explaining wages accurately wants what the union wants. That makes them a
distribution channel for trust rather than an obstacle to route around — and
"route around the union" is precisely the instinct that gets a deployment killed
in a Bengaluru cluster.

---

## Part 5 — What ships first

Not all five. Sequence by **trust-yield per unit of integration cost.**

| Phase | Scope | Why here |
|---|---|---|
| **Weeks 0–4** | Salary variance calls. One plant, ~2,000 workers, two languages. | Highest emotional stakes, highest trust yield, and it needs only payroll data the customer already has. No hardware, no gate integration, no content production. |
| **Weeks 4–10** | Onboarding disclosure calls + the verification probe. | Also needs no hardware. Fixes the lie at its source, and feeds the salary explanations downstream. |
| **Weeks 10–20** | Attendance layers and the audit loop. | Needs gate hardware and payroll integration. Slowest and most capex, so it goes after trust exists. |
| **Weeks 20+** | Training library and line-side delivery. | Needs content production. Highest effort, most deferrable. |

**The reason for this order is the whole argument:**

> If the first thing the AI ever does is check whether she showed up, it is a
> surveillance tool. If the first thing it does is explain her money and find her
> a missed ₹200, it is her manager.
>
> **Sequence the rollout so the AI is useful to her before it is useful to them.**

**The condition under which this plan is wrong.** All of the above assumes the
pilot population is directly employed and their wage data is reachable. If week-one
discovery finds most of the roster is contract labour whose payroll sits with
contractors who will not share it, the salary wedge is unavailable and
**attendance goes first instead** — because gate presence is observable even when
payroll is not. Better to state the branch than defend a sequence that assumed its
way past §4.1.

---

## Part 6 — How I would know it worked

**North star — unaided recall.** Sample workers at random and ask them to state
their own wage structure and this month's expected pay, with no prompting. If
that number climbs, the product is working. Everything else is a proxy.

**Business metrics the customer already tracks:** day-30 and day-90 retention,
absenteeism rate, time-to-standard-output, payroll query volume, grievance
escalation rate.

**Guardrail metrics that must not degrade:** share of attendance records needing
human discretion, per-cohort face recognition failure rate, AI-to-human
escalation rate, probe failure rate at onboarding.

**Method:** holdout by plant or by line, never a big-bang rollout. At 100,000
workers there is enough population to run a real control group, and a customer
who sees a controlled result buys the next phase.

---

## Part 7 — What I would refuse to build

Knowing what to say no to is part of the design.

- **No voice-read productivity leaderboards.** Ranking people out loud is
  humiliation at scale.
- **No AI-delivered discipline or termination.** Covered above; it is absolute.
- **No always-on audio capture on the floor.** The moment workers believe they
  are being recorded continuously, every other mechanism here dies.
- **No salary details to an unverified handset.** Non-negotiable, and it follows
  directly from the ownership data.
- **No engagement nudges that exist to populate a dashboard.** If a call does not
  change a decision she is about to make, it should not be placed. Every
  unnecessary call spends trust and lowers pick-up rate — the one metric that
  matters most.
- **No pushed piece-rate comparisons.** Added after this list cost me one of my
  own mechanisms. A daily "you did 340 today, your average is 310" is a
  leaderboard of one, and in an industry with documented speed-up and
  self-exploitation it is pressure dressed as transparency. On request only, never
  comparative, never pushed.

A refusal list is only worth writing if you apply it to your own work. This one
deleted a feature I had described as the biggest productivity lever in the design,
and it should have.

---

## Part 8 — The lines that must survive into the script

Ranked by differentiation. The video has **604 words**; these get priority.

1. Reading is the accommodation. Listening is the baseline.
2. She never composes. She only confirms.
3. Odia speech recognition sits near 35% word error. So open speech never touches
   anything that matters.
4. A number cannot be faked by nodding. *(Comprehension by arithmetic, not
   agreement — and the reason the confirm-only rule needs an exception.)*
5. The work destroys the fingerprint. Biometrics fail hardest on exactly the workers
   who most need attendance to be right.
6. **Never the average.** *(Declining to recommend a modality you haven't measured
   is the most senior line available.)*
7. The phone is often not hers. Reading her salary to whoever answers is a harm.
8. She does not want her payslip. She wants to know why this month is different.
9. PF is her money, in her name. One sentence between savings and theft.
10. An AI that only enforces is a supervisor. An AI that advocates is a manager.
11. **Thirty-eight percent are contract labour, and for them I can't explain their
    wages at all.** *(Naming the hole in your own design.)*
12. Make it useful to her before it is useful to them.

Lines 4, 6 and 11 are new in v2. All three exist because the first draft was wrong
about something, and all three land as credibility rather than as hedging.
