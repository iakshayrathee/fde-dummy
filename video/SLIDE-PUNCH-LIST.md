# Slide punch list — merged_presentation.pptx

Read from an actual inspection of your deck, not from the plan. 32 slides, 16:9
(13.33 × 7.5 in). Correct size, correct count.

**What's already working:** cold-open audio embedded on slide 1 · opening on-camera
video embedded on slide 6 · text on ~24 slides matches the script · sensible extra
design work on slides 21, 27, 28.

**What's blocking:** 2 of your 3 call audio files aren't in the deck at all, one
slide is missing entirely, no slide auto-advances, 5 placeholders are still visible,
and 3 source citations are attached to the wrong statistics.

---

## 1. BLOCKERS — fix these first

### B1. Two of three call audios are missing from the deck

Only `media1.mp3` is embedded, on slide 1. These two are sitting in `video\call\`
unused:

| File | Belongs on | Currently |
|---|---|---|
| `File 2 (A2 - Absence Call).mp3` | **a new slide** (see B2) | not in deck |
| `File 3 (A3 - Advocacy Call).mp3` | **slide 29** — the subtitle text is there but no audio | not in deck |

**Fix:** click the slide → Insert → Audio → Audio on My PC → pick the file → click the
speaker icon → **Playback** tab → Start: **Automatically**, tick **Hide During Show**.

### B2. The absence call has no slide — you're missing one slide

Your slide 17 is *"A dashboard tells her afterwards…"*. But in the script, the
absence call plays **before** that line. Right now there's nowhere for it to go.

**Fix:** insert a new slide between your current 16 and 17. Black background.
Subtitle text:

> "You're not at the gate. Taking leave? An unpaid day lowers your attendance bonus
> by about ₹250."

Attach `File 2 (A2 - Absence Call).mp3` to it. **Your deck becomes 33 slides** — that
is correct, my earlier count of 32 didn't allow for this one properly.

### B3. Nothing auto-advances — slides 1–5 will desync

No slide in the deck has an advance time set. For slides 1–5 this is fatal: the
20-second call plays while five different subtitles need to appear in sync.

**Fix, two parts:**

1. Slide 1 → click the audio icon → **Playback** tab → tick **Play Across Slides**
   and **Loop until Stopped: OFF**.
2. Select slides 1–5 → **Transitions** tab → untick **On Mouse Click** → tick
   **After** → set these values:

| Slide | After |
|---|---|
| 1 | 4.00s |
| 2 | 5.00s |
| 3 | 6.00s |
| 4 | 3.00s |
| 5 | 2.00s |

Total 20s. Play it once and nudge until each subtitle lands with the voice. **Do this
by ear — my numbers are a starting point, your recording's actual pacing wins.**

### B4. Closing video not filmed or not inserted

Slide 31 still reads `[PLACEHOLDER: INSERT ON-CAMERA VIDEO 2 HERE]`. You have
`myvideo1.mp4` and it's already used on slide 6.

**Fix:** film the closing clip (~38s, the "I wouldn't build all five" block — use the
**alternate take** in `again\04-video-script.md`). Same framing, same wall, same light
as clip 1. Insert on slide 31, play automatically, fill the slide.

### B5. Five placeholders still visible on screen

These will render into the exported video as literal text:

| Slide | Placeholder text to delete or replace |
|---|---|
| 2, 3, 4, 5 | `[PLACEHOLDER: AUDIO WAVEFORM]` |
| 11 | `[PLACEHOLDER: Add Graphic of a Blank Form…]` |
| 16 | `[PLACEHOLDER: 6-Bar Chart…]` |
| 18 | `[PLACEHOLDER: Two bars side by side…]` |
| 22, 23 | `[PLACEHOLDER: …photo of hands at a sewing machine…]` |
| 31 | `[PLACEHOLDER: INSERT ON-CAMERA VIDEO 2 HERE]` |

For slides 2–5, **just delete the text.** A black slide with a subtitle is fine and
matches slide 1's look. You don't need a waveform graphic on every one.

---

## 2. FACTUAL ERRORS — wrong sources on the wrong slides

These matter more than they look. An evaluator who knows the material will spot a
statistic credited to a study that doesn't contain it, and it undermines every other
number in the deck.

| Slide | Statistic | You have | Should be |
|---|---|---|---|
| **9** | ₹13,000/mo · 30% below other industries · Noida April 2026 | "Labour Bureau / News Reports" | **GATWU via Times of India** (wage) · **Indian Express / PTI** (Noida) |
| **14** | 6.5% Aadhaar failure · 36% Telangana | "NIST FRVT · NBER 2022" | **Policy Circle** (6.5%) · **HuffPost India** (36% Telangana) |
| **16** | face recognition bias varies by algorithm | *(none)* | **NIST FRVT** ← this is where NIST belongs |
| **20** | 38% women / 71% men own a phone | "NFHS-5" | **Yale EGC / Inclusion Economics** — unless you've personally verified NFHS-5 carries these exact figures |
| **28** | forced resignations | GATWU / Alternative Law Forum | ✅ correct, leave it |

NIST FRVT is a face-recognition study — it says nothing about Aadhaar fingerprints.
NBER w29151 is the contract-labour paper — it says nothing about biometrics. Those two
citations are currently on the wrong slide.

Full source list: `again\06-one-pager.md`, bottom section.

---

## 3. SLIDES THAT NEED ARTWORK

Three slides need a graphic. Ranked by how much they matter.

### Slide 16 — the bar chart · **most important visual in the deck**

Six vertical bars, different heights. A dotted horizontal line across them labelled
**"average — 6%"**. One bar coloured red, spiking well above, labelled **"this group
— 31%"**. Caption already present: *Never the average.*

**Already generated for you — just drag it in:**

- **`slide16-chart-dark.png`** ← use this one (black background baked in, matches your slides)
- `slide16-chart-alpha.png` — transparent version, only if your slide background isn't near-black

It's marked *"illustrative"* in the corner, because those six figures are an example
rather than measured data. Leave that marker on. It costs nothing and it stops the one
chart in your deck that isn't sourced from looking like it's pretending to be.

**Also add a source line to this slide: `NIST FRVT`.** This is the slide the NIST
citation actually belongs to.

### Slide 18 — the salary delta

Two vertical bars side by side. Taller = `₹13,100`, shorter = `₹12,480`. Bracket
between the tops labelled **₹620 less** (you already have that text). Below the gap,
optionally: `2 days absent = ₹520` and `PF = ₹100`.

**Already generated for you:**

- **`slide18-delta-dark.png`** ← use this one
- `slide18-delta-alpha.png` — transparent version

It already carries the ₹620 bracket and the `2 days absent − ₹520` / `into her PF −
₹100` breakdown, so you can **delete the "₹620 less" text box you already have** on
that slide — otherwise it'll appear twice.

Note the bars are scaled honestly from zero, so the gap looks small. That's correct —
₹620 out of ₹13,100 *is* small in proportion and large in her life. The bracket and
the label carry the meaning, and your narration does the rest.

### Slides 22, 23, 24 — the sewing machine photo

You have **two** sewing-machine slides (22 and 23) doing the same job. The script has
one photo slide, then the same photo with 8 languages beside it.

**Fix:** delete slide 22 entirely. Keep 23 (photo alone, no text) and 24 (photo + the
8 language names, which you already have). That gets you back in sync and removes a
redundant beat.

For the photo: a dark, close-up, over-the-shoulder shot of hands at a sewing machine.
No text on the image. Any free stock source is fine (Unsplash, Pexels). **Avoid a
smiling posed worker** — it undercuts the argument.

---

## 4. CONTENT TRIMS

### Slide 26 — too much text

You've added a paragraph: *"Systems that obscure their logic, speak only in
enforcement, and offer no recourse give workers every reason not to trust them…"*

That's not in the script and it's unreadable in the ~8 seconds this slide is on
screen. **Cut it. Leave only "Her distrust is rational."** One line, big. The
narration carries the reasoning.

### Slide 27 — wrong title

Titled **"The System's Contradictions."** These four items aren't contradictions,
they're the trust rules — the things the AI always does. Retitle to **"Four rules"**
or delete the title and let the four lines stand alone.

### Slide 28 — Before/After is extra

Your Before/After framing isn't in the script. It's not wrong, and it looks
considered — **keep it if you like it**, but drop the body text down to a few words
each so it's readable at a glance.

### Slide 32 — mislabelled

Currently: `Source: Forward Deployed Engineer — Challenge #3`. That's not a source.

