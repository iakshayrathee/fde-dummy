# One-page cheat sheet — Hunar.AI FDE final round

The only doc you reread in the 30 minutes before the call. Everything else (08/09/10)
is reference. Goal: **principles you can improvise from, not scripts you recite.**

> Any term below you can't explain simply → `12-plain-language-glossary.md` (plain
> meaning + analogy for every technical word in this pack).

---

## STEP 0 — Lock your knowled.ai line (do this first, it governs everything)

Pick the ONE that is **true**, and say only that. Overreaching here is the single
biggest way to lose this round.

- **A — Employee/contractor, real schools used it in production:**
  "I built [product] at knowled.ai; it was used by [N] schools / [N] educators."
  → You may say "in production, with real users." Have one real teacher/school you
  could name.
- **B — I built it (solo/founder/contract), piloted with some real schools/teachers:**
  "I built it end-to-end and piloted it with [N] schools/teachers." → Say "pilot," not
  "production at scale." Cite the pilot honestly.
- **C — Solo build, limited/no real deployment yet:**
  "I built it end-to-end as a working product; it's pilot-stage." → Lead with the
  *engineering decisions*, not user counts. Do **not** claim school/teacher fieldwork
  you didn't do.

**Rule:** only tell a customer-discovery anecdote (a teacher said X → I built Y) if it
literally happened. If it didn't, talk about the *constraint* you designed for
("children can't type, so PIN login"), which is true from the code regardless.

---

## The 60-second "about me" (say it out loud, on a timer, twice)

> "I'm Akshay. Most recently, knowled.ai — AI for special education under India's
> inclusive-ed mandate. I built [STEP-0 LINE]: the whole stack — schema, APIs, a
> separate Python AI service, the frontends. Two things from it are why Hunar pulls at
> me. One, none of my users could be assumed to read — four-year-olds log in with a
> 4-digit PIN, IEP docs are read aloud by text-to-speech. Two, the AI never got the
> last word — every AI-drafted goal needed a human's approval. Frontline non-literate
> workers reached by voice is the same problem at a new edge — which is why I picked
> challenge 3. When I saw it, it wasn't a stretch; it was the problem I'd been
> circling." → stop.

---

## 3 flagship code decisions (your technical spine — all true, all defensible)

1. **Deterministic core, LLM at the edge.** In the screening tool, the risk *tier* is
   set by pure weighted-math rules (`scoring.service.ts`); the LLM runs *after* and only
   *explains* it (`tier_rationale.py`: a pure-Python `analyse_scores` node feeds the LLM
   nodes). → "A model never decides something consequential about a person; math does,
   AI phrases it. That's the boundary I'd hold for a voice HR agent."
   *(Plain: fixed math — like a calculator — decides the risk level; the AI just writes
   the explanation. So the serious decision is predictable, not an AI guess.)*
2. **Offline-first resilience.** The literacy app's `attempt-queue.ts`: UUID idempotency,
   localStorage persistence, exponential-backoff retry, `sendBeacon` on tab close,
   flush-on-reconnect. → "A classroom's wifi drops; a worker's on 2G in a basement. Same
   problem. Nothing is lost."
   *(Plain: the app keeps the child's answers on the device when the internet drops,
   gives each a unique ID so it can't be saved twice, and keeps retrying — waiting a bit
   longer each time — until it's safely sent.)*
3. **Explainable over clever.** The adaptive engine is rule-based, not ML — mastery =
   ≥80% accuracy AND ≤4s AND <20% confusion errors; every change returns a `reason`.
   → "Cold-start, explainable to a teacher, testable. I chose the simple correct thing
   first, not because I couldn't do ML."
   *(Plain: I used clear rules, not a black-box AI, to decide when to make the game
   harder — so I could tell a teacher exactly why it changed, and because on day one I
   had no data to train an AI on anyway.)*

Plus the recurring one: **human override, but with a required justification** (educator
can override the AI tier only by typing why).

---

## 5 stats — memorize, say "around," never invent precision

- Odia ASR **~35%** WER vs Hindi **~16%** — this drives the whole architecture.
- Phone ownership **~38%** women / **~71%** men — why you can't assume a smartphone.
- Contract labour **~38%** — the fact that broke your own salary wedge (own it).
- Karnataka garment wage **~₹13,000/mo**.
- Biometric failure **~6.5%** national / **~36%** worn-fingerprint (Telangana).
- (Own as invented: the ₹8k replacement cost and 55% answer-rate — say so if pressed.)

---

## Who's in the room

- **Krishna Khandelwal (CEO)** — ex-Locus (logistics, business side). Fieldwork
  evangelist; "80% of HR is calling." Talk ground truth, payroll desk, week-one.
- **Dr Shantanu Bhattacharyya (CTO)** — CMU PhD, ex-Locus Chief Data Scientist.
  Scientist. Talk WER, disaggregated metrics, holdout design, "measure at the gate."
- Hunar: ~5 lakh calls/day, ARR ~$3–4M; Swiggy/Zepto/Bajaj/Starbucks; ElevenLabs +
  Cartesia; hybrid voice architecture; pivoted voice-native 2024.

---

## Killer questions → one-line answers

- **"Did you use AI to build this?"** → "Yes, as a tool — like any FDE would. The
  judgment is mine: which challenge, running a second research pass, catching that
  contract labour breaks my own plan, deciding what to refuse to build."
- **"Was it solo? / Was it a real job?"** → your STEP-0 line, exactly. No embellishment.
- **"How does it scale to our volume?"** → "Right primitives — queues, idempotency,
  failure isolation. But pilot-scale, not 5 lakh/day. I'd want to learn where *your*
  system bends, not pretend mine has."
- **"Why leave knowled.ai?"** → [your real, forward-looking reason]. Never trash it.
- **"Why not challenge #1, given we're ex-logistics?"** → "#1 rewards imagination; #3
  rewards homework. For a company that did two years of fieldwork before code, I bet
  homework was the higher-signal choice. Happy to riff on #1 though — the interesting
  bit is it's the one case where AI holds authority *over* a person, so the rule is: it
  can advocate, never discipline."
- **"You've never worked a factory floor."** → "Correct. I won't pretend research
  substitutes for a shift change. Week one I'd sit on the payroll desk and ride the 6am
  gate. That's why I wrote a discovery plan, not a feature list."

---

## 3 questions to ask them (open with #1)

1. "When you ran the recruitment agency, what did you believe going in that turned out
   flat wrong on the ground?"
2. "On a live deployment, what stalls a pilot most — integration, supervisor adoption,
   or the customer's own data quality?"
3. "Where does the product hand off to a human today — chosen deliberately, or learned
   the hard way?"

---

## Leave them believing 3 things

1. **You reason from ground truth, not the demo** (picked the homework prompt; found the
   hole in your own plan).
2. **You've already built for non-readers with a human in the loop** (PIN login, TTS,
   approve/reject, override-with-reason).
3. **You have the temperament**: "I was wrong," "I don't know — I'll find out," "here's
   what I'd measure."

---

## Do-not-do list

- Don't inflate scale or invent users. Don't recite — improvise from principles.
- Don't claim fieldwork that didn't happen. Don't answer comp/logistics questions first.
- Don't leave your GitHub public with seeded creds if you'll be asked to share it.
- Don't ramble after your point lands — finish and hold the silence.
