# Production guide — shots, audio, checklist

Assumes: phone camera, a quiet room, free software. No crew. One day of work.

Tools that will do the job: **CapCut** or **DaVinci Resolve** (free) for edit and
burned-in subtitles, **Audacity** (free) for voice cleanup, **Canva** or **Google
Slides** for cards. Nothing else is needed.

---

## 1. Asset list

Script v2 reference: **604 narration words · 31s call audio · 4:48 runtime.**

| # | Asset | Type | Length | Notes |
|---|---|---|---|---|
| A1 | Cold-open salary call | audio | 20s | two voices |
| A2 | Absence + cost call | audio | 6s | one voice |
| A3 | Advocacy call (₹340 overtime) | audio | 5s | one voice |
| N1 | Narration, 8 blocks | audio | 253s | English, your voice |
| V1 | On-camera open | video | 25s | 0:20 beat |
| V2 | On-camera close | video | 38s | 4:07 beat |
| C1–C18 | Cards | stills | — | see section 4 |

---

## 0. The assumption I should have checked first

**This format assumes you can record credible Hindi.** I built the whole cold open
around it without asking, which was a mistake — it's the single most load-bearing
asset in the video.

If you can't, pick one. All three preserve the argument:

| Option | How | Cost |
|---|---|---|
| **Any other Indian language you do speak** | Swap Hindi for Tamil, Telugu, Bengali, Marathi, Kannada. Change one line in the frame from "migrant women" to name that state's workforce. | none — arguably better, since it's authentic |
| **Hindi TTS for both voices** | Use a Hindi TTS for the AI, and a second voice for Sunita's one line. Her line is four syllables. | none, slightly less warmth |
| **English audio, stated as a stand-in** | Run the calls in English and say once: "in production this is in her language." | costs the strongest thing in the video — last resort |

**Do not record Hindi you aren't fluent in.** An evaluator in this domain will hear
it immediately, and a video about respecting workers' languages that mispronounces
one is worse than a video that doesn't try. Getting a fluent friend to read the AI
lines is better than doing it yourself badly.

Either way: **have a Hindi or regional-language speaker check the Devanagari in the
script before you record.** I wrote it from knowledge, not from a native speaker's
review.

---

## 2. Recording the call audio

This is the part that carries the video, so it gets the most care.

**Two voices needed.** The AI voice and Sunita. Options, best first:

1. **Ask someone.** A woman who speaks Hindi naturally, for Sunita's two lines
   ("अच्छा… ठीक है" and nothing else). Ten seconds of her time.
2. **TTS for the AI voice.** Use any Hindi TTS — this is *correct*, not a
   shortcut. The agent is a machine and should sound like a competent one. Do not
   pick a breathy or over-friendly voice. Flat, clear, slightly slow.
3. **You record both** if no one is available. Pitch-shift is not needed; a
   different mic distance and pace is enough to separate them.

**Make it sound like a phone call, not a studio.** Three steps in Audacity:
- high-pass filter around 300 Hz, low-pass around 3,400 Hz (telephone band)
- add very light room noise or a faint line hiss underneath
- keep levels a touch lower than your narration so the cut to camera lifts

**Pacing matters more than accuracy.** Leave a real half-second pause before
Sunita's "अच्छा… ठीक है". That pause is the most persuasive moment in the video —
it is the sound of someone understanding her own payslip for the first time.

**Numbers must be spoken in full Hindi**, not digits read in English. ₹12,480
becomes "बारह हज़ार चार सौ अस्सी", not "twelve four eight zero".

---

## 3. Recording narration

- Phone earbuds with a mic, under a blanket, is genuinely fine. Room echo is the
  only thing that reads as amateur.
- Record **block by block**, not in one take. Six blocks, three takes each,
  pick the best. Far faster than chasing a perfect five-minute run.
- Stand up. It changes breath support and the read gets more authoritative.
- Watch the eight bolded lines in the script. Slow down, drop pitch, small pause
  after. Do not let them pass at conversational speed.

---

## 4. Cards

Dark background, one idea per card, type large enough to read on a phone. No
logos, no icons, no stock photography of smiling workers — that would undercut
the whole argument.

**The card list has moved.** All 24 cards, with their exact cue times and the C11
chart build note, now live in **`04-video-script.md` §4**, next to the words they
appear under. Keeping two copies in sync was a defect waiting to happen.

This file covers **technique only**: how to record the audio, how to make it sound
like a phone call, subtitling, assembly order and the pre-submit checklist.

---

## 5. Subtitles

**Burned in, not a sidecar track.** Two reasons: the evaluator may watch muted,
and hard subtitles are quietly on-theme for a submission about people who cannot
read the interface.

- Hindi audio gets **English** subtitles.
- English narration gets English subtitles too. Do not skip this. Partial
  subtitling looks like an oversight.
- Auto-generate in CapCut, then **read every line**. Auto-caption reliably
  mangles rupee figures and Hindi transliteration, which are exactly the words
  that matter here.
- White text, subtle dark scrim behind it, bottom third, never over a card's own
  type.

---

## 6. Assembly order

Work in this order — it front-loads the risky parts.

0. **Timing test before anything else.** Read all eight narration blocks aloud
   against a stopwatch, at the pace you actually intend to use. Script v2 budgets
   253 seconds. If you come in over 265, take the trims listed in the script *now* —
   not after you've recorded and edited. Version 1 of this script ran 35 seconds
   over a hard cap because nobody did this step.
1. Cut A1 (cold open) and get it to **20 seconds**. If this does not land, nothing
   else matters, so build it first.
2. Lay in N1 narration blocks against the timing ledger in the script.
3. Drop A2 and A3 into their beats.
4. Build cards to fit the audio that already exists — never the reverse.
5. Shoot V1 and V2 last, once you know exactly how much time is left.
6. Subtitle. Budget **90 minutes** for this. It always takes longer than expected.
7. Export: MP4, H.264, 1080p, 16:9.

---

## 7. Pre-submit checklist

- [ ] **Runtime is under 5:00 in the exported file**, checked by playing it — not
      read off the timeline, and not trusted from the script. Target 4:48.
- [ ] Devanagari lines **checked by a fluent speaker** before recording.
- [ ] Cold open starts at 0:00 with no title card and no introduction.
- [ ] Every statistic on screen carries a visible source.
- [ ] Subtitles present for **both** Hindi and English, with rupee figures correct.
- [ ] Audio levels consistent — call audio slightly under narration.
- [ ] Watch it once **muted**. It should still be followable.
- [ ] Watch it once on a **phone**. Card type must be readable.
- [ ] Filename: `Hunar-FDE-Challenge3-<YourName>.mp4`
- [ ] Uploaded, link set to **anyone can view**, tested in a private window.
- [ ] One-pager PDF attached alongside the link.
- [ ] Sent before **31 Aug 2026, 09:00 IST** — aim for 07:00.

---

## 8. If time runs short

Cut in this order, and only in this order:

1. Drop V1 and V2. Go full voiceover over cards. Costs the least.
2. Drop A3 (the advocacy call) and deliver that line as narration instead.
3. Drop C11 and C12 animations, use static cards.

**Never cut:** A1 the cold open, the burned-in subtitles, or the final silent
card. Those three are the submission's whole personality.