**Fix:** the slide should read:

> **Can she state her own pay, unprompted, before payday?**
> *That's the only number I'd report.*
>
> `[Your Name] · Forward Deployed Engineer — Challenge #3`  ← small, bottom

The second line (*"That's the only number I'd report"*) is currently missing.

### Slide 9 — formatting artifact

Reads `₹13,000 / /month` — there's a stray slash. Should be `₹13,000/month`.

---

## 5. FULL SLIDE STATUS

| # | Content | Status |
|---|---|---|
| 1 | Cold open, subtitle 1 + audio | ✅ audio in · ⚠️ needs Play Across Slides + 4s advance |
| 2 | Subtitle 2 | ⚠️ delete placeholder · set 5s |
| 3 | Subtitle 3 | ⚠️ delete placeholder · set 6s |
| 4 | Subtitle 4 | ⚠️ delete placeholder · set 3s |
| 5 | Subtitle 5 "Oh… all right" | ⚠️ delete placeholder · set 2s |
| 6 | Your opening video | ✅ done |
| 7 | Reading is the accommodation / Listening is the baseline | ✅ done |
| 8 | She never composes / She only confirms | ✅ done |
| 9 | ₹13,000 · 30% · Noida | ⚠️ fix `/ /month` · fix source |
| 10 | Under one day of her wages, per year | ✅ done |
| 11 | Form + thumbprint + strike-through | ❌ needs graphic |
| 12 | THE CONTRACT waveform | ✅ done · ⚠️ add §7a subtext (*hers to replay · her voice is her key*) |
| 13 | A number can't be faked by nodding | ✅ done |
| 14 | 6.5% · 36% | ⚠️ **wrong sources** |
| 15 | The work destroys the fingerprint | ✅ done |
| 16 | Never the average + chart | ❌ needs chart · add NIST source |
| **NEW** | **Absence call + subtitle + A2 audio** | ❌ **missing slide — insert here** |
| 17 | A dashboard tells her afterwards… | ✅ done |
| 18 | ₹620 less + two bars | ❌ needs chart |
| 19 | PF is your money | ✅ done |
| 20 | 38% / 71% | ⚠️ verify source · ⚠️ add §7a subtext (*a shared handset never hears her pay*) |
| 21 | Accessibility & Control — 3 options | ✅ done · ⚠️ add §7a header (**Verified first — her voiceprint, or the gate at her line**) |
| 22 | Work & Dignity + photo | ❌ **delete this slide** |
| 23 | Sewing machine photo | ⚠️ add photo, delete placeholder text |
| 24 | Photo + 8 languages | ✅ done |
| 25 | I'd never measure completion | ✅ done |
| 26 | Her distrust is rational | ⚠️ **cut the paragraph** |
| 27 | Four trust rules | ⚠️ retitle |
| 28 | Forced resignations, Before/After | ⚠️ trim text, source ✅ |
| 29 | ₹340 overtime subtitle | ❌ **attach A3 audio** |
| 30 | Enforces = supervisor / advocates = manager | ✅ done |
| 31 | Your closing video | ❌ film it, insert it |
| 32 | Final question | ⚠️ add second line, fix "Source:" label |

