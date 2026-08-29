# Q&A prep — the follow-ups that actually come

Ordered roughly by likelihood × difficulty. Answers are notes to speak from, not
scripts to read.

---

## A. The commercial questions

### A1. "What does this cost to run at 100,000 workers?"

Do the arithmetic out loud. It is the single fastest way to look like an engineer
rather than a designer.

> **Corrected model.** My first version used ₹2.5/min blended and priced only the
> AI. Both were wrong. ₹2.5 is the Indian *self-serve floor* — production
> deployments land far higher once every component is billed — and I had promised a
> named human on every call and then never costed the headcount. Revised below.

**Step 1 — connected minutes per month:**

| Flow | Calls | Avg | Minutes |
|---|---|---|---|
| Payday salary call | 100,000 | 90s | 150,000 |
| Mid-month variance alert (~30% material variance) | 30,000 | 45s | 22,500 |
| Unplanned absence (capped 2/worker/mo, ~1.2 actual) | 120,000 | 30s | 60,000 |
| Gate-override verification (~3% of worker-days) | 75,000 | 20s | 25,000 |
| Onboarding disclosure (~5,000 joiners) | 5,000 | 6 min | 30,000 |
| | **330,000** | | **~288,000** |

**Step 2 — attempt overhead, which I originally ignored.** You pay for ringing,
not just for talking. At an assumed **55% answer rate**, 330,000 connections need
~600,000 attempts. The 270,000 failures ring ~15s each: **+67,500 min.**

**Billed total ≈ 356,000 min/month.**

**Step 3 — price it.** Indian voice AI starts near ₹2/min self-serve and runs to
₹12 with the fees nobody quotes; global production deployments cluster around
$0.12–0.25/min fully loaded. Use **₹6/min central, ₹4–8 sensitivity:**

- **₹21.4 lakh/month → ~₹2.6 crore/year** (range ₹1.7–3.4 crore)

**Step 4 — price the humans I promised.** At 8% escalation, that's 26,400 human
interactions/month, ~8 min each = 3,520 hours = **~25 FTE**. At ₹30,000/month
loaded: **~₹0.9 crore/year.** Much of this is likely *redeployment* of the existing
payroll query desk rather than net-new headcount — but I should not assume that for
free.

**All-in ≈ ₹3.5 crore/year → ~₹350 per worker per year.**

**Frame it against her wage.** On ₹13,000/month, a working day is roughly ₹500. The
entire system costs **under one day of her wages, per year.**

**Then frame the return as breakeven, not as a multiple.** My first version claimed
5x ROI off two numbers I invented. Better:

> At ₹3.5 crore/year and an assumed ₹8,000 to replace one worker, this has to
> prevent about **4,300 departures a year — roughly 4 attrition points out of
> 100,000 workers — to break even.**

That is a falsifiable claim they can check against their own attrition. It also
tells them exactly what to measure. Say plainly: the ₹8,000 replacement cost and
the 55% answer rate are the two assumptions I'd replace with their actuals in week
one, and **answer rate is the largest single sensitivity in the model** — at 40%
answer, telephony overhead alone adds roughly another ₹0.5 crore.

### A2. "Who buys this, and why? Your design advocates for the worker, but the employer pays."

The tension is real, so name it rather than dodge it.

The buyer is the CHRO or plant head whose problem is attrition, absenteeism and
production stoppage — not the payroll clerk who benefits from confusion. For that
buyer, worker advocacy and employer interest point the same direction: a worker
who understands her pay stays longer and escalates less.

Where they genuinely diverge — an employer who wants opacity — see A3.

### A3. "What if the employer doesn't *want* wage transparency?" — the hardest question

Four-part answer:

1. **For a compliant employer, transparency is free.** If payroll is correct,
   explaining it costs nothing and buys retention.
2. **Resistance is diagnostic.** An employer who refuses to explain wage variance
   is telling you their payroll is wrong. Better to learn that in week one than
   month four. As an FDE I'd want that signal early and I'd surface it to my own
   leadership, not paper over it.
