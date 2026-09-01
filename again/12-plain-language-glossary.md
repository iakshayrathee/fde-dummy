# Plain-language glossary — understand every term in your prep

Read this alongside `08`, `09`, `10`, `11`. It explains every technical word in those
docs in simple language, with an everyday analogy, and — where it matters — **how to
say it out loud** in the interview. Nothing technical was removed from the other docs;
this is the translation layer.

> How to use it: if a sentence in another doc has a word you'd stumble on, find it here.
> The goal is that you can *explain* each idea simply — because the ability to explain a
> technical thing in plain words is exactly what a good FDE does with a customer.

---

## 1. The AI / LLM words

- **LLM (Large Language Model)** — the kind of AI behind ChatGPT: software that
  understands and writes human language. *Analogy:* an extremely well-read assistant
  that predicts the next words. *In Hunar's world:* the thing that powers a voice agent.
- **Model** — the specific trained AI you're using (e.g. *GPT-4o-mini*, *Gemini 2.0
  Flash*). Different models = different brands/sizes of the same idea.
- **Prompt** — the instruction you type to the LLM. "Prompting" = asking it well.
- **Token** — a small chunk of text (roughly part of a word) the model reads and writes.
  Models charge money and have limits *per token*, so "cap at 2048 tokens" just means
  "don't let the answer get longer than ~1,500 words."
- **Temperature** — a 0-to-1 dial for randomness. Low (0.1) = focused, predictable,
  same-every-time. Higher (0.4) = more creative and varied. *You used low temperature
  when the AI had to classify something precisely, and higher when it had to write
  friendly prose.* Say it as: "I turned creativity down for decisions and up for
  writing."
- **Streaming** — showing the answer word-by-word as it's generated, instead of waiting
  for the whole thing. *Analogy:* watching someone type live vs. getting a finished
  letter. *Why it matters for Hunar:* on a voice call you want the reply to *start*
  fast.
- **Agent** — an LLM set up to complete a task in **steps** (and use data/tools), not
  just answer one question. A "manager" agent, a "screening" agent, etc.
- **LangChain / LangGraph** — free toolkits for building LLM agents so you don't code it
  all from scratch. **LangGraph** specifically lets you build an agent as a **flowchart**
  of steps. *Analogy:* a recipe with numbered steps and arrows.
