# Code deep-dive — knowled.ai, built solo, in the field · FDE technical prep

Companion to `08-founder-round-prep.md`. That file is the person/process layer.
**This file is the engineering** — the systems you built alone at knowled.ai, the
decisions behind them, and how to defend them at a CTO/senior-FDE level. Every claim
here is grounded in your own committed code so it holds up under probing.

> **New here / a term trips you up?** Keep `12-plain-language-glossary.md` open next to
> this. Every jargon word below (deterministic, queue, idempotency, LangGraph, WER, JWT…)
> is explained there in one plain sentence with an analogy. The key spots below also have
> an inline *"Plain:"* note. You should be able to say each idea in simple words — that
> ability *is* the FDE skill.

> **Positioning in one line:**
> "knowled.ai wasn't a team handing me tickets. I was the engineer. I sat with
> special educators and school leaders, watched how they actually worked, and built
> the whole stack myself — Postgres schema, Express APIs, a Python AI service, the
> Next.js frontends, and the deploys. Every technical decision traces back to
> something a teacher told me in a room."
>
> That sentence *is* the FDE job description. Lead with it.
>
> **Honesty guard (read `11` STEP-0 first):** this doc is written in the strongest
> framing — solo authorship + real school/teacher contact. Use it **only** if that is
> literally true. If you were on a team, or these were pilot/portfolio builds without
> real school users, downgrade the claims accordingly. The *code* facts below are true
> regardless; the *customer-discovery* claims are yours to substantiate. Never assert a
> specific "a school asked for X" cause unless it actually happened.

---

## 0. Why this is your strongest card with a senior FDE recruiter

A senior FDE recruiter is screening for six things. You can evidence every one with
code you wrote:

| FDE competency | Your proof from knowled.ai |
|---|---|
| **Customer discovery** — sit with users, extract the real constraint | You built *with* schools and teachers; each design choice below answers a specific thing a user told you |
| **Solo, full-stack ownership** — no one to hand off to | You built DB + backend + a separate Python AI service + frontend + deployment, across three products |
| **Production judgment** — it has to survive contact with reality | Offline queue, idempotent jobs, graceful degradation, per-job timeouts, model fallback, audit logging |
| **Human-in-the-loop / trust** — AI assists, humans decide | Deterministic scoring with the LLM only *explaining*; approval and override-with-justification workflows |
| **India + compliance context** | RCI certification tracking, DPDP/FERPA posture, multilingual, multi-role hierarchy |
| **Ships under ambiguity, iterates** | ~20 forward migrations reshaping the schema as the product met real classrooms |

The through-line to say out loud: **"I didn't build features. I built answers to
things I saw teachers struggle with."**

---

## 1. The field-to-code map (memorise this — it's the whole pitch)

For each system, the shape is: **what I saw in the field → the engineering decision →
the code that proves it.** This is exactly how an FDE reasons, so tell it this way.

| What a teacher / school told me | The decision I made | Where it lives in the code |
|---|---|---|
| "Why did the app suddenly make it harder for my student?" | Make adaptivity **rule-based and explainable**, not a black-box model | `adaptive-engine.ts` — every adjustment returns a `reason` string |
| A Tier-3 label is a serious thing to put on a child | The **AI never assigns the tier** — deterministic math does; the LLM only writes the explanation | `scoring.service.ts` (pure rules) vs `tier_rationale.py` (LLM only after `analyse_scores`) |
| "I've taught this child for a year; a 40-minute screening doesn't know her" | Let the educator **override the AI tier — but require a written reason** | `tierAlloc.isOverridden / overrideReason`, respected everywhere downstream |
| Special educators care *why* a child erred, not just that they did | Classify the **error type** (b/d, p/q reversals), don't just mark wrong | `classifyError()` + `ErrorType` enum in `adaptive-engine.ts` |
| A 5-year-old can't type an email/password | **4-digit PIN** auth for children; email/password only for adults | `auth.ts` role model `CHILD / TEACHER / ADMIN` |
| A parent won't read a 12-page IEP | **Text-to-speech** module so documents can be *heard* | `assessment-tool` TTS controls + `useSpeechSynthesis` |
| Classroom wi-fi drops mid-session; a teacher can't lose 40 kids' work | **Offline-first queue** with retry and guaranteed delivery | `attempt-queue.ts` — localStorage + idempotent UUIDs + `sendBeacon` |
| An educator entering a whole grade's scores can't wait on 40 AI calls | Push AI work to **background queues**; return instantly | `ai.service.ts` + `aiProcessor.ts` (Bull/Redis) |
| If the AI is down, screening still has to work | **Graceful degradation** — mark AI failed, keep the report available | `triggerAiPipeline` catch → `aiStatus: FAILED`, `status: REPORT_READY` |
| School leaders and regulators need accountability | **Audit log with IP**, RCI cert tracking, approval workflow | `assessment-tool` `AuditLog`, approval/reject-with-feedback |