3. **Sequence around it.** Lead with *legitimate* variance — absence, overtime,
   PF, canteen — which no employer objects to. Do not open with "we'll expose your
   errors." Legitimate variance is most of the volume anyway.
4. **The commercial argument is downside risk.** The April 2026 Noida protests
   started partly over payslips not matching hours worked and ended in production
   stoppage across sector belts. Opacity has a tail. That reframes transparency
   as risk management, which is a budget line that already exists.

And the honest bottom line: an employer who fundamentally requires opacity isn't
the customer for this module. Qualify them out early rather than fail slowly.

### A4. "How is this different from what Hunar already does?"

Say the true thing: a lot of it isn't different, and that's deliberate. Hunar
already runs outbound multilingual voice agents across hiring, onboarding,
training and engagement. I'm not going to pitch them their own product as novel.

What I'd argue is additive:
- **salary-delta explanation as the wedge use case**, ahead of everything else
- **the shared-handset identity and privacy gate** before any pay figure is spoken
- **the attendance audit loop** that makes supervisor discretion visible
- **the monthly advocacy behaviour** — proactively finding money in her favour
- **unaided recall as the north-star metric**, in place of completion or engagement

---

### A5. "A third of your workers aren't on this employer's payroll. Doesn't that kill your plan?"

For those workers, yes — and I'd rather say so than be caught by it.

Contract workers were about **38% of employment at Indian manufacturing firms with
more than 100 workers** by 2015, up from ~20% in 2000. On this customer that's
~38,000 people whose payroll a contractor holds. The AI cannot read out a figure the
principal employer does not compute. **The salary wedge does not reach them, and
they are the most precarious population in the building.**

Three things follow, and none of them is a clever workaround:

1. **The pilot is scoped to directly employed workers**, stated as a limitation up
   front.
2. **Contractor payroll data access becomes a contractual precondition for phase
   two** — a commercial term the customer negotiates with its contractors, not
   something I can engineer around.
3. **If week-one discovery finds most of the roster is contract labour and the data
   is unreachable, my recommended sequence is wrong and attendance goes first** —
   because gate presence is observable even when payroll isn't.

Also worth naming, because it explains why the data is hard to get: research finds
firms use contract labour partly as leverage against unionised regular workers. The
opacity isn't accidental, which means data access is a negotiation, not an
integration ticket.

---

## B. The technical challenges

### B1. "If Odia ASR is 35% WER, doesn't that break your entire design?"

This is the best question in the set and it's actually the proof of the design.

WER measures **open transcription**. Almost nothing in this design requires open
transcription. Distinguishing "हाँ" from "नहीं", or recognising a single digit, is
a small closed-set classification problem with accuracy far above open-vocabulary
transcription. That's exactly why the rule is *she only confirms*.

Two supporting points: the benchmark literature itself notes that strict
single-reference WER overstates degradation relative to what users perceive, and
open speech is permitted in my design in precisely one place — next-day training
recall — where a recognition error costs nothing.

So the 35% figure isn't an obstacle I'm working around. It's the constraint that
produced the architecture.

### B2. "Voiceprint verification — reliable? Spoofable?"

Not reliable enough to be the only gate, and yes, spoofable by a family member
with a recording. So it isn't load-bearing alone. Layers:

- voiceprint as a *first* check, cheap and passive
- a short spoken or keyed PIN chosen at onboarding for anything sensitive
- **the shared-phone flag from onboarding overrides everything** — if she said the
  handset is shared, salary is never pushed to it at all
- on failure, the AI degrades to a content-free message: "I have information about
  your work, please call back from somewhere private"

The design goal isn't perfect authentication. It's that **a failed check never
leaks a number.**

### B3. "How many languages, and how do you handle dialects?"

Two different questions, and my first answer conflated them.

