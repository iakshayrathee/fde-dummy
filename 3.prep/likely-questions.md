# Likely questions — crib sheet

Ten questions, ranked by probability × damage. One tight answer each. **Learn the shape, not the words** — reciting
this verbatim is worse than answering it badly in your own voice.

The first six are the gaps an independent reviewer found in the submission. Assume a sharp interviewer finds them too.

---

### 1. "Does the driver even want a manager? Most of them took this job to get away from having a boss."

**The most dangerous question, and the correct one.**

> "That's the objection I'd put first, and I got to it late. 'No boss' isn't a side effect of gig work — for a lot of
> riders it's the feature.
>
> The distinction I'd hold the design to is that a boss has authority *over* you; this has authority *for* you. And
> the test is whether he can tell it to shut up. A boss, you can't. If he can silence it mid-sentence and it still
> files his claim and still calls the customer, it isn't supervision — it's staff. He's not getting a manager, he's
> getting a manager *of his own*, which only salaried people have ever had.
>
> So default intensity is minimal — money and exceptions. Everything else is opt-in, changeable by voice. And the
> primary metric is volition: what share of shifts does he *choose* to talk to it. If most riders pick quiet mode,
> that's the finding and the product narrows to money and exceptions. I'd rather build the small true thing."

### 2. "The collective is a union in software. What happens the first time it files against our client on pay rates?"

> "It doesn't, and that's architected rather than promised. The case-filing tool has an allowlist of case types —
> operational friction only. Time lost, unsafe locations, broken process, bad data. Rate aggregation isn't a
> capability that exists.
>
> The reasoning is what I'd want you to hold me to. Friction cases are Pareto — the warehouse delay costs you money
> too, so they actually get resolved. Rate cases are distributive: one side gains what the other loses, and the first
> one filed gets the whole product switched off, at which point the riders lose the friction cases as well. **Scoping
> it narrowly is the thing that protects it.**
>
> And the agent says the limit out loud: *I can't take up pay rates, and I'd rather tell you than pretend.* An agent
> that names its own limits is more credible than one that seems omnipotent."

### 3. "Voice as identity — what about account sharing?"

> "It breaks it overnight, and that's the second-order effect I'd surface in week one rather than month six.
>
> Account renting is widespread and for some riders it's load-bearing — illness, family emergency, a brother earning a
> second income. So voice-ID is a *policy* decision wearing an *authentication* decision's clothes.
>
> I wouldn't ship it as enforcement first. Ship it as convenience — no password — with soft verification, measure the
> real sharing rate, and bring you the number with options. My guess is the data shows a rational response to a real
> need, and the right answer is a sanctioned substitute-rider flow rather than a better lock. Fraud you design out;
> need you design for."

### 4. "You're scoring the agent on driver earnings. Won't it just push people to over-work?"

> "Yes, if I only did that. Goodhart applies to my scorecard as much as to yours.
>
> So every optimised metric is paired with a guardrail that's monitored and never optimised. Earnings per hour is
> paired with hours worked and fatigue incidents. Retention is paired with a sampled, human-rated honesty audit — did
> it tell people uncomfortable truths, or did it just get reassuring. Progression is paired with attention
> distribution so it can't win by cherry-picking the easy promotions. And overrule rate is paired with appeal rate,
> because a low overrule rate achieved by discouraging appeals is a failure.
>
> Two structural rules: the scorecard is capped, not maximised. And cohort assignment is random — the agent never
> picks its drivers."

### 5. "Our legal team will say this creates an evidence trail about working conditions."

> "They're right, and I'd rather say that than dodge it.
>
> Two things. First, the exposure exists whether or not you measure it — what changes is whether you find out first or
> in a summons. Documented friction you *fixed* is a defence; undocumented friction that a plaintiff reconstructs
> isn't.
>
> Second, regulation is moving toward mandated transparency on allocation, scoring and deactivation. Reason strings on
> every decision, named-human termination, real appeal paths, replayable audit — that *is* substantially the
> compliance posture that's coming. You can build it now as product or retrofit it later against someone else's
> deadline.
>
> Week one, in writing: retention periods, legal hold, and whether the driver's record is discoverable. My view is it
> should be his."