---

## 2. System 1 — Gamified Literacy Platform (`gamified-ai`)

**What it is:** an adaptive literacy game for 4–6 year-olds, with teacher and admin
dashboards. **Your framing:** "The users literally cannot read, so I couldn't rely on
text for anything that mattered — auth, feedback, or navigation."

### 2.1 The adaptive difficulty engine — rule-based on purpose

Single file, ~500 lines, that you wrote: `backend/src/lib/adaptive-engine.ts`. A
`AdaptiveDifficultyEngine` class with explicit, inspectable rules.

- **Level up** when, over the last 5 attempts: accuracy ≥ 80% **and** average response
  time < 10s **and** no 2 consecutive errors → `min(3, level+1)`.
- **Level down** on: 3 consecutive errors **or** accuracy < 40% **or** (confusion
  pattern detected **and** avg time > 20s) → `max(1, level-1)`.
- **Mastery** requires all three: accuracy ≥ 80% over the last 10 **and** avg time
  ≤ 4s **and** confusion-error rate < 20%.
- Every decision returns a human-readable `reason` (e.g. *"Three consecutive errors
  detected — reducing difficulty"*).

> **Plain:** the game watches the child's last few answers. Do well (get most right,
> answer quickly) and it steps up a level; struggle (miss three in a row, or go slow and
> mix up look-alike letters) and it steps down. "Mastered" means a clear bar — 80%+
> correct, fast, few mix-ups. These are plain rules, so I can always say *why* the level
> changed.

**The decision to defend — why rules, not ML:**
> "Three reasons, all from the field. One, cold start — on day one I had zero
> training data, and an untrained model is worse than a good heuristic. Two,
> explainability — a teacher asked me point-blank why the game got harder for her
> student, and I could show her the exact rule that fired. A model that shrugs 'the
> weights said so' loses the teacher. Three, it's deterministic, so I can unit-test it
> and it behaves the same every time. When I had enough attempt data I could have
> swapped in a model behind the same interface — but the rules were the right *first*
> system, not a shortcut."

That last clause matters: it shows you chose the simple thing deliberately, not from
inability. **This is the exact instinct Hunar would want for a voice HR agent** — keep
the consequential decision legible.

### 2.2 Error classification — diagnosing *why*, not just *wrong*

`classifyError(correct, response)` maps a wrong answer to an `ErrorType`:
`B_D_CONFUSION`, `P_Q_CONFUSION`, `M_N_CONFUSION`, `U_N_CONFUSION`, `VOWEL_ERROR`,
`OTHER`. A confusion *pattern* is flagged when ≥ 30% of recent errors are these
letter-reversal types.

> "Special educators told me letter reversals like b/d are a signal they watch for.
> A generic 'incorrect' throws that signal away. So I classified the error itself —
> the same instinct as my Hunar submission: explain the delta, don't just report the
> outcome."

### 2.3 Auth for people who can't read — PIN vs password

`backend/src/lib/auth.ts`: a `role` of `CHILD | TEACHER | ADMIN`. Children authenticate
with a **4-digit PIN**; adults get email + bcrypt-hashed passwords, JWT access (24h) +
refresh (7d).