- **Node / edge** — in that flowchart, a **node** is one step ("work out the weak
  subjects"), an **edge** is the arrow to the next step. Saying "a 3-node graph" just
  means "a 3-step process."
- **State (TypedDict)** — the shared **clipboard** of information passed from step to
  step. "TypedDict" just means you wrote down exactly what fields are on that clipboard,
  so mistakes get caught early. Say it as: "each step reads and updates a shared data
  object."
- **Intent classification** — the AI first works out *what kind* of question was asked
  before answering. *Analogy:* a receptionist routing your call to the right desk. *In
  your code:* is this a question about a student, a subject, or a tier?
- **RAG (retrieval-augmented generation)** — giving the LLM the relevant facts to read
  *before* it answers, so it doesn't make things up. *Analogy:* open-book exam instead
  of from memory. (Hunar uses this idea; you can nod to it.)
- **LangSmith** — a tool that records what the AI did on every call so you can debug it
  later. *Analogy:* a flight recorder / CCTV for your AI. Say it as: "so when an agent
  gives a weird answer, I can see exactly what it did."

---

## 2. The most important idea: "deterministic" vs "AI"

This is the spine of your whole technical pitch, so be crystal clear on it.

- **Deterministic / rule-based** — fixed rules that always give the **same** answer for
  the same input, with no guessing. *Analogy:* a calculator, or an if-this-then-that
  flowchart. **The AI does NOT do this — a calculator does.**
- **Weighted average** — an average where some parts count more than others. E.g.
  reading counts 25% of the score, writing only 10%. *Analogy:* a final grade where the
  exam matters more than homework.
- **Threshold** — a cut-off number that triggers a decision. "Below 40% = high risk" is
  a threshold.
- **Why you keep saying this:** in your screening tool, the child's **risk tier is
  decided by fixed math** (deterministic), and the **AI only writes the explanation
  afterwards.** Plain version to say out loud: *"A language model never decides
  something serious about a person. The math decides; the AI just puts it into words a
  parent can read. That keeps the important decision predictable and auditable."*
  *(“Auditable” = someone can check exactly why the decision happened.)*

---

## 3. How the software is put together (architecture)

- **Frontend** — what the user sees and taps: the screens. Built with **Next.js /
  React** (toolkits for building screens).
- **Backend** — the "brain" on the server behind the screens: stores data, runs the
  logic. Built with **Express** (JavaScript/TypeScript) or **FastAPI** (Python).
- **Why two backends in one project:** you put the AI in its own **Python (FastAPI)**
  service because AI tools are Python-based, and you didn't want slow AI calls to slow
  down the normal app. *Analogy:* a separate specialist department.
- **Service / microservice split** — breaking the app into separate programs that each
  do one job, so if one breaks the others keep running. Say it as: "clean failure
  isolation — the AI can fall over and score-entry still works."
- **API** — the way two programs talk: a menu of requests one can make to another.
  *Analogy:* a waiter carrying your order to the kitchen and bringing food back.
- **Database / PostgreSQL / Neon** — where information is stored permanently.
  *PostgreSQL* is a popular database; *Neon* is a rented, cloud version of it.
- **Schema** — the **blueprint** of the database: which tables exist and what each
  stores.
- **Migration** — a recorded change to that blueprint over time. *Analogy:* renovation
  records / version history for your database. **Why you cite "~20 migrations":** it
  proves the product kept changing as it met real use — not built once and abandoned.
- **ORM / Prisma** — a translator so you write normal code instead of raw database
  commands. *Analogy:* using your own language instead of the database's dialect.
- **Redis** — a very fast *temporary* memory store, used for queues and short-term
  memory. *Analogy:* a whiteboard (fast, wiped often) vs the filing cabinet (the
  database).
- **Vercel / Render** — services that **host** (run) your app on the internet so people
  can use it. **Deploy** = put your code live.
- **S3** — Amazon's file storage, for documents and images.
- **WebSocket** — a live, two-way connection so updates appear instantly without
  refreshing (e.g. notifications popping up).

---

## 4. Making it survive the real world (reliability) — your strongest FDE signals

- **Queue / Bull / job / worker** — a **to-do list for slow tasks.** Instead of making
  the user wait, you drop the task (a "job") onto a list (the "queue"), and background
  programs ("workers") do them later. *Bull* is the queue tool. *Analogy:* take a token
  at the bank and sit down, instead of freezing at the counter. **Why it matters:** a
  teacher entering 40 kids' scores can't wait on 40 slow AI calls.
- **Concurrency** — how many jobs run at once (you allowed 5 of one kind, 1 of another).
- **Timeout** — a maximum wait; if a task takes too long, stop instead of hanging
  forever.
- **Idempotency** — making sure doing the same thing twice doesn't **double-count.** You
  gave each attempt a unique ID, so if it's sent twice by accident, it's only saved
  once. *Analogy:* a ticket/reference number so the same payment isn't charged twice.
  Say it as: "unique IDs so a retry can't create duplicates."
- **Graceful degradation** — if a fancy part fails, the system still works in a simpler
  way instead of crashing. *Your example:* if the AI service is down, the report still
  comes out, just without the AI extras. *Analogy:* a broken escalator is still stairs —
  you can still get up.
- **Failure isolation** — stopping a crash in one part from taking down everything else.
- **Retry with exponential backoff** — if something fails, try again — waiting **longer
  each time** (1s, then 2s, then 4s…) so you don't hammer a struggling server. *Analogy:*
  knocking politely with longer pauses, not banging non-stop.
- **Offline-first** — built to keep working with **no internet**, then sync up later.
  *Why it's your best frontline point:* a worker on 2G in a warehouse basement is the
  same as a classroom with dropping wifi.
- **localStorage** — a small storage space inside the user's own browser that survives
  refreshing or closing the tab. You used it so unsent work isn't lost.
- **sendBeacon** — a browser trick to reliably send one last bit of data *even as the
  user closes the tab.* *Analogy:* dropping a letter in the mailbox on your way out.
- **Cold start** — the very beginning, when you have **no data yet.** *Why you mention
  it:* you can't train a machine-learning model with zero data, so rules were the right
  first choice.

---

## 5. Adaptive learning engine (the literacy app)

- **Rule-based adaptive engine** — the part that makes the game **harder or easier**
  based on how the child is doing, using **fixed rules** (not AI). Say it as: "if they
  get 80% right and answer fast, level up; if they miss three in a row, level down."
- **Mastery criteria** — your fixed definition of "they've learned it": **≥80% correct,
  under 4 seconds each, fewer than 20% confusion errors.** Plain version: "I defined
  'mastered' as a real, measurable bar, not a gut feeling."
- **Confusion-pattern detection** — spotting *specific* mix-ups like **b/d** or **p/q**
  (letters that look alike), instead of just marking the answer wrong. *Why it's clever:*
  it tells the teacher *why* the child erred, which is a known dyslexia signal.

---

## 6. Logging in and staying safe (auth & security)

- **Auth (authentication)** — proving who you are to log in.
- **PIN auth** — logging in with a short number instead of email + password. *Why:* a
  four-year-old can't type an email. This was a **design decision**, not a shortcut.
- **JWT (token)** — a digital **wristband** that proves you're logged in, so you don't
  re-enter your password on every action. *(Full name: JSON Web Token — you don't need
  the full name.)*
- **bcrypt / hashing** — storing passwords **scrambled one-way**, so even if the
  database leaks, the real passwords aren't exposed. *Analogy:* storing a locked box, not
  the key.
- **RBAC (role-based access control)** — different users can see and do different things
  based on their **role** (teacher vs parent vs admin). Say it as: "six roles, each with
  its own permissions."
- **Audit log** — a record of **who did what, when, and from where (IP address)**, for
  accountability. *Analogy:* a security logbook.
- **DPDP / FERPA** — **data-protection laws** (DPDP = India's; FERPA = the US student-
  records law). Mentioning them means "I handled personal data carefully and legally" —
  important because your users were children.
- **RCI (Rehabilitation Council of India)** — the body that **certifies special
  educators.** You tracked whether their certification was still valid — a specific,
  India-only compliance detail that shows you built for the real system.

---

## 7. Voice & speech (Hunar's whole world — know these cold)

- **ASR (automatic speech recognition) / STT (speech-to-text)** — software that turns
  **spoken words into text** (what happens when Siri "hears" you).
- **WER (word error rate)** — how often speech-to-text **gets words wrong.** Lower is
  better. **Odia at ~35% WER** means it mis-hears about **1 word in 3** — that's why you
  can't trust it and must design around it. This single number drives your whole #3
  design. Say it as: "the speech recognition is wrong a third of the time in Odia, so I
  never make the worker's outcome depend on it being right."
- **TTS (text-to-speech)** — the reverse: software that **reads text aloud** in a voice.
  Your IEP "read-aloud" feature used this.
- **Hybrid voice architecture** — Hunar's approach of processing the raw *audio* (tone,
  pauses, interruptions) instead of instantly flattening it to text. Plain version:
  "they keep the *voice*, not just the words, because how something is said carries
  meaning."
