# Research notes — field facts for Challenge #3

Everything here is sourced. Content rephrased for compliance with licensing
restrictions; no verbatim reproduction beyond short fragments.

Purpose: the pick rests on the claim that this answer will be *grounded* rather
than plausible. These are the facts that make it grounded. Each one is paired
with its design implication, because a fact without an implication is trivia.

---

## 0. The grounding customer

Multi-plant apparel / garment manufacturer, ~100,000 workers, migrant-heavy,
majority women, Bengaluru + Tirupur style clusters. Wages = piece rate /
production incentive + attendance incentive − statutory deductions.

Why this is real: research on Bengaluru's garment industry documents young
female migrant workers who do not speak Kannada, the local language, leaving
them isolated and vulnerable — and earning less than what a recruiting agent had
promised them, once rent, electricity and water were taken out.
→ [Clean Clothes Campaign](https://cleanclothes.org/file-repository/resources-publications-labour-without-liberty-2013-female-migrant-workers-in-bangalores-garment-industry-short-version/@@download/file)

**Design implication:** the literacy problem is inseparable from a *language*
problem and a *migration* problem. A worker can be fully literate in Odia and
functionally illiterate in her workplace. Also: the gap between promised pay and
received pay is created at hiring and detonates on payday. Onboarding and salary
are the same problem.

---

## 1. The strongest fact: ASR is not ready for the languages that matter

A benchmark across 10,934 audio recordings and up to 10 ASR models per recording
found Hindi performing best at about **16.2% WER**, while **Odia was hardest,
with the best result around 35.1% WER** and only when speaker diarization was
applied.
→ [Benchmarking ASR for Indian Languages in Agricultural Contexts (arXiv 2602.03868)](https://arxiv.org/html/2602.03868v2)

State-of-the-art Indic ASR models degrade badly on low-resource dialects and
language varieties, including ones closely related to languages seen in
pre-training.
→ [Cross-Lingual ASR Transfer for Low-Resource Indic Varieties (arXiv 2601.04373)](https://arxiv.org/html/2601.04373v1)

Counter-nuance worth one line in the video: strict single-reference WER
over-penalises natural spelling variation and code-mixed English words, so WER
paints a bleaker picture than what users actually perceive.
→ [Orthographically-Informed Evaluation (arXiv 2603.00941)](https://arxiv.org/html/2603.00941v1)

Existing Indic benchmarks lean on scripted, clean speech, which encourages
dataset-specific overfitting and hides real-world performance.
→ [Voice of India benchmark (arXiv 2604.19151)](https://arxiv.org/html/2604.19151v1)

**Design implication — this is the load-bearing one.** Roughly one word in three
misheard for an Odia-speaking migrant means: *never require open-ended speech
for anything consequential.* The architecture has to be
- closed vocabulary for anything that changes a record
- confirm-by-repeat-back before any commit
- DTMF keypad and missed-call as first-class equals, not fallbacks
- open speech allowed only where a mistake is cheap and recoverable

This is the single most differentiating point available. Most submissions will
say "voice-first" and stop. Saying "voice-first, and here is why naive voice
fails at 35% WER, and here is the architecture that survives it" is the answer.

---

## 2. Biometric attendance is a trap

Aadhaar biometric authentication runs roughly **312 million attempts per month,
of which about 20.3 million fail — a ~6.5% failure rate**, effectively unchanged
for over a decade, with success rates sitting between 93.5% and 95%.
→ [Policy Circle](https://www.policycircle.org/opinion/aadhaar-authentication-failures/)

A study of Andhra Pradesh's PDS attributed about **92% of authentication
failures to biometric mismatch** — the leading cause in the state.
→ [ISB Bharti Institute](https://www.isb.edu/faculty-and-research/bharti-institute-of-public-policy/aadhar-authentication-failure-in-public-distribution-system-of-andhra-pradesh)

In Telangana, worn-down fingerprints were reported as the cause behind roughly
**36% verification failure** in a major government scheme, with rural workers
denied access to benefits as a result. Reporting on Mundoti, Rajasthan similarly
found fingerprints worn down by agricultural labour causing verification
trouble, varying by age, gender and occupation.
→ HuffPost India archive (paraphrased, no verbatim) and
  [Lattice Science Publication](https://www.journals.latticescipub.com/index.php/ijssl/article/view/609)

MPs across party lines have raised faulty fingerprint and iris scans blocking
access to PDS rations and MGNREGA work.
→ [Biometric Update](https://www.biometricupdate.com/202507/high-rates-of-aadhaar-biometric-verification-failure-leads-to-uidai-scrutiny)

**Design implication:** the work destroys the credential. Hands that stitch,
cut, load and dye all day produce degraded fingerprints — so a fingerprint
attendance system fails hardest on exactly the workers it is meant to serve, and
fails as a *wage* event, not a UX event. Any attendance design must have a
non-biometric path that does not require a supervisor's favour, because the
moment attendance failure is resolved by asking a supervisor, you have created a
rent-seeking opportunity.

---

## 3. Access is not ownership — and it breaks identity

In India roughly **71% of men own mobile phones versus 38% of women**.
→ [Yale EGC](https://egc.yale.edu/research/pande-and-coauthors-understanding-barriers-and-impacts-womens-mobile-phone-adoption-india)

A related finding: the gender gap in *access to any* mobile phone is about 14%,
**much smaller than the gap in ownership**.
→ [Yale Inclusion Economics](https://www.ie.yale.edu/news/171227/can-india-answer-call-addressing-gender-gap-mobile-phone-access)

Women are around 20% less likely to own a smartphone and more likely to borrow
one from a male family member; boys are ~1.5x likelier to own a mobile and ~1.8x
likelier to own a smartphone than girls.
→ [UNFPA India](https://india.unfpa.org/en/news/india-needs-double-down-bridging-its-digital-gender-gap)

**Design implication:** for a majority-female garment workforce, the number on
file frequently belongs to a husband, father or brother. Consequences the design
must handle explicitly:
- you cannot assume the person who answers is the worker
- salary information is *sensitive* — reading out her pay to whoever picks up is
  a real harm, not a privacy technicality
- authentication cannot rest on "possession of the handset"
- an outbound call at the wrong hour reaches a household, not a person

Almost nobody will address this. It is a genuine differentiator.

---

## 4. Help-seeking is the actual behaviour, not a failure mode

A mixed-methods study combining interviews with a survey of **604 women informal
workers** (domestic work, street vending, tailoring) found a marked **"language
penalty" for non-English readers** across every domain except social media —
and, importantly, that **help-seeking was mostly a positive predictor of digital
confidence rather than a marker of deficit**.
→ [Springer, J. Computer Science & Tech (2026)](https://link.springer.com/article/10.1007/s40012-026-00432-4)

**Design implication:** stop designing for a lone worker and a device. Assisted
use is normal and healthy. So the product should make assistance *safe* instead
of pretending it away: a "explain this to my friend" mode, shareable voice notes
a peer can replay, and — critically — an audit trail so that assistance cannot
quietly become impersonation. This reframes the whole trust section.

---

## 5. Voice services for oral populations have real precedent

Voice-message services where users call a number to record and hear messages in
their own language have been deployed widely and have had substantial impact in
marginalised, low-resource communities — a body of work described as the
"Internet of the Orals."
→ [Communications of the ACM (2019)](https://cacm.acm.org/magazines/2019/11/240382/fulltext)

IVR has been found genuinely useful for poorly literate and non-tech-savvy
populations because the phone interface is familiar.
→ [IIT Delhi / ACM DEV](http://www.cse.iitd.ernet.in/~aseth/visually_impaired.pdf)

But conventional IVR systems fail to capture what users actually want and present
a rigid interface, which is why they are widely experienced as frustrating.
→ [IIIT-Delhi technical report](https://repository.iiitd.edu.in/xmlui/bitstream/handle/123456789/29/IIITD-TR-2011-008.pdf?isAllowed=y&sequence=1)

Where teledensity is high and literacy is low, voice backed by ASR and TTS is an
effective delivery channel for services.
→ [Open Source For You](https://www.opensourceforu.com/2016/04/developing-an-interactive-voice-response-system-ivr/)

**Design implication:** the precedent validates voice but indicts *menu trees*.
The design is not "press 1 for attendance." It is an agent that already knows
why it is calling, states its purpose in one sentence, and asks one question.
Rigid IVR is the thing being replaced, not the thing being adopted.

---

## 6. Wage opacity is currently causing unrest — the commercial argument

During the April 2026 Noida factory protests, a worker told PTI that his payslip
did not reflect the hours he worked: 12 to 14 hour days, with overtime paid on
only three hours beyond his eight-hour shift, on a monthly income of roughly
₹13,000.
→ [Yahoo/PTI](https://ca.news.yahoo.com/does-one-survive-factory-protests-222531761.html)

The Noida agitation, beginning 8 April 2026 and spreading across sector belts
before turning violent, centred on minimum wage, working conditions and overtime
pay, in an industrial township with over 10,000 factories and service units.
→ [Indian Express](https://indianexpress.com/article/explained/rising-costs-stagnating-wages-why-workers-are-protesting-in-india-10636950/),
  [The Hindu Frontline](https://frontline.thehindu.com/columns/noida-workers-protest-labour-codes/article70924552.ece)

A parliamentary committee summary notes employees being made to suffer even
though statutory deductions had in fact been taken from their salaries.
→ [PRS India](https://prsindia.org/policy/report-summaries/compliance-with-the-prescribed-provisions-of-deduction-and-deposit-of-pf-esi-and-tds-by-the-employers)

Workers routinely do not understand ESI deductions appearing on their slips —
the "why is ₹360 being taken from me every month" question shows up repeatedly
in public forums.
→ [Quora thread on ESI deductions](https://www.quora.com/What-are-the-benefits-of-ESI-Every-month-Rs-360-is-being-deducted-from-my-salary-for-ESI-Can-someone-help-me-understand-it)

**Design implication:** this converts the salary sub-question from a UX nicety
into a risk-and-retention argument the customer's CHRO will actually fund. The
product's job is not to *display* a payslip. It is to answer one question —
"why is this month different from last month?" — before the worker has to ask,
in her language, in her own arithmetic. Unexplained variance is the trigger.

---

## 7. Attrition and absenteeism — why the customer pays

Absenteeism and attrition are treated in the literature as an existential
productivity problem for garment factories, with working environment,
relationships, employer-provided facilities and job satisfaction identified as
the major drivers of absence.
→ [Study on absenteeism in garment industry (ResearchGate)](https://www.researchgate.net/publication/359836076_A_STUDY_ON_EMPLOYEE_ABSENTEEISM_IN_GARMET_INDUSTRY),
  [Study on attrition and absenteeism, Odisha garment industry](https://www.ijprems.com/ijprems-paper/a-study-on-the-attrition-and-absenteeism-in-the-garment-industry-of-odisha)

Worker attrition is being described as a threat to India's broader manufacturing
ambitions.
→ [Livemint](https://www.livemint.com/industry/worker-attrition-manufacturing-china-labour-factory-jobs-odisha-farm-plfs-employment-iit-bombay-world-bank-tamil-nadu-11753282264097.html)

One industry line captures it: machines are available, operators are not.
→ [Multi Innovation Journal](https://www.multiinnovationjournal.com/assets/archives/2019/vol1issue4/1-4-12-848.pdf)

**Design implication:** every one of the five sub-answers must land on a metric
the customer already tracks — day-30 and day-90 retention, absenteeism rate,
time-to-productivity, payroll query volume, grievance escalation rate. That is
what turns an empathy answer into a business answer.

---

## 8. Facts I still want but will proceed without

Flagging honestly rather than inventing:

- hard numbers on shared-handset rates *inside* garment factories specifically
  (as opposed to general Indian gender gap data)
- published day-30 attrition figures for Indian garment manufacturing
- measured completion rates for voice-based vs text-based worker onboarding

If any of these turn up, they strengthen the video. None of them are load-bearing
for the argument as constructed.

---

## 9. The five best lines to actually say out loud

Ranked by how much they differentiate:

1. Odia ASR sits near 35% word error rate. A third of her words come back wrong.
   So the design never lets open speech touch anything that matters.
2. The work destroys the fingerprint. Biometric attendance fails hardest on the
   workers who most need attendance to be correct.
3. The phone is often not hers. Reading her salary to whoever answers is a harm.
4. Asking a friend for help is not the failure mode. It is the interface.
5. She does not want her payslip. She wants to know why this month is different.

---
---

# Addendum — second research pass

Added after a senior-FDE self-review found four evidence gaps, two of which
change the design rather than decorate it. Section 8 above listed facts I was
proceeding without; this closes most of them and opens one new problem.

---

## 10. Contract labour — the structural fact I had missed entirely

By 2015, contract workers accounted for about **38% of total employment at Indian
manufacturing firms with more than 100 workers**, up from roughly 20% in 2000.
→ [NBER w29151](https://www.nber.org/papers/w29151),
  [World Bank](https://thedocs.worldbank.org/en/doc/6cc843232d05fb4b153e56e5eaf2eb0a-0050022022/original/Contract-Labor-and-Firm.pdf)

Firms hire contract workers partly as **strategic leverage against unionised
regular workers**, to hold down bargaining power and wage demands — a channel
whose strength varies with firm size, capital intensity and existing contract
intensity.
→ [IGC / Kapoor & Krishnapriya](https://www.theigc.org/sites/default/files/2017/05/Kapoor-and-Krishnapriya-working-paper-2017.pdf)

On contract labour in Ahmedabad's textile industry: these workers are effectively
invisible to the outside world, records are kept properly by neither industry nor
government, and unions have not historically prioritised them.
→ [Contract Labour in Ahmedabad Textile Industry](https://www.researchgate.net/publication/325680676_Contract_Labour_in_Ahmedabad_Textile_Industry)

**Design implication — this breaks the salary wedge for ~38,000 of 100,000
workers.** If a contractor runs their payroll, the principal employer cannot
explain a wage it does not compute, and the AI cannot read out a figure it cannot
see. Worse, the population it fails is the *most* precarious one.

Three consequences, all of which now appear in the design:
- the pilot runs on **directly employed workers only**, stated openly as a
  limitation rather than buried
- **contractor payroll data access becomes a contractual precondition** for phase
  two, not a technical afterthought
- week-one discovery must establish what share of the roster is contract labour
  and whether that data is reachable at all

This is the difference between a design and a deployment plan. I did not have it
in the first pass.

---

## 11. Unions — the stakeholder I had ignored

The Garment and Textile Workers Union (GATWU) is an active, organised presence in
Bengaluru's garment industry, working from the workstation outward to the factory
gate and into wider social and transnational spaces.
→ [Building a labour countermovement in Bangalore's garment industry](https://www.tandfonline.com/doi/abs/10.1080/13604813.2014.962894)

GATWU reports roughly **4 lakh Karnataka garment workers on a minimum wage of
about ₹13,000/month, nearly 30% below several other industries**, and criticised
their exclusion from a state wage revision — noting revisions have been unfair for
close to 40 years.
→ [Times of India](https://timesofindia.indiatimes.com/city/bengaluru/textile-workers-union-slams-karnataka-govt-for-exclusion-from-wage-revision/articleshow/131294323.cms),
  [Bangalore Mirror](https://bangaloremirror.indiatimes.com/bangalore/others/wage-hike-sparks-relief-among-karnataka-workers/articleshow/131355726.cms)

Reported gains — reduced harassment, fairer wages, enforcement of maternity and
overtime rights — have come **wherever union presence is strong**.
→ [Bangalore Mirror](https://bangaloremirror.indiatimes.com/bangalore/others/behind-bengalurus-seams-women-power-citys-global-garment-hubs/articleshow/124588113.cms)

GATWU, with Alternative Law Forum, has documented **forced resignations** in the
sector.
→ [GATWU / ALF via Business & Human Rights Resource Centre](https://media.business-humanrights.org/media/documents/English_GATWU_ALF_Forced-resignations1.pdf)

**Design implications, two of them significant:**

1. **The ₹13,000 figure in my script is now sourced**, and it is the actual
   Karnataka garment minimum wage rather than a plausible invention.
2. **"The AI never delivers termination or discipline" now has an evidence base.**
   Forced resignation is a documented practice in this sector. A system that
   cannot be pointed at a worker to pressure an exit is a *safeguard*, and it
   should be a written commitment a union can hold the employer to — not a design
   preference I happen to hold.
3. **Unions are a distribution ally, not an obstacle.** An AI that explains wages
   accurately wants what they want. Brief them before launch, give them aggregate
   (never individual) visibility into wage-query and grievance volumes, and the
   rollout gains legitimacy that no amount of product polish can buy.

Designing a wage-communication system for this workforce without a union strategy
was naive. Correcting it.

---

## 12. Face recognition — what the evidence actually supports

NIST's Face Recognition Vendor Test programme documents demographic differentials
in Parts 3 and 8 (NISTIR 8280, NIST IR 8429), reporting results split by sex and
age band with false non-match rate estimates and uncertainty ranges per
demographic. NIST also notes that FNMR variation across datasets is driven
primarily by **image quality and ageing differences**, and that differentials vary
substantially **between algorithms**.
→ [NIST FRVT Demographics](https://pages.nist.gov/frvt/html/frvt_demographics.html),
  [NISTIR 8280](https://pages.nist.gov/frvt/reports/demographics/nistir_8280.pdf),
  [NIST IR 8429](https://nvlpubs.nist.gov/nistpubs/ir/2022/NIST.IR.8429.ipd.pdf),
  [NIST summary](https://www.nist.gov/news-events/news/2019/12/nist-study-evaluates-effects-race-age-sex-face-recognition-software)

**Design implication — I was wrong to recommend face recognition.** In the first
pass I demolished fingerprints with hard numbers and then endorsed face on pure
assertion. The evidence does not support endorsing *any* modality from a
distance, because performance is algorithm-specific and quality-driven, and a
6am shift change in poor light with headscarves is close to a worst case for
image quality.

What the evidence *does* support is a **selection procedure**:
- measure false non-match rate at this customer's own gates for two weeks
- disaggregate by cohort and by shift hour, never report the average
- choose the algorithm and modality on measured performance, not on a datasheet
- guarantee a non-biometric path regardless of which modality wins
- treat a rising per-cohort FNMR as a system defect under SLA

That is a stronger answer than the one I replaced. "I pick the modality from two
weeks of measurement at their gate, not from a brochure" is the FDE position.

---

## 13. Cost of voice — my first model was optimistic by more than 2x

Indian voice AI pricing starts around **₹2/min on self-serve tools**, with
enterprise contracts often unpublished.
→ [MyOperator](https://myoperator.com/blog/top-10-voice-ai-agents-india-2026)

One breakdown puts the practical range at **₹2 to ₹12 per minute once the fees
that don't get quoted are included**.
→ [eCorpIT](https://ecorpit.hashnode.dev/ai-voice-agent-costs-in-india-in-2026-2-to-12-a-minute-plus-7-fees-nobody-quotes)

Globally, self-serve platforms run about **$0.05–0.35/min**, with most production
deployments landing between **$0.12 and $0.25/min** once every component is
billed; enterprise platforms frequently do not price per minute at all.
→ [Kommunicate](https://www.kommunicate.io/blog/ai-voice-agent-pricing/)

**Design implication:** my original ₹2.5/min blended figure was the self-serve
floor, not a production number. Revised model uses **₹6/min central, ₹4–8
sensitivity**, and separately prices the human escalation layer I had promised and
never costed. Full revised model in `07-qa-prep.md` §A1, now framed as
**breakeven** rather than as an ROI multiple, because the ROI numerator rested on
two figures I invented.

---

## 14. Still missing after two passes

Honest ledger:

- **Outbound answer rates** for this population. Not found. Treated as an
  explicit assumption (55%) and flagged as the largest sensitivity in the cost
  model.
- **Published day-30 attrition** for Indian apparel manufacturing. Still not
  found. The cost case is therefore expressed as breakeven attrition-point
  movement rather than as a promised return.
- **Replacement cost per garment worker.** Assumed ₹8,000, labelled as needing
  the customer's actual figure.
- **Shared-handset rates inside garment factories specifically.** Still
  extrapolating from national gender-gap data. Remains a genuine gap.