> "The obvious build is email/password because that's what the auth library hands
> you. But the user is four. Deciding *which user gets which credential model* was the
> actual product decision; the crypto was trivial. That's the same problem Hunar has
> with a worker who doesn't own a smartphone."

### 2.4 The offline attempt-queue — the piece that most impresses on frontline reality

`frontend/lib/attempt-queue.ts` — a client-side durable queue you wrote for flaky
classroom networks. Features, all real in the code:

- **Optimistic + durable:** every attempt gets a **UUID** (idempotency key) and is
  persisted to `localStorage` immediately.
- **Batched flush:** on reaching 10 queued or every 5 seconds.
- **Exponential backoff retry:** `min(1000 * 2^retry, 30000)`, up to 5 retries, then
  logged to a `failed_attempts` store for review.
- **Guaranteed delivery on exit:** `navigator.sendBeacon` on `beforeunload`.
- **Network-aware:** flushes on the `online` event; queues silently when `offline`.
- **Quota-safe:** on `QuotaExceededError`, trims to the most recent 50 and retries.

> **Plain:** when the internet drops, the app doesn't lose the child's work. It saves
> each answer on the device with a unique ID (so it can't be counted twice), keeps
> trying to send — waiting longer between tries so it doesn't spam a weak connection —
> and even flushes the last answers if the tab is closed. Exactly what a delivery
> worker on a patchy phone signal needs too.

> "A classroom's wi-fi drops constantly. A teacher should never lose a child's work
> because a request timed out. So the client is offline-first: idempotent IDs so a
> retry can't double-count, localStorage so a refresh doesn't lose data, sendBeacon so
> even closing the tab flushes. This is the single most transferable thing I built for
> Hunar — a delivery partner on 2G in a warehouse basement is the same problem."

**If they push on idempotency:** the UUID is generated client-side and the batch
endpoint returns `savedAttemptIds`; the client only removes confirmed IDs from the
queue, so a network failure after the server committed still reconciles correctly on
the next flush.

---

## 3. System 2 — Mass Screening + AI (`mass-assessment`) — the most Hunar-shaped system

**What it is:** screen an entire grade, tier every student, and run 8 AI agents to
explain, detect anomalies, generate reports, and answer educator questions. **Your
framing:** "This is a multi-agent system with queues, observability, model fallback,
and a hard human-override path — architecturally the closest thing I've built to what
Hunar runs."

### 3.1 The architecture — three services, deliberate boundaries

```
Next.js (frontend)  →  Express + TypeScript (backend)  →  FastAPI + Python (AI service)
                              │                                   │
                        PostgreSQL (Neon)                Redis (Bull queues + chat memory)
```

> "I split the AI into its own Python service on purpose. The LLM/LangGraph ecosystem
> is Python-native, and I didn't want slow, failure-prone AI calls sharing a process
> with the transactional API that teachers depend on to enter scores. Clean failure
> isolation: the AI service can fall over and score entry still works."

### 3.2 The safety spine — deterministic tiering, LLM only explains

This is the point to hammer for a company that will put AI in front of livelihoods.

`backend/src/services/scoring.service.ts` allocates the tier with **pure math**, no
LLM:
- Domain weights: reading .25, reading-comp .25, numeracy .25, spelling .15, writing .10.
- **Tier 3** if any domain < 40%, or 3+ domains < 70%, or weighted avg < 50%, or
  (behavioural flag **and** 2+ domains < 70%).
- **Tier 2** if 1–2 domains in 40–70%, or weighted avg < 70%, or (attention flag and a
  weak domain).
- **Tier 1** otherwise.

Only *after* the tier is fixed does the LLM run. In `ai-service/agents/tier_rationale.py`
the LangGraph is a 3-node chain: **`analyse_scores` (pure Python)** identifies weak
domains and which rule fired → **`generate_rationale` (LLM)** writes plain English →
**`generate_interventions` (LLM)** suggests actions.

> **Plain:** think of it as a 3-step assembly line. Step 1 is ordinary code (no AI) that
> works out which subjects are weak and which rule made the child "high risk." Only then
> do steps 2 and 3 — the AI — turn that into a readable paragraph and a list of
> suggestions. The AI never picks the risk level; it only explains a decision the plain
> rules already made.

> "The model that a child is Tier 3 is never made by a language model. It's made by
> deterministic, auditable rules that a school psychologist could read. The LLM's only
> job is to explain the decision the math already made and suggest interventions. If
> Hunar asked me to build a voice agent that touches hiring or discipline, this is
> exactly the boundary I'd hold: the consequential decision is legible and testable;
> the AI does language, not judgment."

### 3.3 The human override — and why it's more than a flag

Everywhere the tier is read, the code respects the educator's override:
`tierAlloc.isOverridden && overrideTier ? overrideTier : tier`. And the escalation
agent receives `educator_override_reason` as context.

> "Educators told me they know a child better than a 40-minute test. So they can
> override the AI tier — but the schema *requires* an `overrideReason`. That does two
> things: it keeps a human accountable, and the reason becomes a signal that flows
> into the escalation note. It's the same design as my Hunar rule that the worker must
> produce a number, not just say yes — force one irreducible act of real human input
> instead of a rubber stamp."

### 3.4 Queues, timeouts, and graceful degradation — production judgment

`ai.service.ts` `triggerAiPipeline()` runs after deterministic scoring:
- Sets `aiStatus: PROCESSING`, then enqueues **one tier-rationale job per student** and
  **one anomaly job per session** on Bull/Redis.
- **Deterministic job IDs** (`rationale-${sessionId}-${studentId}`) so a retry or
  double-submit can't create duplicate work — idempotency again.
- **Graceful degradation:** the whole thing is wrapped so that on failure it sets
  `aiStatus: FAILED` but `status: REPORT_READY` — *the screening report still works
  without the AI.*

`queues/aiProcessor.ts` (the Bull workers):
- **Concurrency tuned per job:** tier-rationale runs 5 in parallel; anomaly runs 1
  (it's whole-session and heavier).
- **Per-job timeouts** matched to the work: 55s tier, 110s anomaly, 170s report.
- **A chained pipeline:** the anomaly worker, on success, re-fetches *fresh* session
  data and enqueues report generation — the code comment literally says "no stale
  closures," because I'd been bitten by enqueuing stale in-memory data.
- Failure of report generation marks `aiStatus: FAILED` but leaves the session
  submitted — degrade, don't crash.

> **Plain:** the slow AI work is put on a "to-do list" (a queue) and done in the
> background, so the teacher never waits. Each task has a fixed ID so it can't run
> twice, and a time limit so it can't hang forever. And if the AI fails completely, the
> teacher still gets the basic report — the app degrades to a simpler version instead of
> breaking. (A broken escalator is still stairs.)

> "An educator entering 40 students' scores can't wait on 40 sequential LLM calls, and
> the LLM sometimes times out or rate-limits. So AI is background work on queues with
> concurrency limits, deterministic job IDs for idempotency, timeouts sized to each
> agent, and a fallback where a failed AI run still yields a usable report. Latency and
> failure isolation when a human is waiting on the other end — that's the entire game
> at Hunar too, only more so on a live phone call."

### 3.5 Multi-agent orchestration — LangGraph, typed state, streaming, memory

- **Typed state machines:** every agent is a `StateGraph` over a `TypedDict` state
  (`ai-service/models/states.py`), with explicit nodes and edges. Not a free-for-all
  prompt — a graph you can reason about.
- **Educator Assistant** (`educator_assistant.py`) is a 4-node graph:
  `understand_intent → fetch_relevant_data → generate_answer → update_memory`.
  - **Intent classification** first (STUDENT_QUERY / DOMAIN_QUERY / TIER_QUERY /
    COMPARISON_QUERY / GENERAL) — the same routing an HR voice agent does before it
    acts.
  - **Redis-backed conversation memory** keyed `chat:{educatorId}:{sessionId}`, 24h
    TTL, trimmed to the last 20 messages to bound tokens.
  - **Token streaming** via `llm.astream(...)` for SSE, then it persists the full turn
    to Redis after streaming completes.
- **Model config with fallback** (`config.py`): Gemini 2.0 Flash as primary, GPT-4o-mini
  as fallback, both capped at 2048 output tokens; **LangSmith tracing** wired in for
  observability.

> "Token streaming with a persisted conversation memory is the same pattern a voice
> agent needs — you stream tokens so the reply starts fast, and you keep session memory
> so it doesn't forget what was said 20 seconds ago. And I wrapped it in LangSmith from
> the start because when an agent gives a weird answer, 'I can't see what it did' is not
> an acceptable place to be. That observability instinct is what I'd bring to debugging
> a Hunar deployment."

---

## 4. System 3 — IEP / Assessment Platform (`assessment-tool`) — the enterprise one

**What it is:** the largest of the three — a full special-education management platform.
**Your framing:** "This is where I learned to build for an *organisation*, not just a
user — six roles, an approval chain, and compliance baked in."

- **Six roles with real permission boundaries:** Admin, Center, Special Educator,
  **Super** Special Educator, Parent, School Viewer. Layered cleanly into
  controller → service → repository (name the layering; it signals you write
  maintainable code, not one 4,000-line file).
- **The approval workflow is the spine:** a special educator drafts an IEP goal or
  assessment; a *super* educator approves or **rejects with feedback**; plus a
  **flagged-cases** queue. This is your human-in-the-loop proof at the org level.
- **Compliance is built in, not bolted on:** an `AuditLog` capturing user + IP per
  action; **RCI certification tracking** (Rehabilitation Council of India — validity
  and renewal dates), a genuinely India-specific regulatory detail; DPDP/FERPA posture;
  per-student primary/secondary language.
- **Text-to-speech** module (document viewer, TTS controls, `useSpeechSynthesis`) so
  IEPs can be heard — the listen-not-read thesis, shipped.
- **~20 forward migrations** from `init` through `add_approval_system`,
  `add_school_assignments`, `add_center_report_snapshots`, `make_parent_optional`.

> "The migration history shows a schema that changed as the product met reality —
> `make_parent_optional`, `add_approval_system`, `add_school_assignments`. Each one was
> a real constraint I had to design around, not a feature I dreamed up."
>
> *(If — and only if — you genuinely have the story behind a specific migration, e.g. a
> school that enrolled kids without parent records, tell that story; it's the most
> FDE-sounding thing you can say. If you don't, do not invent a cause — "the schema
> iterated as I hit real constraints" is true and enough.)*

---

## 5. CTO / senior-FDE technical Q&A — code-grounded answers

Short, specific, and always tied back to a decision. Don't recite the stack; explain a
tradeoff.

**Q: Why rule-based adaptivity instead of ML?**
> Cold start (no data on day one), explainability (a teacher asked me why difficulty
> changed and I could point at the rule), and testability (deterministic). Same
> interface, so a model could slot in later. Choosing the simple correct thing first.

**Q: How do you stop the LLM from making a harmful call?**
> It never makes the call. Tiering is deterministic math in `scoring.service.ts`; the
> LLM runs only after, and only to explain and suggest. `analyse_scores` is a pure
> Python node; the LLM nodes come downstream. The consequential decision is legible.

**Q: LLM is slow / rate-limited / down. What happens?**
> Background Bull queues, per-agent timeouts (55/110/170s), concurrency tuned per job,
> a Gemini→GPT-4o-mini fallback, and graceful degradation: `aiStatus: FAILED` but the
> report is still `REPORT_READY`. The human workflow never blocks on the AI.

**Q: How do you avoid duplicate or lost work?**
> Idempotency on both ends. Client: UUID per attempt, server returns saved IDs, only
> confirmed IDs leave the queue. Server: deterministic Bull job IDs like
> `rationale-${sessionId}-${studentId}` so re-submits don't double-process.

**Q: How is the multi-agent system structured — is it just chained prompts?**
> LangGraph `StateGraph`s over `TypedDict` states with explicit nodes/edges. Pure-Python
> nodes do the deterministic analysis; LLM nodes do language. One pipeline chains across
> queues (anomaly → report). The assistant adds intent-classification, Redis memory, and
> token streaming.

**Q: Bad connectivity — how does the client behave?**
> Offline-first `attempt-queue.ts`: localStorage persistence, batched flush, exponential
> backoff, `sendBeacon` on unload, `online` re-flush, quota handling. Nothing is lost on
> a dropped connection or a closed tab.

**Q: How would this scale to Hunar's volume?** *(be honest)*
> It's built with the right primitives — queue concurrency, stateless workers, serverless
> Postgres, failure isolation — but I've run it at pilot scale, not 5 lakh calls a day. I
> know the difference, and I'd want to learn where *your* system actually bends under
> that load rather than pretend mine has.

**Q: Security / data protection?**
> JWT + bcrypt, role-based access across six roles, an `AuditLog` with IP per action,
> S3 for documents, and RCI/DPDP-aware handling of minors' data. Compliance was a
> first-class concern because the users are children.

---

## 6. Talking points that specifically land "solo + in the field"

Deploy these verbatim-ish when the recruiter probes ownership or customer contact:

- **Solo ownership:** "There was no backend team or ML team to hand off to. I designed
  the Postgres schema, wrote the Express APIs, stood up a separate Python AI service,
  built the Next.js frontends, and did the deploys on Neon, Render and Vercel. If it
  broke at ११ PM, I was the one who fixed it."
- **In the field:** "I wasn't building from a PRD. I was talking to special educators
  and school leaders, watching where they got stuck, and turning that into schema
  changes and features. The approval workflow, the override-with-reason, the PIN login
  — none of those came from my head, they came from a person telling me something."
- **Judgment under constraints:** "Every interesting decision was a constraint I
  couldn't design away — kids can't read, wi-fi drops, teachers won't trust a black
  box, a Tier-3 label is serious. I optimised for trust and resilience over
  cleverness."
- **The honest edge:** "It's pilot-stage software and I'll tell you exactly what's
  solid and what's still rough — same way I wrote up the weaknesses in my challenge
  submission. I'd rather you trust my read of my own work than oversell it."

---

## 7. Staying bulletproof (read before the call)

You're presenting this as **your** solo build in partnership with schools and teachers.
To keep that unimpeachable under a sharp technical interviewer:

- **Be ready to open any file and explain it.** You wrote it, so this is easy — but
  skim `adaptive-engine.ts`, `scoring.service.ts`, `aiProcessor.ts`, `tier_rationale.py`
  and `attempt-queue.ts` the night before so the details are instant, not fished-for.
- **Don't inflate scale or user counts.** Solo authorship and real school/teacher
  engagement are impressive on their own. Inventing "10,000 students" is the one thing
  that, if caught, retro-taints everything true. Say "pilot with [real, honest
  number]."
- **Have one concrete field anecdote ready** — a specific thing a teacher or school
  leader said that changed the code. One real story beats ten abstractions, and it's
  the most FDE-sounding thing you can say.
- **Repo hygiene (from `08` §8):** the repos are public under your personal account with
  seeded creds like `admin@knowled.com / admin123` in the READMEs. Consider making them
  private + sharing on request, rotate anything real, and be ready to state plainly what
  permission you had to build/retain this. A senior FDE recruiter evaluating you for
  access to enterprise HR/payroll data will notice how you handle ex-employer code.

---

*§2–§4 details were read directly from the source of
[gamified-ai](https://github.com/iakshayrathee/gamified-ai),
[mass-assessment](https://github.com/iakshayrathee/mass-assessment) and
[assessment-tool](https://github.com/iakshayrathee/assessment-tool): specifically
`adaptive-engine.ts`, `auth.ts`, `attempt-queue.ts`, `scoring.service.ts`,
`ai.service.ts`, `queues/aiProcessor.ts`, `ai-service/agents/tier_rationale.py`,
`educator_assistant.py`, `config.py`, and `models/states.py`.*