### 6. "Who owns the city graph?"

**No good answer prepared. Say so.**

> "Honestly — that's the gap in my thinking. I called it the moat and didn't work out who owns it. You'll say it's
> your operational data; I'd argue the fleet-level knowledge is what makes the product work across customers, and the
> driver-level record should belong to the driver.
>
> That negotiation is probably worth more than the contract, and I don't want to invent a position on it in an
> interview. It's the first thing I'd want to be briefed on."

---

### 7. "We're paying for this. Why does it work for the driver?"

> "Attrition is your largest controllable cost — thirty crore of annual exposure at your scale. The only thing that
> reduces it is him believing the agent is on his side, and belief requires visibly acting against you sometimes. The
> loyalty flip *is* the ROI mechanism. It isn't charity you tolerate, it's what you're buying."

### 8. "How is this different from our dispatch system with a nicer voice?"

> "The scorecard. It's reviewed on his earnings per hour, his ninety-day retention and his progression — never on
> throughput. Loyalty in a system prompt is cosplay; loyalty in the objective function is structural. If throughput
> goes on the agent's scorecard, you've rebuilt the dispatcher with a friendlier voice.
>
> Which is why I'd concede audit rights and reporting, and never concede the objective function."

### 9. "Why can't we build this ourselves?"

> "You can build the voice — voice is commoditising. You can't build **neutrality.** An in-house agent is the
> company's agent by construction, and no rider will believe the thing built by the people who pay him is on his
> side. He'd be right not to.
>
> The trust that moves the attrition number is only available to a third party whose scorecard the driver can be shown
> and whose overrule rate is audited outside your walls. Neutrality is the product, and it isn't technical."

### 10. "Which part of this is most likely to fail?"

> "The authority grant. Nobody hands software a budget on day one — which is exactly why the wedge is scoped to the
> one exception where the ROI is impossible to argue with.
>
> And the harder version of the same fight: you'll want throughput on the agent's scorecard. That's the conversation
> that decides whether this is the product I described or a dispatcher with a voice."

---

---

## The most important answer on this page

A reviewer flagged that this crib sheet trains **defence** rather than **updating** — ten prepared rebuttals, one
admission. That's optimised for surviving an interrogation, and an interview isn't one. What a good interviewer most
wants to observe is you being *moved* by a better argument, and rehearsed answers actively prevent it.

So: **plan to change your mind about something, out loud.** Not as a tactic — genuinely. These three are the places
where you should be most willing, because the honest answer really is unsettled:

- **"Isn't the agent market over-engineered?"** → Yes. I'd cut it. It's the weakest of the seven and I only kept it in
  the write-up because it's structurally interesting.
- **"Why should the driver's record be portable if we paid to create it?"** → I have a values answer, not a commercial
  one. If you pushed, I'd probably concede it belongs at the platform layer rather than in your contract.
- **"Is quiet mode compatible with the collective?"** → I resolved this on paper — the pattern comes from passive
  telemetry, not conversation — but I'd want to check that against real dwell-time data before I asserted it to you.

**One sentence to have ready, and to mean:** *"That's a better argument than mine — let me change that."* If you say it
once and it's real, it does more for you than any of the ten answers above.

---

## Two rules for the conversation

**Rebuild your own numbers from memory.** Pick any figure in the pack — ₹6,000 replacement cost, 1.5 support
contacts/week, ₹15 margin/drop — and be able to say where it came from and what it's sensitive to. A polished
submission raises the bar you then have to clear live; hesitating on your own arithmetic is the fastest way to make
the artifact work against you.

**Say "I don't know" once, deliberately.** Question 6 is the natural place. It resolves any suspicion that the pack
was over-assisted, in about four seconds, and it's what the job actually sounds like.