**Which languages to build** comes from the HR roster — the top 4–5 that cover the
plant. That's a capacity-planning input.

**Which language *she* speaks** never comes from the roster, because the premise of
this whole design is that her record is wrong about her. It's detected from the
first ten seconds of speech, and the roster is allowed to be wrong without
consequence. Dialect is stored *separately* from language, because state-of-the-art
Indic models degrade on low-resource varieties even when closely related to their
pretraining languages.

If detection surfaces a language the roster didn't predict, that's not an error —
it's a finding, and it should raise a flag for the HR data owner.

Practical mitigations: keep consequential vocabulary closed and short, use a
peer's recorded voice from her own language group for training content instead of
TTS, and route to a human when confidence is low rather than guessing.

### B4. "What breaks first in production?"

**Payroll data quality**, not the voice stack. The AI can only explain what
payroll can compute. If piece-rate output lands late, or overtime is keyed
inconsistently across plants, the calls become confidently wrong — and one
confidently wrong salary figure destroys more trust than fifty correct ones build.

Hence the kill switch: if payroll data quality drops below threshold, salary calls
**suspend** rather than degrade. Silence is recoverable. A wrong number spoken
with confidence is not.

### B5. "Won't nobody pick up? Unknown numbers get ignored."

Right, and pick-up rate is my primary trust metric precisely because it's revealed
preference. Countermeasures:

- her supervisor introduces the first call **in person** — borrowed authority
- one consistent, verified caller ID, never a rotating pool
- call window chosen by her at onboarding, asked once
- **never call without a reason.** Every pointless call spends trust. This is why
  I refuse to build engagement nudges that exist to fill a dashboard.

If pick-up trends down, the product is wrong, not the worker.

### B6. "Doesn't the attendance audit loop just create call volume nobody answers?"

It's ~75,000 twenty-second calls a month by my estimate, and it's the cheapest
flow in the system. But the volume isn't the point — the *deterrent* is. A
supervisor who knows every override gets verified with the worker behaves
differently even if she never picks up. And a falling override rate is the metric
I actually want, which means success looks like this flow shrinking over time.

---

### B7. "You ruled out fingerprints. So what do you use instead?"

I don't answer that from here, and declining is the point.

NIST's FRVT work documents demographic differentials in face recognition that
**vary substantially between algorithms**, with false non-match rates driven largely
by image quality and ageing. A 6am shift change in poor light, with headscarves, is
close to a worst case for image quality. Picking a modality from a datasheet under
those conditions is how you end up with a system that quietly fails one cohort and
takes a day's pay off them each time.

So the deliverable is a **selection procedure**, not a product name:

- instrument the gate for two weeks
- measure false non-match rate **disaggregated by cohort and shift hour** — never
  report the average
- choose on measured performance
- guarantee a non-biometric path regardless of which option wins
- treat a rising per-cohort rate as a **system defect under SLA**, not worker error

What I'll commit to before measuring: **not fingerprint**, because the failure
mechanism is already established, and **never a single modality alone** — whatever
wins gets paired with a badge tap.

> **Own the correction if it comes up:** an earlier draft of mine demolished
> fingerprints with hard numbers and then endorsed face recognition on assertion.
> That was using evidence to kill the option I didn't want and rhetoric to justify
> the one I did. I'd rather be caught correcting it than defending it.

---

## C. The ethics challenges

### C1. "How do you know she actually understood, rather than just agreed?"

She confirms by computing, not by agreeing:

> *"If you take two days off next month, how much less will you get?"*

If the number is right, comprehension is real. Wrong or absent, a human redoes the
disclosure in person.

Three reasons it works, all falling out of the constraints. Numerals are the most
reliable class in Indian-language ASR, so recognition isn't the weak link.
**Numeracy substantially outruns literacy** here, so the question is answerable by
someone who can't read a word of it. And a number **cannot be produced by nodding**
— it is the one answer acquiescence can't fake.