**Count: 12 done · 12 need edits · 8 need real work · 1 slide to add · 1 to delete.**
Final deck = **32 slides** (33 minus the deleted slide 22).

---

## 6. DO IT IN THIS ORDER

1. **Film the closing clip.** It's the only thing that needs daylight and a set-up.
2. **Insert the missing absence-call slide** and attach A2 audio.
3. **Attach A3 audio to slide 29.**
4. **Delete slide 22.**
5. **Delete all remaining `[PLACEHOLDER…]` text.**
6. **Drop in the two generated PNGs** (slides 16 and 18) and find one sewing photo.
7. **Fix the three wrong citations** — 10 minutes, disproportionate payoff.
8. **Set the slide 1–5 timings by ear.**
9. **Record narration** — Slide Show → Record Slide Show, in chunks.
10. **Export**, then subtitle the English narration, then check the runtime is under
    5:00 by playing the file.

---

## 7. v3 — close the phone-channel gap + name the verification (do these)

Why this section exists: a senior reviewer's first two questions are *"how does a
worker who can't read prove it's her on a phone that isn't hers?"* and *"doesn't the
rest of your design assume a phone you just said 38% of women don't own?"* The design
doc already answers both; the deck didn't show it. These edits make the slides carry
the answer. No new slide, no renumbering — the deck stays as-is.

