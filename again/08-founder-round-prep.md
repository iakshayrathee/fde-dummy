# Founder round prep — Akshay Rathee · FDE · Hunar.AI

Final round. Likely with **Krishna Khandelwal (CEO)** and/or **Dr Shantanu
Bhattacharyya (CTO)**. This round is **not** about the design — the video and
one-pager already made that case, and `07-qa-prep.md` covers every technical,
commercial and ethical follow-up. This round is about **you**: your background,
your previous work, and *how you actually arrived at this submission*.

> Companion docs: design in `03-design-doc.md`, the full product/tech/ethics Q&A in
> `07-qa-prep.md`. This file is the **person and process** layer. Don't duplicate —
> when a design question comes up, answer briefly and point yourself back to `07`.
>
> **Any technical word you're unsure of** (ASR, WER, hybrid voice architecture, TTS,
> DPDP…) is explained in plain language with an analogy in `12-plain-language-glossary.md`.

---

## 0. What this round is really testing

A cleared submission means the *idea* passed. A founder round exists to answer four
questions they will not ask out loud:

1. **Is this person real?** Did they actually reason their way here, or did they
   produce a slick artifact they can't defend when pushed off-script?
2. **Will they survive being embedded at a customer?** FDE = alone at a factory,
   ambiguity everywhere, the customer's data is a mess, the supervisor is hostile,
   and you have to make a call. Do they have the temperament?
3. **Do they have judgment, not just intelligence?** Can they say "I was wrong,"
   "I don't know," and "here's what I'd measure" — the three sentences that separate
   a deployable engineer from a clever one.
4. **Do they actually want *this* problem?** Frontline India, blue-collar, voice,
   unglamorous fieldwork — or do they just want an AI job?

Everything below is aimed at those four. **The single highest-leverage move in this
round is to tell the truth, including about your own mistakes.** It happens to also
be your strongest card, because your process was full of self-correction — see §4.

---

## 1. Know the company cold (so you sound like you already work there)

Speak about Hunar as someone who has read it closely, not skimmed it.

- **What it is.** Multilingual conversational **voice AI** for India's frontline /
  blue-collar workforce — "AI HRs." Covers hiring, screening, onboarding, training,
  engagement, retention. The product **calls people**; there is no chat window.
- **Scale.** ~**5 lakh calls/day**, among India's largest voice AI by call volume.
  Average call **over 3 minutes** — deliberately the *hard*, high-fidelity
  conversations, not sub-30-second EMI-reminder bots.
- **Customers.** Swiggy, Zepto, Aditya Birla Capital, Bajaj Finserv, Croma,
  Dr Lal PathLabs, 1mg, Starbucks. Six sectors: q-commerce/e-commerce, supply
  chain & logistics, retail & QSR, healthcare diagnostics, BFSI, construction &
  manufacturing.
- **The origin story that matters most.** They ran an **actual recruitment agency
  for ~2 years** before building software, and recorded **40–50 lakh minutes** of
  real workforce conversations. That dataset became the product. **This company's
  entire identity is fieldwork-before-code.** Your whole submission was built to
  respect that — say so.
- **Tech, in case the CTO probes.** A **hybrid voice architecture**: raw audio goes
  through a proprietary "Dynamic Config Generator" that strips filler/acknowledgements
  and detects contextual pauses *before* inference, preserving tonality, interruptions
  and modulation rather than flattening to text first. An "Audio Regenerative Model"
  reconstructs context after interruptions instead of restarting. They **switch TTS
  providers dynamically** (ElevenLabs, Cartesia, others) by regional-language
  performance — strong in Telugu, Kannada, Tamil. Models from Google/OpenAI, plus
  open-source models trained on their proprietary data. Pivoted voice-native in 2024
  once real-time audio models matured.
- **Pricing.** Function-based, not infra-based: they charge per *workflow*
  (screening ₹15–20, onboarding/assessment ₹75–100), not per minute. **Note how this
  differs from your own per-minute cost model in `07` §A1** — if cost comes up, you
  can say you modelled it bottom-up per-minute but their outcome-based pricing is the
  smarter commercial frame, and ask how they landed on it.
