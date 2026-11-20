#!/usr/bin/env python3
"""Draw the news-image-20261120 entry: a one-page newspaper front page
summing up world news of Friday 20 November 2026.

HERO-LED front page: the Shenzhen peace declaration leads as a tall hero
panel with a large code-drawn illustration (dusk sky, setting sun,
Shenzhen skyline, the round summit table with the three leaders' flags
and a dove above it). Six more stories sit in two compact rows below,
with an "Also today" strip at the foot. All art is drawn
programmatically with Pillow (no photos, no scraped images, no logos).
Run:  python3 draw.py  ->  writes entry.png (1024x1024, < 1 MiB).

Stories (all first reported on 20 Nov 2026, verified against at least
two reputable outlets each):
  Lead  Trump, Xi and Putin sign a "Declaration toward Peace" after
        their first-ever three-way summit in Shenzhen; nuclear war
        "cannot be won and must never be fought"; Ukraine unmentioned.
  1     Houthi missile hits Riyadh's tallest tower, the PIF Tower;
        windows blown out across 7-8 floors, no injuries.
  2     Russia strikes Kyiv overnight with ballistic missiles; three
        Dnipro bridges damaged, fires across the capital.
  3     GTA VI: an estimated $2.36bn on day one, 24.6m copies sold --
        the biggest entertainment launch ever (Sensor Tower estimate).
  4     Anthropic closes 17% up at $97.17 on its Nasdaq debut after
        the $81.3bn IPO, as Wall Street falls a fifth straight day.
  5     COP31 draft deal drops every mention of phasing out fossil
        fuels as talks in Antalya enter their final day.
  6     Gazans return home as Israel ends its rare ground operation
        in central Gaza.
  Also   US Senate rejects Iran war-powers bid 51-48; Trump pardons
        Pete Rose; Kenya's last Ebola patient discharged; Europe's
        youth protest living costs; Somalia expels UAE envoy.
"""
import random

from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
PAPER = (247, 242, 231)
INK = (20, 20, 20)
SOFT = (58, 58, 58)
NAVY = (16, 36, 62)
DARKNAVY = (10, 24, 44)
RED = (179, 39, 30)
GOLD = (217, 164, 65)
PANEL = (255, 253, 247)
BORDER = (206, 198, 178)
TEAL = (18, 92, 96)
GREEN = (31, 110, 58)
ORANGE = (214, 96, 20)
STEEL = (52, 84, 122)
CRIMSON = (140, 28, 28)

FD = "/usr/share/fonts/truetype/dejavu/"
FN = "/usr/share/fonts/truetype/noto/"


def font(path, size):
    return ImageFont.truetype(path, size)


SERIF_B = FD + "DejaVuSerif-Bold.ttf"
SANS_B = FN + "NotoSans-Bold.ttf"
SANS_R = FN + "NotoSans-Regular.ttf"

img = Image.new("RGB", (W, H), PAPER)
d = ImageDraw.Draw(img)


def wrap(text, fnt, max_w):
    """Greedy word wrap to pixel width; returns list of lines."""
    lines, cur = [], ""
    for word in text.split():
        trial = (cur + " " + word).strip()
        if d.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def text_block(x, y, lines, fnt, fill, leading):
    for ln in lines:
        d.text((x, y), ln, font=fnt, fill=fill)
        y += leading
    return y