### 7a. Three slide edits (text only, ~10 minutes)

| Slide | Current | Add |
|---|---|---|
| **12** — THE CONTRACT waveform | label only | small subtext under the label: *hers to replay · her voice is her key* |
| **20** — `38%` / `71%` phone ownership | stat only | subtext: *the handset is often shared — so a shared handset never hears her pay* |
| **21** — Accessibility & Control, 3 options | the three delivery choices | a header line above the three options: **Verified first — her voiceprint, or the gate at her line** |

The move that ties it together: **the same measured gate that marks her present at
the line (the attendance modality) doubles as her identity at a line-side screen** —
so the kiosk needs no PIN she'd have to read. Voiceprint covers the phone; the gate
covers the kiosk. That's the whole verification answer, and it reuses attendance
infrastructure rather than inventing a new one.

### 7b. Re-record two narration blocks

The script (`again\04-video-script.md`) changed the **Onboarding** and **Salary**
SAY blocks. If you've already recorded narration, re-record just those two:

- **Onboarding** now ends the disclosure with *"the recording is the contract — hers
  to replay, and her voice on it becomes her key."* (drops the old "and she keeps
  it", which wrongly implied a personal phone).
- **Salary** now says *"nothing is spoken until it knows it's her — her voiceprint,
  or the gate that marks her present … so a shared phone never hears her pay. She
  chooses the channel."*

Net effect on runtime: +5s on Salary, bought back by three trims already applied in
the script. New total **4:51**, still under the cap.

### 7c. The two proactive calls (slides 17 and 29) are post-verification

`call2.mp3` (absence) and `call3.mp3` (advocacy) both speak a rupee figure. Under the
new rule, a proactive call says nothing about money until the voiceprint matches — so
in the story these are **already-verified** sessions reaching *her*, not an
unverified shared handset. You do **not** need to re-record them. If you want to make
it explicit, add one line of on-screen text to slides 17 and 29, bottom-left:
*"after voiceprint match"*. Optional, but it pre-empts the question.

### 7d. Optional: make verification its own slide

If you'd rather give the crux a dedicated beat, insert a black slide between the PF
slide (20) and the phone-ownership slide (21):

> **Nothing about her pay until it knows it's her.**
> *her voiceprint · or the gate at her line · a shared handset never hears her pay*

That makes the deck 33 slides and shifts everything after it by one — only do this if
you're comfortable renumbering. The 7a approach avoids that entirely and conveys the
same thing.