> **If they ask what I considered first:** an earlier version had the AI state one
> term *wrongly* on purpose, to see whether she'd correct it — an attention check
> borrowed from survey research. I killed it. If the recording is the contract
> artifact, deliberately misstating a material term puts a false statement inside a
> legally operative document during contract formation. Survey attention checks
> don't live inside contracts. The numeric check gets the same signal with none of
> the exposure, and it's a better test anyway: a wrong number is unambiguous,
> whereas a failure to correct could just be politeness.

Volunteering that trade-off is worth more than defending the original would have
been.

### C1b. "Your confirm-only rule sounds like it manufactures consent."

Correct, and that's why the rule is two-tier. A design whose only verb is "yes,"
aimed at someone who already agrees with authority, industrialises acquiescence.

So: **confirmation for information delivery and routine operations; production of a
number for consent and anything legally operative.** Collapsing those two into one
mechanism was the flaw in my first draft.

### C2. "Recording every call — consent, DPDP, data retention?"

Consent to recording is part of the onboarding disclosure, with purpose stated in
her language. Pay data is sensitive personal data, which is independently why the
verification gate exists. Recordings need a defined retention window and
purpose limitation rather than indefinite storage.

I'd flag clearly that I'd run the specifics past counsel rather than claim
regulatory expertise. What I *can* commit to is the design posture: minimum data,
stated purpose, retrievable by the worker herself, and no secondary use.

### C3. "Isn't an AI managing people just automated surveillance with a friendly voice?"

It can be, and the rollout order is what decides which one you've built. That's
the whole argument in the close: if the first thing the AI ever does is check
whether she showed up, it's surveillance. If the first thing it does is find her a
missing ₹340, it's a manager.

Backed by hard limits: no voice-read productivity leaderboards, no AI-delivered
discipline or termination, no always-on floor audio, and a named human exit on
every single call.

### C4. "What about the supervisor whose discretion you just audited? He'll resist."

He will, and he's the actual adoption risk — not the workers. Mitigations:

- the audit loop reduces *his* liability too; documented overrides protect him
  from accusations as much as they constrain him
- gate self-repair (auto re-enrolment after three failures) removes work from his
  day rather than adding it
- he keeps the authority that matters: he's the named human on escalation, and he
  introduces the AI to his line

If supervisors are hostile, the pilot fails regardless of how good the design is.
So in week one I'd interview supervisors **separately from workers**, and treat
supervisor buy-in as a deliverable, not a formality.

---

### C5. "There's an active union in these clusters. Do you go through them or around them?"

Through them, and not out of politeness — out of self-interest.

GATWU is organised in Bengaluru's garment industry and reports roughly 4 lakh
Karnataka garment workers on about ₹13,000/month, close to 30% below other
industries. Reported gains on harassment, wages, and maternity and overtime
enforcement have come **wherever union presence is strong.** So the union is already
doing the thing my product claims to do, with more legitimacy than any product will
have on day one.

Three commitments:

- **Brief them before launch, not after.** A wage-communication system that arrives
  unannounced in a unionised cluster gets read as a management instrument, and that
  reading is hard to reverse.
- **Aggregate visibility, never individual.** Wage-query volumes, grievance counts,
  resolution times — yes. Worker-level data — never. Aggregate transparency buys
  legitimacy; individual data would make the system a surveillance tool for a second
  party.
- **Put the termination rule in writing where they can hold the employer to it.**
  GATWU with Alternative Law Forum has documented forced resignations in this
  sector. That is exactly why "the AI never delivers termination, discipline, or the
  rejection of a grievance" exists. Self-restraint nobody can enforce is marketing;
  a written commitment a union can cite is a safeguard.

And the honest strategic read: an AI whose core job is explaining wages accurately
wants what the union wants. Routing around them would be both wrong and stupid.

---

## D. The role questions

### D1. "Why did you pick this challenge?"

