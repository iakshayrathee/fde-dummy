"""Generates the two slide graphics.

Each is written twice:
  *-dark.png  - #0D0D0D background baked in. Use this one on your slides.
  *-alpha.png - transparent, if your slide background isn't near-black.
"""
from PIL import Image, ImageDraw, ImageFont

W, H = 1800, 1000
DARKBG = (13, 13, 13, 255)
WHITE = (255, 255, 255, 255)
GREY = (155, 155, 155, 255)
AXIS = (80, 80, 80, 255)
RED = (226, 66, 58, 255)
BAR = (225, 225, 225, 255)
BARDIM = (110, 110, 110, 255)


def font(sz, bold=False):
    for name in (("arialbd.ttf" if bold else "arial.ttf"),
                 ("Arial Bold.ttf" if bold else "Arial.ttf"),
                 "segoeui.ttf", "DejaVuSans.ttf"):
        try:
            return ImageFont.truetype(name, sz)
        except OSError:
            continue
    return ImageFont.load_default()


def rupee(f):
    try:
        return "\u20b9" if f.getmask("\u20b9").getbbox() else "Rs "
    except Exception:
        return "Rs "


def dashed(d, x0, x1, y, colour, width=5, dash=20, gap=18):
    x = x0
    while x < x1:
        d.line([(x, y), (min(x + dash, x1), y)], fill=colour, width=width)
        x += dash + gap


# ----------------------------------------------------------------- slide 16
def chart_cohorts(bg, path):
    img = Image.new("RGBA", (W, H), bg)
    d = ImageDraw.Draw(img)
    f_lab, f_val = font(34), font(38, True)
    f_note, f_avg = font(40, True), font(34, True)

    vals = [5, 6, 4, 31, 7, 5]
    labels = ["Group 1", "Group 2", "Group 3", "Group 4", "Group 5", "Group 6"]
    spike = 3

    left, right = 210, W - 330
    base, top, ymax = H - 200, 190, 35.0
    slot = (right - left) / len(vals)
    bw = slot * 0.44

    d.line([(left - 50, base), (right + 50, base)], fill=AXIS, width=3)

    for i, v in enumerate(vals):
        cx = left + slot * (i + 0.5)
        h = (v / ymax) * (base - top)
        hot = i == spike
        d.rectangle([cx - bw / 2, base - h, cx + bw / 2, base],
                    fill=RED if hot else BAR)
        # no value labels on the small bars: they collide with the average line
        # and the message is the shape, not the individual numbers
        d.text((cx - d.textlength(labels[i], font=f_lab) / 2, base + 28),
               labels[i], font=f_lab, fill=GREY)

    # average line, drawn last so it sits on top of every bar
    avg_y = base - (6 / ymax) * (base - top)
    dashed(d, left - 50, right + 50, avg_y, WHITE)
    d.text((right + 74, avg_y - 44), "average", font=f_avg, fill=WHITE)
    d.text((right + 74, avg_y + 6), "6%", font=f_avg, fill=WHITE)

    # callout above the spike
    cx = left + slot * (spike + 0.5)
    h = (vals[spike] / ymax) * (base - top)
    note = "this group: 31%"
    nw = d.textlength(note, font=f_note)
    d.text((min(max(cx - nw / 2, 20), right - nw), base - h - 74),
           note, font=f_note, fill=RED)

    # honesty marker: these are illustrative figures, not measured data
    d.text((left - 50, H - 68), "illustrative", font=font(26), fill=(105, 105, 105, 255))

    img.save(path)
    print("wrote", path)


# ----------------------------------------------------------------- slide 18
def chart_delta(bg, path):
    img = Image.new("RGBA", (W, H), bg)
    d = ImageDraw.Draw(img)
    f_val, f_lab = font(54, True), font(34)
    f_gap, f_break = font(50, True), font(34)
    R = rupee(f_val)

    last, this = 13100, 12480
    base, top, ymax = H - 230, 210, 14500.0
    cx1, cx2, bw = 560, 990, 220

    d.line([(380, base), (1170, base)], fill=AXIS, width=3)

    h1 = (last / ymax) * (base - top)
    h2 = (this / ymax) * (base - top)
    d.rectangle([cx1 - bw / 2, base - h1, cx1 + bw / 2, base], fill=BARDIM)
    d.rectangle([cx2 - bw / 2, base - h2, cx2 + bw / 2, base], fill=BAR)

    for cx, val, lab, h in ((cx1, last, "last month", h1),
                            (cx2, this, "this month", h2)):
        t = f"{R}{val:,}"
        d.text((cx - d.textlength(t, font=f_val) / 2, base - h - 76),
               t, font=f_val, fill=WHITE)
        d.text((cx - d.textlength(lab, font=f_lab) / 2, base + 28),
               lab, font=f_lab, fill=GREY)

    # bracket spanning the two bar tops
    # bracket sits entirely to the right of both bars so it never crosses a label
    y1, y2 = base - h1, base - h2
    ax = cx2 + bw / 2 + 24
    bx = ax + 86
    d.line([(ax, y1), (bx, y1)], fill=RED, width=4)
    d.line([(ax, y2), (bx, y2)], fill=RED, width=4)
    d.line([(bx, y1), (bx, y2)], fill=RED, width=4)
    d.text((bx + 30, (y1 + y2) / 2 - 30), f"{R}620 less", font=f_gap, fill=RED)

    for i, line in enumerate((f"2 days absent   \u2212 {R}520",
                              f"into her PF     \u2212 {R}100")):
        d.text((cx1 - bw / 2, base + 100 + i * 50), line, font=f_break, fill=GREY)

    img.save(path)
    print("wrote", path)


chart_cohorts(DARKBG, "slide16-chart-dark.png")
chart_cohorts((13, 13, 13, 0), "slide16-chart-alpha.png")
chart_delta(DARKBG, "slide18-delta-dark.png")
chart_delta((13, 13, 13, 0), "slide18-delta-alpha.png")