- **ARR** ~$3–4M, closing another round. Registered as **Bluejay WorkTech Pvt Ltd**.
  ~51–200 on LinkedIn (small, so an FDE is a big hire — you'd be close to the founders).

### The founders — who you're talking to

- **Krishna Khandelwal (CEO).** Business/commercial founder. Led the business team
  at **Locus** (logistics optimisation). His line — *"80% of an HR's job is calling"*
  — is the company thesis. He is the fieldwork evangelist. **He will respond to
  fieldwork instinct and commercial clarity.** Talk to him about the payroll query
  desk, the shift-change count, the CHRO's budget line, week-one discovery.
- **Dr Shantanu Bhattacharyya (CTO).** PhD from Carnegie Mellon; biophysics,
  structural biology, computational immunology; was **Chief Data Scientist at Locus**,
  where he met Krishna. **A scientist.** He will respond to rigor: the ASR WER
  argument, closed-set vs open-vocabulary, disaggregated metrics vs averages, holdout
  design, "measure at the gate, don't trust the datasheet." Your `07` §B answers are
  built for him.
- **Both are ex-Locus — a logistics company.** This is directly relevant, see §6.

---

## 2. Your story — the 90-second version

You will be asked some form of *"tell me about yourself"* / *"walk me through your
background."* Have a tight arc ready. This version is built from your **actual
shipped work** (§2.1). Only the bracketed items are still yours to fill.

> I'm Akshay. Most recently I was at **knowled.ai**, an AI special-education platform
> for India's inclusive-education mandate. I built it end-to-end myself — schema,
> backend, a separate Python AI service, the frontends, the deploys — working directly
> with special educators and school leaders rather than from a spec. Across three
> products: the
> core **IEP and assessment platform** — six roles, from special educator up to
> school leadership, with an approval workflow where a senior educator signs off every
> AI-generated goal; a **mass-screening system** that runs whole grades through five
> domains and tiers them, with eight LangGraph agents doing the rationale, anomaly
> detection and escalation notes; and a **gamified literacy platform** for four-to-six
> year-olds with an adaptive difficulty engine and ten game templates.
>
> Two things from that work are why Hunar's problem pulls at me.
>
> First, **none of my users could be assumed to read.** On the literacy platform
> children log in with a **four-digit PIN — no email, no password**, because they
> can't type one. On the IEP platform I shipped a **text-to-speech module** so
> documents could be *heard* instead of read. That's the same instinct as my
> submission: reading is the accommodation, listening is the baseline.
>
> Second, **the AI never got the last word.** Every AI-generated IEP goal needed a
> human educator's approval. In the screening tool the educator can override the
> AI's tier — but has to type a justification. That boundary is the product, not a
> safety bolt-on.
>
> Hunar is the same shape of problem at a different edge of the population —
> frontline workers, many non-literate, reached by voice. When I saw the FDE
> challenge, #3 wasn't a stretch. It was the problem I'd been circling.

Then stop. Let them pull the thread they care about.

**Still to fill in before the call:**
- [ ] Your exact title and dates at knowled.ai, and anything before it.
- [ ] Scale numbers if you have them: how many schools / educators / children
      actually used these in production? (Huge credibility lift — "85% complete,
      pilot" is fine and honest; a real user count is better.)
- [ ] Your education / how you got into this.
- [ ] Whether you were customer-facing (sat with educators, ran the pilot, trained
      users) — **FDE gold if yes, say it explicitly and unprompted.**
- [ ] Why you're moving on from knowled.ai (see §5).

### 2.1 Your knowled.ai portfolio — the three projects, with the detail that lands

Know these cold. When they ask "what did you actually build," you want specifics, not
adjectives. Lead with the *design decision*, not the tech stack — but have the stack
ready because the CTO will ask.

**1. Knowled Special Education Platform** — `assessment-tool` ·
[live](https://assessment-tool-chi.vercel.app) · Oct 2025 → Jul 2026, your largest codebase

- **Six roles, real hierarchy:** Admin, Center, Special Educator, Super Special
  Educator, Parent, School Viewer. Each with a distinct dashboard and permission set.
- **The approval workflow is the spine:** a special educator creates an assessment or
  IEP goal → a *super* special educator reviews, approves, or **rejects with
  feedback**. Plus a **flagged-cases** queue for cases needing senior attention.
  This is your human-in-the-loop proof.
- **Text-to-speech module** — TTS controls, document viewer, document search, a
  `useSpeechSynthesis` hook. **Say this out loud in the interview.** You shipped
  listen-instead-of-read before you ever wrote the submission.
- **Compliance built in, not bolted on:** an `AuditLog` model capturing user and IP
  per action, DPDP/FERPA posture, **RCI certification tracking** with validity and
  renewal dates (the Rehabilitation Council of India — a genuinely India-specific
  regulatory detail), and primary/secondary language tracking per student.
- **Depth of the assessment work:** separate reading, writing and math skill
  assessments (the writing one is the single biggest component in the repo), formal
  assessment batteries, concept-to-performance mapping, grade-level mapping.
- **Full planning hierarchy:** long-term plan → short-term plan → weekly lesson plan
  → homework, all linked to IEP goals.
- **Report snapshots** at parent, school and center level — plus an AI report service
  that is the largest service file in the backend.
- **Stack:** Next.js 14 App Router, TypeScript, TanStack Query, Zustand, Tailwind +
  Radix/shadcn, React Hook Form + Zod · Node/Express + TypeScript, PostgreSQL +
  Prisma, JWT with RBAC, S3 for documents, WebSockets for live notifications.
- **Evidence it's real, not a demo:** ~20 sequential migrations from Sept 2025 to Feb
  2026 with names like `make_parent_optional`, `add_approval_system`,
  `add_school_assignments`, `add_center_report_snapshots`. That migration history *is*
  your story of a product meeting reality — use it if someone doubts this shipped.

**2. Mass Assessment System** — `mass-assessment` ·
[live](https://mass-assessment.vercel.app) · Feb 2026

- **The problem:** screen an entire grade, not one child at a time. Students are
  scored across five domains (reading, comprehension, spelling, numeracy, writing),
  weighted, and auto-placed into **Tier 1 / 2 / 3** risk bands.
- **The human-in-the-loop decision:** the educator **can override the AI's tier — but
  must supply a justification.** Same design instinct as your "she must produce a
  number, not just say yes": make the human do one irreducible act of real input.
- **Eight LangGraph agents**, each with a job: tier rationale in plain English,
  statistical anomaly detection across a session, class report generation, escalation
  /referral notes, a streaming educator assistant with Redis-backed memory, PDF/DOCX
  document extraction, answer scoring, observation-based suggestions.
- **Three-service architecture:** Next.js frontend → Express/TypeScript backend →
  **FastAPI Python AI service**. Redis for Bull job queues *and* chat memory, so the
  slow AI work is async and never blocks the educator entering scores.
- **Stack extras worth naming to the CTO:** LangGraph + LangChain, GPT-4o-mini,
  **LangSmith for tracing**, Neon serverless Postgres, PDFKit, deployed across
  Render + Vercel.
- **Why this one matters most for Hunar:** it is a **multi-agent system with
  observability, queues and a human override path** — architecturally the closest
  thing in your portfolio to what Hunar runs.

**3. Gamified Literacy Platform** — `gamified-ai` ·
[live](https://gamified-ai.vercel.app) · Dec 2025 → Jan 2026

- **Users are 4–6 year olds** (Nursery/LKG/UKG) — pre-literate by definition.
- **The auth decision:** children log in with a **4-digit PIN. No email, no
  password.** Teachers and admins use email/password. You solved "credentials for
  someone who can't read or type" a year before the challenge asked you to.
- **Interface for non-readers:** 60px+ touch targets, audio prompts, an
  **audio-to-letter phonics game** where the child hears a sound and picks the
  letter — voice as input channel, not decoration.
- **Adaptive difficulty engine you wrote yourself:** looks at accuracy over the last
  five attempts, average response time, and error patterns. Mastery is defined
  concretely — **80% accuracy under 4 seconds** — which then unlocks the next skill
  via a prerequisite graph.
- **Confusion-pattern detection:** it specifically detects **b/d, p/q, m/n, u/n
  reversals** rather than just marking answers wrong. Diagnosing *why* the error
  happened is the same move as "explain the delta, not the total."
- **Ten game templates** across recognition, matching, sorting, blending, sequencing,
  memory and discrimination — 24 skill domains, 100+ micro-skills.
- **Stack:** Next.js 16, TypeScript, Prisma 6, Express 5, Neon Postgres, AWS S3,
  Redis, **Google Gemini** for question generation.
- **Be honest about status:** the README says ~85% complete with several features
  marked upcoming. **Don't hide that — lead with it.** "I mark what's shipped and
  what isn't" is exactly the trait they're screening for, and it matches how you
  wrote up your own submission's weaknesses.

**Two non-knowled projects worth having in your pocket** (only raise if asked "what
else have you built" or if voice architecture comes up):

- **SafeSpace** — a multi-channel AI companion over **web chat, WhatsApp *and*
  phone/voice**, built so every channel calls the same agent entrypoint. Your own
  framing: **voice is a transport layer, not a fork of the agent logic.** That is
  precisely the architectural question Hunar lives inside. If Shantanu asks whether
  you've thought about voice systems, this is the answer — with the honest caveat
  that it's a personal project, not production traffic at their scale.
- **An AI hiring reach-out assistant** with two intake routes feeding a shared calls
  dashboard. Same domain as Hunar's product. Mention only briefly, and don't imply
  it's comparable to their system.

---

## 3. The knowled.ai → Hunar bridge (your strongest narrative asset)

These parallels are **concrete and verifiable**, not thematic hand-waving. That's what
makes you not a generic AI candidate. Learn them and deploy the one that fits the
question.

| What you actually shipped at knowled.ai | The same judgment in your Hunar submission |
|---|---|
| **4-digit PIN login for 4-year-olds — no email, no password** (`gamified-ai`) | The **shared-handset privacy gate** and refusing to assume phone ownership or literacy. You have *already* designed credentials for someone who cannot type them. |
| **Text-to-speech module** so IEP documents could be heard, not read (`assessment-tool`) | **"Reading is the accommodation, listening is the baseline."** You shipped the thesis before you argued it. |
| **Super Special Educator must approve or reject-with-feedback every AI-generated IEP goal**; flagged-cases queue | **"The AI never delivers termination or discipline"** — a named human on every consequential call, escalation on low confidence. |
| **Educator can override the AI's tier, but must type a justification** (`mass-assessment`) | **"She never composes, she only confirms — except she must produce a number"** for anything that binds her. Both designs force one irreducible act of genuine human input instead of a rubber-stamp. |
| **Confusion-pattern detection (b/d, p/q) instead of just marking it wrong** | **Explain the delta, not the total** — diagnose the cause, don't just report the outcome. |
| **Mastery defined concretely: 80% accuracy under 4 seconds**, not a vibe | **Unaided recall as the north-star metric**, and *"measure false-non-match at their gate for two weeks, disaggregated"* — you define success as a measurable threshold, not an impression. |
| **`AuditLog` with user + IP per action; DPDP/FERPA; RCI certification validity tracking** | **DPDP posture on salary data, minimum-data and purpose-limitation** (`07` §C2). Compliance is a habit for you, not a slide. |
| **Six roles from parent to school leadership, each with a real permission boundary** | **Worker + supervisor + CHRO + union** — including briefing the union before launch. You instinctively design for everyone in the room, not just the buyer. |
| **Eight agents behind queues with LangSmith tracing and async processing** | Your cost and latency reasoning in `07` §A1, and the **kill switch** that suspends salary calls when payroll data quality drops. |
| **~20 migrations reshaping the schema as reality pushed back** | **The second research pass that broke your own plan** (contract labour). You expect the first design to be wrong and you build to be corrected. |

**The one-sentence bridge to have ready:**

> "At knowled.ai every user I built for was someone the industry designs around — a
> four-year-old who can't type a password, a parent who won't read a 12-page IEP. You
> learn fast that the model is the easy part; trust, the human in the loop, and
> compliance are the product. That's the lens I brought to this challenge, and it's
> what an FDE does."

**Caution — don't overclaim.** Special-ed software and frontline voice AI at 5 lakh
calls/day are different worlds. Frame it as *transferable judgment*, not equivalent
experience. If they push ("this is quite different from what we do"), agree
immediately: the transfer is in **how you treat an underserved user and where you put
the human**, not in domain knowledge or voice infrastructure at scale — which you'd
build in the field, the way they did with the agency. Never imply your personal
projects operate at their scale.

---

## 4. How you built the submission — the process story (your secret weapon)

This is the part most candidates can't answer well and the part your own files answer
*beautifully*. The founders will almost certainly ask some version of **"walk me
through how you approached this"** or **"how much of this is real vs. plausible?"**
Your process is a genuine differentiator because it mirrors *their* fieldwork-first
value. Tell it as a story of **deliberate choice → grounding in evidence → catching
your own errors.**

### 4.1 The arc to narrate

1. **I chose the prompt deliberately, against my own instinct for the flashy one.**
   "#1 rewards imagination, #3 rewards homework. For a company that ran a recruitment
   agency for two years before writing code, I bet homework was the higher-signal
   choice." (This flatters the truth, not the interviewer — it's genuinely why you
   picked it. See `00-pick-decision.md`.)
2. **I grounded every claim in a source, then did a second research pass that broke
   my own design.** The second pass surfaced **contract labour (~38%)**, which
   punctured my own recommended sequence. "Finding a hole in your own plan is worth
   more than a tidier answer."
3. **I corrected three of my own mistakes**, and I kept them in the design as
   evidence of how I work (see §4.2). "I'd rather be caught correcting a mistake than
   defending one."
4. **I designed the *deliverable* to prove the thesis** — audio-led, subtitled,
   because if the argument is that these workers can't read, the video should be
   something you can *hear*.

### 4.2 The three self-corrections — know these cold, they're your credibility

If asked "what did you get wrong / change your mind on," you have three real ones.
Each shows a different senior trait.

1. **I endorsed face recognition, then retracted it.** First draft demolished
   fingerprints with hard numbers, then endorsed face recognition *on assertion* —
   "using evidence to kill the option I didn't want and rhetoric to justify the one I
   did." NIST FRVT shows face-recognition bias **varies by algorithm** and is driven
   by image quality; a 6am shift change with headscarves is near worst-case. So I
   replaced "use face recognition" with a **selection procedure**: measure false-non-
   match at *their* gate for two weeks, disaggregated by cohort and shift hour, never
   the average. → *Trait: I don't recommend a technology I haven't measured.*
2. **My "confirm-only" rule manufactured consent.** "She only confirms" is right for
   information — but a design whose only verb is "yes," aimed at someone who already
   defers to authority, **industrialises acquiescence.** So the rule went two-tier:
   confirm for routine info, **produce a number** for anything that binds her ("if you
   take two days off, how much less?"). A number can't be faked by nodding, numerals
   are the most ASR-reliable class, and numeracy outruns literacy here. → *Trait: I
   audit my own design for the failure mode it claims to solve.*
3. **My video script ran 5:35 against a 5-minute cap while I claimed 4:56** — because
   I *asserted* a word count instead of counting it. I caught it by auditing my own
   work and rebuilt the script to a machine-counted 4:48. → *Trait: confirmation of an
   action is not verification of its result* — which is, not coincidentally, exactly
   the discipline you'd bring to a customer deployment.

> There's a fourth, softer one you can offer: I killed a "daily piece-rate feedback"
> feature I'd been proud of, because a daily "you did 340, your average is 310" is a
> **leaderboard of one** — productivity pressure dressed as transparency, in an
> industry with documented speed-up harms. A refusal list is only worth writing if
> you apply it to your own work.

### 4.3 If they ask: "did you use AI to build this?"

Answer honestly and turn it into a positive. Suggested framing:

> "Yes — I used AI as a research and drafting partner, the way an FDE would use every
> tool available. But the *judgment* is mine: which challenge to pick and why, the
> decision to run a second research pass, catching that contract labour breaks my own
> salary wedge, retracting the face-recognition endorsement, and deciding what to
> *refuse* to build. AI doesn't tell you to go find the hole in your own plan. That's
> the part you're hiring."

Do **not** pretend you didn't use AI — this is an AI company; that reads as either
dishonest or out of touch. Own the tool, own the judgment.

---

## 5. "About you" behavioural questions — prep answers

Notes to speak from, not scripts. Keep each to 60–90 seconds. Pull concrete examples
from §2.1 rather than speaking in generalities.

**Q: What's the thing you're proudest of building?**
> Pick **one** and go deep rather than listing three. Strongest option: *the PIN login
> on the literacy platform.* "The obvious build is email and password because that's
> what every auth library gives you. But the user is four years old. So it's a
> four-digit PIN, 60-pixel touch targets, and audio prompts — and the teachers keep
> email/password because they can handle it. Deciding which user gets which
> credential model is the actual product decision; the auth code is trivial."
> Alternative if they lean technical: *the eight-agent screening service* — queues so
> the educator never waits on the LLM, LangSmith so you can see what the agent
> actually did, and a mandatory justification field on any human override.

**Q: Walk me through a hard technical decision you made.**
> Good candidate: **putting the AI behind a queue instead of in the request path**
> (`mass-assessment`). An educator entering scores for 40 students cannot wait on
> eight LLM calls. So the AI work is Bull/Redis jobs, the educator gets an immediate
> write, and the rationale arrives after. Tie it to Hunar: "latency and failure
> isolation are the whole game when a human is waiting on the other end — that's true
> for a teacher at a desk and much more true for a worker on a phone call."

**Q: Why do you want to be an FDE, specifically? (vs. a normal PM/engineer role)**
> The FDE role is the honest version of building product: you don't get to hide
> behind a spec, you're in the room where it breaks. I like being accountable to a
> real user in a real place. My whole submission is a week-one discovery plan, not a
> feature list, because that's the part of the job I actually want.

**Q: Why Hunar? (Why not a bigger/flashier AI company)**
> Because the interesting AI problem in India isn't another white-collar copilot —
> it's the workforce nobody builds for. Hunar is one of the few companies pointing
> real voice AI at that, and you've earned the right to by doing the fieldwork first.
> I want to work where the ground truth matters more than the demo.

**Q: Why are you leaving knowled.ai?** *(Have a clean, honest, non-bitter reason.)*
> [YOUR REAL REASON — framed forward, not backward.] Safe framings: wanting to work
> on a larger-scale deployment problem; wanting to be customer-embedded; the pull of
> the frontline-workforce problem specifically. **Never** trash the old company or a
> manager. If there was a layoff/shutdown, state it plainly and without drama.

**Q: What's your biggest weakness? / Where do you struggle?**
> Pick a real one with a real mitigation. A defensible one grounded in your own docs:
> "I can over-invest in getting the reasoning airtight before I ship — my first video
> script overran because I kept refining content instead of timing it early. I've
> learned to put the cheap verification check *first*, not last." (This is true from
> your own process and it doubles as an FDE virtue.)

**Q: Tell me about a time you were wrong / changed your mind.**
> Use the **face-recognition retraction** from §4.2. It's a clean, specific,
> intellectually-honest example and it's *yours*.

**Q: Tell me about a time you dealt with a difficult stakeholder / ambiguity.**
> [YOUR REAL knowled.ai example — e.g. a school leader or parent who distrusted the
> AI, and how you built trust.] If you don't have a sharp one, the **approval workflow**
> is a legitimate substitute: "senior educators didn't trust AI-drafted IEP goals, and
> they were right not to — an IEP is a legal document about a child. So the AI drafts
> and a super educator approves or rejects with feedback. Trust came from the
> reject-with-feedback path existing, not from telling them the model was accurate."
> Tie it to the submission: "that's why my trust section starts from 'her distrust is
> rational,' not from tone of voice."

**Q: Have you ever had to say no to a feature / push back?**
> Two options, both real. From the submission: you **killed the daily piece-rate
> feedback feature** you'd been proud of, because a daily "you did 340, average is
> 310" is a leaderboard of one — productivity pressure dressed as transparency. From
> knowled.ai: the honest "85% complete" framing on the literacy platform, with
> features explicitly marked upcoming rather than quietly implied as done.

**Q: How do you handle a situation where you don't know the answer?**
> Say the sentence that's literally in my design: "I'm not sure — I'll find out and
> come back." In the field that's not weakness, it's the thing that keeps you from
> shipping a confidently-wrong answer, which does more damage than silence. My salary
> module has a kill switch for exactly that reason.

**Q: You have no frontline/factory experience. Why should we trust you on a plant floor?**
> Correct — I don't, and I'm not going to pretend the secondary research substitutes
> for a shift change. What I'd bring in week one is the instinct to go *find* the
> ground truth: sit on the payroll desk, ride the gate at 6am, interview ten workers
> and three supervisors separately. I built a whole discovery plan because I know the
> plausible answer and the real answer are different — the way you learned it running
> the agency.

**Q: Where do you see yourself / what do you want to learn here?**
> Keep it about the craft: learning what actually breaks a deployment (data quality,
> supervisor adoption, integration — I have a guess, I want the real answer), and
> earning the fieldwork intuition you two already have.

---

## 6. Founder-specific angles — connect to *their* history

### 6.1 The Locus / logistics connection — and "why not Challenge #1?"

Both founders come from **Locus, a logistics company**. **Challenge #1 was literally
about a logistics company with 50,000 delivery partners** — and you *didn't* pick it.
There's a real chance Krishna asks why. Have a confident answer:

> "I noticed #1 was the one closest to your own backyard — delivery fleets,
> logistics. I nearly took it for that reason. I didn't, and here's the honest logic:
> #1 explicitly says 'imagine AI has become good enough' and 'forget how apps work
> today' — it *rewards imagination*, and a vivid answer can be thin. #3 hands you a
> population and dares you to know something real about them. For a company whose
> origin story is two years of fieldwork, I bet demonstrating homework beat
> demonstrating imagination. #1 has a higher ceiling; its floor is a lot lower."

Then, if you want to score the point:

> "That said — if you want to talk #1, I have opinions. The interesting thing about an
> AI *manager* for drivers is that it's the one prompt where the AI holds *authority*
> over a human: assign, evaluate, discipline, reward. And I'd apply the same rule I
> used in #3 — the AI can advocate and inform, but it never delivers the discipline.
> That boundary is the whole product."

This shows you can play on their turf and that your design principles generalise.

### 6.2 The "80% of HR is calling" thesis

Krishna's framing is that HR is fundamentally voice work. Your submission *is* a voice-
first, no-app, no-chatbot design — "outbound conversations at the right moment." You
independently arrived at their core thesis. **Name that alignment** — but credit it as
convergence, not flattery: "I didn't design it to match your product; the constraints
forced it. Odia ASR at 35% WER and 38% phone ownership don't leave you a chat window."

### 6.3 The agency / ground-truth ethos

Every time you can, tie a design choice back to *"the plausible answer differs from
the real one."* That's the lesson they paid two years to learn. Your contract-labour
finding, your "measure at the gate not the datasheet," your unaided-recall north star
— all of them are that lesson. This is the deepest cultural fit signal you have.

---

## 7. Questions to ask them (pick 3–4; these signal how you'd operate)

Ordered by signal. The first four are the strongest.

1. **When you ran the recruitment agency, what did you believe going in that turned
   out to be flat wrong on the ground?** *(Directly honours their origin story and
   invites the most interesting answer they have.)*
2. **On a live deployment, what most often stalls a pilot — integration, supervisor/
   manager adoption, or the customer's own data quality?** *(This is the FDE
   question. Their answer tells you the real job. In my design I bet on data quality
   breaking first — I'd want to know if that's right.)*
3. **Where does the product hand off to a human today, and was that boundary chosen
   deliberately or discovered the hard way?** *(Shows you think about the human-in-loop
   seam, which is your knowled.ai muscle.)*
4. **How much of an FDE's week here is customer conversation vs. configuration vs.
   firefighting?** *(Signals you understand the role isn't glamorous.)*
5. You price by workflow, not by minute. How did you land there, and does it ever
   fight against doing the *right* number of calls? *(Shows you read the commercial
   model closely.)*
6. Your hybrid voice architecture keeps audio properties instead of flattening to
   text early. Where has that mattered most — which sector or language forced it?
   *(One for Shantanu; shows genuine technical curiosity.)*
7. As you move from hiring into deeper workforce management — the kind of "AI as
   manager" territory the challenges gesture at — where's the hardest trust boundary
   you're running into with customers?

**Avoid:** salary/comp/hours as your *first* question, anything answered on the
homepage, and "do you have work-life balance" in a founder round. Save logistics of
comp for the recruiter.

---

## 8. Landmines & how to defuse them

- **Getting defensive about a weakness.** They already know the holes — you *wrote
  them down* (no primary research, contract-labour gap, two invented numbers). When
  they poke, agree fast, restate the mitigation, move on. Defensiveness is the only
  way to actually fail here.
- **Over-talking.** You have a lot of material. Answer in 60–90 seconds, then stop and
  let them steer. Density beats volume. The founders are busy operators.
- **Pretending to know factory/frontline reality you don't.** Fatal with these two.
  Always distinguish "what I found in research" from "what I'd confirm in the field."
- **Name-dropping stats wrong.** Keep the five you actually need: Odia ASR **~35%** vs
  Hindi **~16%** WER; phone ownership **38% women / 71% men**; contract labour **~38%**;
  Karnataka garment wage **~₹13,000**; biometric failure **~6.5%** national / **~36%**
  worn-fingerprint Telangana. If unsure of a number, say "around" and move on — don't
  invent precision.
- **The AI-authorship question.** Covered in §4.3 — own the tool, own the judgment.
- **"This is just our product, what's new?"** Covered in `07` §A4 — concede most of it
  isn't new *and that's deliberate*; the additive parts are the salary-delta wedge, the
  shared-handset privacy gate, the attendance audit loop, monthly advocacy, and
  unaided-recall as the metric.
- **Silence after you answer.** Founders sometimes go quiet to see if you'll
  ramble-fill. Don't. Finish your point and hold.
- **Overstating your projects' scale.** Hunar runs ~5 lakh calls/day. Your repos are
  pilot/early-stage products and one is openly ~85% complete. If you imply parity, a
  founder who checks will catch it and everything else you said gets discounted. Give
  the real status unprompted — it costs you nothing and buys credibility.
- **A practical flag on the repos themselves.** `assessment-tool`, `mass-assessment`
  and `gamified-ai` are **public** under your personal account, and they contain
  knowled.ai product code, schema, and README seed credentials like
  `admin@knowled.com / admin123`. Two implications worth thinking about before the
  call: (1) a founder evaluating you for a role handling **enterprise HR and payroll
  data** may read public ex-employer code as a discretion signal — consider making
  them private and sharing access on request, or at minimum confirm you had
  permission; (2) if the seeded credentials match anything real or reused, rotate
  them. If it comes up, the clean answer is a factual one about what permission you
  had — don't improvise.

---

## 9. The three things to make sure they leave believing

If the conversation goes sideways, steer back to these:

1. **You reason from the ground truth, not the demo** — you picked the "homework"
   prompt, grounded every claim, and went looking for the hole in your own plan.
   *(This is their culture.)*
2. **You've already shipped for non-readers, with the human holding the final call.**
   A 4-digit PIN for four-year-olds, text-to-speech on IEP documents, a senior
   educator who must approve or reject every AI-generated goal, an override that
   requires a written justification. Frontline non-literate workers aren't a leap for
   you — they're the same instinct at a new edge.
3. **You have the FDE temperament** — you say "I was wrong," "I don't know, I'll find
   out," and "here's what I'd measure," and you designed a week-one discovery plan
   instead of a feature list.

---

## 10. Night-before checklist

- [ ] Fill in the remaining brackets in §2 (title, dates, real user/school counts,
      whether you were customer-facing) — then rehearse the 90-second story aloud
      twice, on a timer.
- [ ] Memorise the **four flagship details** from §2.1: the 4-digit PIN, the
      text-to-speech module, approve-or-reject-with-feedback, and
      override-requires-justification. These four carry the entire bridge in §3.
- [ ] Re-read `00-pick-decision.md` §4 (the tiebreaker) and this file §4 (the three
      self-corrections) — those are your two highest-value stories.
- [ ] Skim `07-qa-prep.md` §A1 (cost), §B1 (ASR), §D2 (week one) so a design probe
      doesn't catch you flat.
- [ ] Memorise the five stats in §8 and the founders' backgrounds in §1.
- [ ] Decide on the repo visibility question in §8 **before** the call, and rotate any
      real credentials that appear in the seed data or READMEs.
- [ ] Confirm the three live demo links still load (they're on Vercel free tier and
      may cold-start): `assessment-tool-chi`, `mass-assessment`, `gamified-ai`. A dead
      link mid-interview is an avoidable own goal.
- [ ] Have the video and one-pager open in a tab in case they want to reference a
      specific moment.
- [ ] Prepare your 3–4 questions from §7; know which one you'll open with.
- [ ] One clean, forward-looking sentence on why you're leaving knowled.ai.
- [ ] Water, quiet room, headphones, test the mic — you're interviewing at a *voice*
      company; audio quality is table stakes and they will notice.

---

*Sources for company/founder facts: [Inc42](https://inc42.com/startups/why-hunar-ai-thinks-indias-frontline-workforce-needs-ai-agents/),
[YourStory](https://yourstory.com/ai-story/hunarai-whatsapp-ai-fix-india-frontline-hiring-problem),
[Republic World](https://www.republicworld.com/initiatives/meet-indias-visionary-founders-transforming-success-in-2026-with-purposeful-leadership-2026-08-11-134490),
[ElevenLabs](https://elevenlabs.io/blog/hunar), [Hunar.AI](https://hunar.ai/),
[knowled.ai](https://knowled.ai/). Content rephrased for compliance with licensing
restrictions. §2.1 project details were read directly from the READMEs, Prisma
schemas, migration history and file trees of
[assessment-tool](https://github.com/iakshayrathee/assessment-tool),
[mass-assessment](https://github.com/iakshayrathee/mass-assessment) and
[gamified-ai](https://github.com/iakshayrathee/gamified-ai).*