Short version: #1 rewards imagination, #3 rewards homework. The delivery brief
grants explicit licence to speculate on the driver-manager prompt, which means a
vivid answer can be thin. #3 hands you a population and dares you to know
something real about them.

For a company that ran an actual recruitment agency for two years before writing
software, demonstrating fieldwork instinct seemed like the higher-signal choice.

Don't oversell it — if they push, concede #1 has the higher ceiling and say why
you took the trade.

### D2. "What would you actually do in week one on this account?"

The most important question in the set. Be specific:

1. **Establish the contract-labour share first**, because it's the only finding that
   can invalidate my whole plan. What percentage of the roster is on contractor
   payrolls, and is that wage data reachable at all? If the answer is "most, and no,"
   the sequence flips to attendance and I need to know that on day one, not day ninety.
2. **Sit on the payroll query desk for two days** and log every question verbatim.
   That log is the requirements document.
3. **Pull one month of payroll data** and compute the variance distribution: what
   share of workers see a month-over-month change above ₹300, and what drives it.
   That tells me whether the wedge is real or whether I'm wrong.
4. **Ride one shift change at the gate** and count recognition failures myself
   rather than trusting a vendor spec sheet — disaggregated, not averaged.
5. **Interview ten workers in their own language**, and three supervisors
   **separately**, because supervisor buy-in is the actual adoption risk.
6. **Ask for the grievance log and the exit-interview reasons.** Attrition causes are
   usually already written down and unread.
7. **Ask who the union contact is**, and whether anyone has spoken to them.

End-of-week deliverable: the contract-labour share, the top five recurring worker
questions, the variance distribution, and a one-page pilot spec with a holdout group
defined.

### D3. "What's the weakest part of your answer?"

Have this ready; refusing to answer it is worse than any weakness.

Four real ones:

- **I have no primary research.** Everything is secondary sources. The comprehension
  check and the attendance audit loop came from reasoning, not from watching a shift
  change. Both could die on contact with a plant floor.
- **Contract labour is an unsolved hole, not a solved problem.** ~38% of workers at
  large Indian factories sit on contractor payrolls. For them my centrepiece
  mechanism simply does not function, and they're the most vulnerable people in the
  building. I have a discovery plan and a fallback sequence, not an answer.
- **The economics rest on two invented numbers** — a ₹8,000 replacement cost and a
  55% answer rate. Answer rate is the largest sensitivity in the whole model and I
  could not find data for this population.
- **I still can't find shared-handset rates specific to garment factories**, or
  published day-30 attrition for Indian apparel. I extrapolated from national
  gender-gap data, which remains a genuine weakness.

**And one process weakness worth admitting:** the first version of my own video
script ran 5:35 against a 5-minute cap while claiming 4:56, because I asserted a
word count instead of counting. I found it by auditing my own work. That's the habit
I'd want on an account — but it should have been the first check, not a later one.

### D4. "What would you cut if you had one engineer and one month?"

The payday delta call, one plant, two languages, no attendance, no training, no
onboarding. Read the delta, offer a repeat, offer a human. Measure pick-up rate
and unaided recall against a holdout line.

Everything else in the design is an argument for what comes *after* that works.

---

## E. Questions to ask them

Ask two or three. They signal what you'd be like on an account.

1. When you ran the recruitment agency, what did you believe going in that turned
   out to be wrong on the ground?
2. On a live deployment, what's the most common reason a pilot stalls —
   integration, supervisor adoption, or the customer's own data quality?
3. Where does your product currently hand off to a human, and was that boundary
   chosen deliberately or discovered?
4. How much of an FDE's time here is customer conversation versus configuration?

---

## F. The three lines to land no matter what

If the conversation goes sideways, get these said:

1. **Reading is the accommodation. Listening is the baseline.**
2. **She never produces. She only confirms** — because Odia ASR is wrong a third
   of the time, so consequential steps have to be classification, not transcription.
3. **Make it useful to her before it's useful to them.**