# ---------------------------------------------------------------- masthead
d.rectangle([0, 0, W, 124], fill=NAVY)
d.text((W // 2, 12), "ONE DAY  \u00b7  ONE PICTURE  \u00b7  THE WORLD",
       font=font(SANS_B, 18), fill=GOLD, anchor="ma")
d.text((W // 2, 36), "THE WORLD IN ONE DAY",
       font=font(SERIF_B, 52), fill=(255, 255, 255), anchor="ma")
d.text((W // 2, 94), "FRIDAY  20  NOVEMBER  2026",
       font=font(SANS_B, 26), fill=(255, 255, 255), anchor="ma")
d.rectangle([0, 124, W, 130], fill=RED)

M, G = 34, 14
X0, X1 = M, W - M
CW = X1 - X0  # 956


def panel(x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=PANEL, outline=BORDER, width=2)


# ---------------------------------------------------------------- icons
def icon_tower(cx, cy, s=16, col=CRIMSON):
    # skyscraper struck at the top: jagged crown, smoke puffs
    d.rectangle([cx - 12, cy - s + 6, cx + 12, cy + s], fill=col)
    d.polygon([(cx - 12, cy - s + 6), (cx - 6, cy - s - 2),
               (cx, cy - s + 6), (cx + 6, cy - s - 4),
               (cx + 12, cy - s + 6)], fill=col)
    for wy in range(cy - s + 12, cy + s - 4, 8):
        d.rectangle([cx - 7, wy, cx - 3, wy + 4], fill=GOLD)
        d.rectangle([cx + 3, wy, cx + 7, wy + 4], fill=GOLD)
    d.ellipse([cx + 14, cy - s - 2, cx + 22, cy - s + 6], fill=(150, 150, 150))
    d.ellipse([cx + 19, cy - s - 8, cx + 26, cy - s - 1], fill=(180, 180, 180))


def icon_missile_bridge(cx, cy, s=16, col=STEEL):
    # cable-stayed bridge: deck, two pylons, fan of cables
    d.line([(cx - s - 6, cy + s - 4), (cx + s + 6, cy + s - 4)],
           fill=col, width=5)
    for px in (cx - 14, cx + 14):
        d.rectangle([px - 2, cy - s, px + 2, cy + s - 4], fill=col)
        for tx in (cx - s - 4, cx - 4, cx + 6, cx + s + 4):
            d.line([(px, cy - s + 2), (tx, cy + s - 6)], fill=col, width=2)
    d.arc([cx - s, cy + s - 14, cx, cy + s + 2], 0, 180, fill=col, width=3)
    d.arc([cx, cy + s - 14, cx + s, cy + s + 2], 0, 180, fill=col, width=3)


def icon_controller(cx, cy, s=16, col=CRIMSON):
    d.rounded_rectangle([cx - s - 8, cy - s + 2, cx + s + 8, cy + s + 6],
                        radius=8, fill=col)
    d.rectangle([cx - 20, cy - 6, cx - 16, cy + 8], fill=(255, 255, 255))
    d.rectangle([cx - 23, cy - 2, cx - 13, cy + 4], fill=(255, 255, 255))
    d.ellipse([cx + 6, cy - 8, cx + 14, cy + 0], fill=GOLD)
    d.ellipse([cx + 14, cy + 0, cx + 22, cy + 8], fill=(255, 255, 255))


def icon_chart(cx, cy, s=16, col=GREEN):
    d.line([(cx - s - 4, cy + s), (cx + s + 4, cy + s)], fill=col, width=4)
    d.line([(cx - s - 4, cy + s), (cx - s - 4, cy - s)], fill=col, width=4)
    pts = [(cx - s, cy + 10), (cx - 6, cy + 2),
           (cx + 4, cy + 8), (cx + s, cy - s + 2)]
    d.line(pts, fill=col, width=5, joint="curve")
    d.polygon([(cx + s, cy - s + 2), (cx + s - 12, cy - s + 2),
               (cx + s, cy - s + 14)], fill=col)


def icon_leaf(cx, cy, s=16, col=GREEN):
    # globe with a leaf: circle, meridians, leaf sprouting top-right
    d.ellipse([cx - s, cy - s + 4, cx + s, cy + s + 2],
              outline=col, width=4)
    d.arc([cx - s + 6, cy - s + 4, cx + s - 6, cy + s + 2],
          270, 90, fill=col, width=3)
    d.line([(cx, cy - s + 4), (cx, cy + s + 2)], fill=col, width=3)
    d.line([(cx - s, cy + 2), (cx + s, cy + 2)], fill=col, width=3)
    d.polygon([(cx + 6, cy - s - 2), (cx + 22, cy - s - 12),
               (cx + 24, cy - s + 2), (cx + 12, cy - s + 6)], fill=col)


def icon_home(cx, cy, s=16, col=TEAL):
    d.polygon([(cx, cy - s), (cx + s + 4, cy - 2), (cx + s + 4, cy + s),
               (cx - s - 4, cy + s), (cx - s - 4, cy - 2)], fill=col)
    d.rectangle([cx - 5, cy + 2, cx + 5, cy + s], fill=PANEL)
    d.polygon([(cx - 4, cy - s - 8), (cx + 14, cy - s + 2),
               (cx + 4, cy - s + 4)], fill=GOLD)


# ---------------------------------------------------------------- hero
LY = 140
LH = 406
panel(X0, LY, CW, LH)
# kicker + headline + deck (left)
lx, lw = X0 + 24, 540
d.text((lx, LY + 20), "SHENZHEN  \u00b7  FIRST THREE-WAY SUMMIT  \u2014  LEAD STORY",
       font=font(SANS_B, 19), fill=RED)
hl = wrap("TRUMP, XI AND PUTIN SIGN PEACE DECLARATION",
          font(SERIF_B, 46), lw)
assert len(hl) <= 3, hl
y = text_block(lx, LY + 54, hl, font(SERIF_B, 46), INK, 54)
d.rectangle([lx, y + 8, lx + 120, y + 13], fill=GOLD)
deck = wrap("First-ever three-way summit of the US, Chinese and Russian "
            "leaders ends in Shenzhen with a vow that nuclear war "
            "\u201ccannot be won and must never be fought\u201d. Ukraine "
            "not mentioned.", font(SANS_R, 23), lw)
assert len(deck) <= 4, deck
y = text_block(lx, y + 28, deck, font(SANS_R, 23), SOFT, 30)
assert y <= LY + LH - 16, y

# hero illustration: dusk sky, setting sun, Shenzhen skyline, the round
# summit table with three flags and a dove above it
ix0, ix1 = X0 + 600, X1 - 24
iy0, iy1 = LY + 18, LY + LH - 18
top = (24, 48, 88)
bot = (244, 178, 96)
for yy in range(iy0, iy1):
    t = (yy - iy0) / max(1, iy1 - iy0)
    c = tuple(int(bot[i] + (top[i] - bot[i]) * t) for i in range(3))
    d.line([(ix0, yy), (ix1, yy)], fill=c)
# setting sun, low behind the skyline
d.ellipse([ix0 + 118, iy0 + 96, ix0 + 202, iy0 + 180], fill=(250, 196, 90))
d.ellipse([ix0 + 130, iy0 + 108, ix0 + 190, iy0 + 168], fill=(252, 216, 140))
# skyline silhouettes (seeded, deterministic) with lit windows
random.seed(20)
bx = ix0
while bx < ix1 - 8:
    bw = random.randint(20, 36)
    bh = random.randint(60, 170)
    d.rectangle([bx, iy1 - bh - 96, bx + bw, iy1 - 96], fill=DARKNAVY)
    for _ in range(bw // 8):
        wx = bx + random.randint(3, max(4, bw - 6))
        wy = iy1 - bh - 96 + random.randint(8, max(9, bh - 12))
        d.rectangle([wx, wy, wx + 3, wy + 4], fill=GOLD)
    bx += bw + 3
# supertall with spire, centre-left
sx0 = ix0 + 44
d.rectangle([sx0, iy1 - 268, sx0 + 32, iy1 - 96], fill=DARKNAVY)
d.polygon([(sx0 + 16, iy1 - 306), (sx0 + 11, iy1 - 268),
           (sx0 + 21, iy1 - 268)], fill=DARKNAVY)
for wy in range(iy1 - 258, iy1 - 116, 22):
    d.rectangle([sx0 + 5, wy, sx0 + 9, wy + 8], fill=GOLD)
    d.rectangle([sx0 + 22, wy, sx0 + 26, wy + 8], fill=GOLD)
# ground band
d.rectangle([ix0, iy1 - 96, ix1, iy1], fill=(12, 28, 52))
d.rectangle([ix0, iy1 - 96, ix1, iy1 - 92], fill=GOLD)
# round summit table (ellipse) with three flags planted around it
tcx, tcy = (ix0 + ix1) // 2, iy1 - 52
d.ellipse([tcx - 118, tcy - 22, tcx + 118, tcy + 22], fill=(122, 74, 32))
d.ellipse([tcx - 118, tcy - 28, tcx + 118, tcy + 16], fill=(146, 94, 44))
d.ellipse([tcx - 118, tcy - 28, tcx + 118, tcy + 16], outline=GOLD, width=2)
for fx, which in ((tcx - 84, "us"), (tcx, "cn"), (tcx + 84, "ru")):
    d.line([(fx, tcy - 26), (fx, tcy - 88)], fill=(220, 220, 220), width=3)
    fw, fh = 44, 30
    fy0 = tcy - 88
    if which == "us":
        for i in range(7):
            d.rectangle([fx + 2, fy0 + i * (fh // 7), fx + 2 + fw,
                         fy0 + (i + 1) * (fh // 7)],
                        fill=RED if i % 2 == 0 else (255, 255, 255))
        d.rectangle([fx + 2, fy0, fx + 20, fy0 + 16], fill=NAVY)
        for sy in (fy0 + 4, fy0 + 10):
            for sx in (fx + 6, fx + 12, fx + 18):
                d.ellipse([sx - 1, sy - 1, sx + 1, sy + 1],
                          fill=(255, 255, 255))
    elif which == "cn":
        d.rectangle([fx + 2, fy0, fx + 2 + fw, fy0 + fh], fill=RED)
        d.ellipse([fx + 7, fy0 + 5, fx + 19, fy0 + 17], fill=GOLD)
        for sx, sy in ((fx + 28, fy0 + 5), (fx + 36, fy0 + 11),
                       (fx + 36, fy0 + 21), (fx + 28, fy0 + 25)):
            d.ellipse([sx - 2, sy - 2, sx + 2, sy + 2], fill=GOLD)
    else:
        d.rectangle([fx + 2, fy0, fx + 2 + fw, fy0 + 10],
                    fill=(255, 255, 255))
        d.rectangle([fx + 2, fy0 + 10, fx + 2 + fw, fy0 + 20],
                    fill=(0, 57, 166))
        d.rectangle([fx + 2, fy0 + 20, fx + 2 + fw, fy0 + 30],
                    fill=(213, 0, 0))
# dove above the table, olive branch in its beak
dx, dy = tcx + 92, iy0 + 64
# tail, body, raised wing, head, beak, eye (all white, inside the frame)
d.polygon([(dx - 34, dy + 0), (dx - 52, dy + 8), (dx - 34, dy + 12)],
          fill=(255, 255, 255))
d.ellipse([dx - 36, dy - 6, dx + 24, dy + 14], fill=(255, 255, 255))
d.polygon([(dx - 28, dy - 2), (dx - 8, dy - 30), (dx + 8, dy - 2)],
          fill=(255, 255, 255), outline=(200, 200, 200))
d.ellipse([dx + 16, dy - 16, dx + 34, dy + 2], fill=(255, 255, 255))
d.polygon([(dx + 32, dy - 8), (dx + 42, dy - 4), (dx + 32, dy - 2)],
          fill=GOLD)
d.ellipse([dx + 26, dy - 13, dx + 30, dy - 9], fill=INK)
d.line([(dx + 40, dy - 4), (dx + 58, dy + 4)], fill=(31, 110, 58), width=3)
d.ellipse([dx + 46, dy + 0, dx + 54, dy + 8], fill=(31, 110, 58))
d.ellipse([dx + 54, dy + 4, dx + 62, dy + 12], fill=(31, 110, 58))
d.rectangle([ix0, iy0, ix1, iy1], outline=BORDER, width=2)

# ---------------------------------------------------------------- story rows
stories = [
    ("RIYADH  \u00b7  MISSILE STRIKE", CRIMSON, icon_tower,
     "HOUTHI MISSILE HITS RIYADH\u2019S TALLEST TOWER",
     "Blast blows out windows across 7\u20138 floors of the PIF Tower; "
     "no injuries reported."),
    ("KYIV  \u00b7  WAR", STEEL, icon_missile_bridge,
     "RUSSIA HITS KYIV WITH BALLISTIC MISSILES",
     "Overnight strikes damage three Dnipro bridges and set fires "
     "across the capital."),
    ("CULTURE  \u00b7  GAMING", CRIMSON, icon_controller,
     "GTA VI: $2.36BN IN A SINGLE DAY",
     "An estimated 24.6m copies sold \u2014 the biggest entertainment "
     "launch ever."),
    ("MARKETS  \u00b7  TECH", GREEN, icon_chart,
     "ANTHROPIC UP 17% ON DEBUT",
     "Shares close at $97 after the $81.3bn IPO, as Wall Street falls "
     "a fifth day."),
    ("ANTALYA  \u00b7  CLIMATE", GREEN, icon_leaf,
     "COP31 DRAFT DROPS FOSSIL FUELS",
     "New deal text erases the phase-out pledge as talks enter their "
     "final day."),
    ("GAZA  \u00b7  WAR", TEAL, icon_home,
     "GAZANS RETURN AS OPERATION ENDS",
     "Israel ends its rare ground operation in central Gaza; residents "
     "head home."),
]

PW = (CW - 2 * G) // 3  # 309
PH = 184
for row in range(2):
    ry = 560 + row * (PH + G)
    for col in range(3):
        kicker, kcol, icon, headline, deck = stories[row * 3 + col]
        px = X0 + col * (PW + G)
        panel(px, ry, PW, PH)
        icon(px + 28, ry + 24, s=16, col=kcol)
        klines = wrap(kicker, font(SANS_B, 14), PW - 78)
        assert len(klines) <= 1, (kicker, klines)
        text_block(px + 64, ry + 14, klines, font(SANS_B, 14), kcol, 18)
        hlines = wrap(headline, font(SERIF_B, 20), PW - 28)
        y = text_block(px + 14, ry + 54, hlines, font(SERIF_B, 20), INK, 24)
        dlines = wrap(deck, font(SANS_R, 14), PW - 28)
        y = text_block(px + 14, y + 6, dlines, font(SANS_R, 14), SOFT, 17)
        assert len(hlines) <= 3 and len(dlines) <= 3, (headline, hlines, dlines)
        assert y <= ry + PH - 6, (headline, y, ry + PH)

# ---------------------------------------------------------------- footer
FY = 950
d.rectangle([0, FY, W, H], fill=NAVY)
d.text((M, FY + 8), "ALSO TODAY \u2014 20 NOV 2026",
       font=font(SANS_B, 19), fill=GOLD)
items = ("Senate rejects Iran war-powers bid 51\u201348  \u00b7  Trump "
         "pardons Pete Rose  \u00b7  Kenya\u2019s last Ebola patient "
         "discharged  \u00b7  Europe\u2019s youth protest living costs  "
         "\u00b7  Somalia expels UAE envoy")
flines = wrap(items, font(SANS_R, 17), W - 2 * M)
assert len(flines) <= 2, flines
text_block(M, FY + 32, flines, font(SANS_R, 17), (255, 255, 255), 20)

img.save("entry.png", optimize=True)
print("saved entry.png")