- **Voice biometrics / voice-print** — recognizing a person **by their voice**, like a
  fingerprint made of sound.
- **SSE (server-sent events)** — a way for the server to **stream** updates to the screen
  continuously; it's the plumbing behind word-by-word streaming.
- **IVR** — the **"press 1 for…"** automated phone menus.
- **USSD** — the **`*123#`** codes on basic phones (like checking your balance). Works
  **without internet or a smartphone** — useful for the "Kill the App" challenge.

---

## 8. Product & estimation words (mostly for Challenge 5)

- **Human-in-the-loop** — a **person reviews or approves** the AI's output before it
  counts. Your core safety principle. *Example:* a senior educator must approve every
  AI-drafted goal.
- **Escalation** — passing a hard case **up to a human/senior** to handle.
- **Tiering** — sorting into **levels**: Tier 1 = on track, Tier 2 = at risk, Tier 3 =
  high risk.
- **Funnel** — start with a **big number and narrow it down** step by step to reach an
  estimate. *Analogy:* a filter that keeps removing people who wouldn't buy.
- **Top-down vs bottom-up** — *top-down:* start from the whole market and divide down.
  *bottom-up:* build up from individual buyers. Doing both and checking they roughly
  agree = a **cross-check.**
- **Take-rate** — what **percentage** of buyers choose a particular option (e.g. "2% of
  car buyers pick the special edition").
- **Sensitivity analysis** — checking **how much your answer changes if your assumption
  changes.** Say it as: "if the take-rate is 1% the answer is ~200; if it's 4% it's
  ~2,000 — so I quote a range, not a fake-precise number."
- **TAM (total addressable market)** — **everyone who could possibly buy** the thing (the
  top of the funnel).
- **Instrument demand** — instead of *guessing* how many will buy, **measure it for real**
  with refundable pre-orders/deposits, then build to the confirmed number. This is the
  standout answer for Challenge 5 (and it's what Mahindra actually did).

---

## 9. The 8-word version of each big idea (last-minute scan)

- Deterministic = fixed rules, no guessing (a calculator).
- LLM = the language AI (ChatGPT's engine).
- Agent = an AI that works in steps.
- LangGraph = building that agent as a flowchart.
- Queue = a to-do list for slow tasks.
- Idempotency = doing it twice can't double-count.
- Graceful degradation = if AI dies, basics still work.
- Offline-first = keeps working with no internet.
- WER = how often speech-to-text mishears (lower is better).
- Human-in-the-loop = a person approves the AI's output.
- Take-rate = what % of buyers pick the option.
- Instrument demand = measure it with deposits, don't guess.
