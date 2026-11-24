"""Generate entry.png for make.fun news-image-20261124.

Summarises Tuesday 24 November 2026 world news in one 1024x1024 image.
Run once locally: python3 generate_image.py
Output: entry.png next to this file, deterministic, under 1 MiB.
"""
from PIL import Image, ImageDraw, ImageFont
import textwrap
import os

W, H = 1024, 1024
BASE = os.path.dirname(os.path.abspath(__file__))

SERIF_B = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"

def font(path, size):
    return ImageFont.truetype(path, size)

def wrap(draw, text, fnt, max_w):
    words = text.split()
    lines, cur = [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines

def draw_wrapped(draw, x, y, text, fnt, max_w, fill, leading=6):
    lines = wrap(draw, text, fnt, max_w)
    for line in lines:
        draw.text((x, y), line, font=fnt, fill=fill)
        y += fnt.size + leading
    return y

# Colours
NAVY = (15, 42, 68)
NAVY2 = (18, 58, 92)
PAPER = (246, 241, 231)
INK = (17, 24, 32)
RED = (178, 34, 34)
GOLD = (212, 175, 55)
TEAL = (14, 110, 110)
ORANGE = (214, 105, 30)
SEA = (27, 98, 148)
LIGHT_BLUE = (190, 220, 240)

img = Image.new("RGB", (W, H), PAPER)
d = ImageDraw.Draw(img)

# --- Header ---
d.rectangle([0, 0, W, 150], fill=NAVY)
d.rectangle([0, 150, W, 156], fill=GOLD)
d.text((48, 18), "TUESDAY  •  24 NOVEMBER 2026", font=font(SANS_B, 21), fill=GOLD)
d.text((48, 52), "THE WORLD IN ONE DAY", font=font(SERIF_B, 52), fill=(255, 255, 255))
# Right side of header: globe circle
d.ellipse([852, 22, 976, 146], outline=GOLD, width=4)
d.ellipse([870, 40, 958, 128], fill=TEAL)
d.text((892, 58), "24", font=font(SERIF_B, 42), fill=(255, 255, 255))
d.text((892, 102), "NOV", font=font(SANS_B, 17), fill=(255, 255, 255))

# --- Top story ---
d.text((48, 178), "TOP STORY  —  LIBYA  /  BLACK SEA", font=font(SANS_B, 19), fill=RED)
d.text((48, 206), "UKRAINE SINKS", font=font(SERIF_B, 50), fill=INK)
d.text((48, 262), "RUSSIAN WARSHIP", font=font(SERIF_B, 50), fill=INK)
draw_wrapped(d, 48, 330, "Naval drones hit the corvette Merkury at Benghazi. Kyiv opens a new Mediterranean front — the UN seeks a probe.", font(SANS, 22), 560, (55, 65, 75), leading=5)

# Visual panel on the right: sea, ship, explosion
d.rectangle([640, 178, 976, 452], fill=SEA)
d.rectangle([640, 178, 976, 452], outline=NAVY, width=3)
# sky
d.rectangle([640, 178, 976, 280], fill=LIGHT_BLUE)
# sun / explosion
cx, cy = 880, 240
for r, col in [(48, (255, 190, 60)), (35, (255, 140, 40)), (22, (255, 90, 30))]:
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=col)
# ship hull
d.polygon([(665, 340), (950, 340), (910, 390), (700, 390)], fill=(20, 30, 45))
d.rectangle([730, 305, 850, 340], fill=(20, 30, 45))
d.rectangle([770, 282, 800, 305], fill=(20, 30, 45))
# waves
for wy in (400, 418):
    for wx in range(650, 970, 40):
        d.arc([wx, wy, wx + 36, wy + 18], start=180, end=360, fill=(255, 255, 255), width=3)
d.text((658, 425), "BENGHAZI, LIBYA", font=font(SANS_B, 17), fill=(255, 255, 255))

# --- COP31 band ---
d.rectangle([48, 478, 976, 648], fill=(255, 255, 255), outline=(220, 210, 190), width=2)
d.rectangle([48, 478, 58, 648], fill=ORANGE)
d.text((78, 494), "CLIMATE  —  COP31 COLLAPSES", font=font(SANS_B, 19), fill=ORANGE)
draw_wrapped(d, 78, 524, "Antalya talks fail after 50 hours overtime — 90+ nations reject a draft with no mention of fossil fuels.", font(SERIF_B, 27), 880, INK, leading=4)
d.text((78, 612), "Called climate diplomacy's darkest moment.", font=font(SANS, 19), fill=(90, 95, 100))

# --- Three columns ---
cols = [
    ("NATO ON EDGE", RED, "Russia tests Article 5: 25 airspace violations in 2026 — 4x the 2024 total."),
    ("HORMUZ FLASHPOINT", TEAL, "US–Iran tensions rise: mines in the Strait, Gulf strikes, Trump warns Tehran."),
    ("JUSTICE  —  ROHINGYA", NAVY2, "14 nations back the ICJ ruling that Myanmar committed genocide against the Rohingya."),
]
x0 = 48
col_w = 288
gap = 24
for i, (title, col, body) in enumerate(cols):
    x = x0 + i * (col_w + gap)
    d.rectangle([x, 672, x + col_w, 868], fill=(255, 255, 255), outline=(220, 210, 190), width=2)
    d.rectangle([x, 672, x + col_w, 680], fill=col)
    draw_wrapped(d, x + 16, 694, title, font(SANS_B, 18), col_w - 32, col, leading=2)
    draw_wrapped(d, x + 16, 736, body, font(SANS, 19), col_w - 32, INK, leading=5)

# --- Bottom strip ---
d.rectangle([48, 892, 976, 976], fill=NAVY)
d.text((68, 908), "MARKETS RALLY:  S&P +4.7%  •  Nasdaq +6.5%  as Nvidia's Huang returns.", font=font(SANS_B, 20), fill=(255, 255, 255))
d.text((68, 942), "ALSO:  UN chief calls for AI safety rules within a year  •  5.6 quake hits Nepal", font=font(SANS, 18), fill=(200, 215, 230))

# Footer credit line
d.text((48, 990), "24 NOV 2026  •  Summary of the day's world news", font=font(SANS, 14), fill=(120, 120, 115))

out = os.path.join(BASE, "entry.png")
img.save(out, "PNG", optimize=True)
print(f"saved {out} {img.size} {os.path.getsize(out)} bytes")
