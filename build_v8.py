#!/usr/bin/env python3
"""
Mechanic Trust — Final Portfolio Deck
Matches the exact cover screenshot design with full-width blue footer bar.
"""

from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor, white, black
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT, TA_JUSTIFY
from reportlab.platypus import (
    Paragraph, Spacer, Image, Table, TableStyle,
    PageBreak, KeepTogether, Flowable,
    Frame, PageTemplate, BaseDocTemplate
)
from PIL import Image as PILImage
import os

UPLOADS = "/mnt/user-data/uploads"
OUTPUT = "/home/claude/mechanic_trust_v8.pdf"
PAGE_W, PAGE_H = letter  # 612 x 792

# --- Colors: brighter modern blue, darker body text ---
NAVY = HexColor("#1e3a6e")           # Brighter navy for hero & footer
NAVY_LIGHT = HexColor("#2563eb")     # Modern bright blue for accents
TEXT_WHITE = HexColor("#ffffff")
TEXT_HERO_SUB = HexColor("#cbd5e8")  # Light blue/gray subtitle in hero
TEXT_HERO_SMALL = HexColor("#8899b8") # Small text at bottom of hero
TEXT_BLACK = HexColor("#111827")      # True dark for headings
TEXT_DARK = HexColor("#1f2937")       # Very dark gray for body (much darker)
TEXT_MED = HexColor("#374151")        # Medium-dark for secondary
TEXT_LIGHT = HexColor("#6b7280")      # Gray for captions (still readable)
BORDER = HexColor("#d1d5db")
BG_TABLE_HEAD = HexColor("#e5e9f0")
TAG_BORDER = HexColor("#2563eb")
TAG_BG = HexColor("#eff3ff")

MARGIN_LR = 0.6 * inch
MARGIN_T = 0.5 * inch
MARGIN_B = 0.5 * inch
CONTENT_W = PAGE_W - 2 * MARGIN_LR
FOOTER_H = 26  # Height of blue footer bar

# --- Images ---
IMG = {
    "home_filters": f"{UPLOADS}/IMG_4098.png",
    "home_shops_list": f"{UPLOADS}/IMG_4099.png",
    "home_map_pwa": f"{UPLOADS}/IMG_4097.png",
    "diagnose_text": f"{UPLOADS}/IMG_4101.png",
    "diagnose_voice": f"{UPLOADS}/IMG_4102.png",
    "diagnose_photo": f"{UPLOADS}/IMG_4103.png",
    "diagnose_analyzing": f"{UPLOADS}/IMG_4107.png",
    "result_brake_87": f"{UPLOADS}/IMG_4104.png",
    "result_assessment": f"{UPLOADS}/IMG_4105.png",
    "result_recs_shops": f"{UPLOADS}/IMG_4106.png",
    "result_low_72": f"{UPLOADS}/IMG_4108.png",
}


def get_img_dims(path, tw):
    with PILImage.open(path) as img:
        w, h = img.size
        return tw, h * tw / w

def make_img(path, width):
    w, h = get_img_dims(path, width)
    return Image(path, width=w, height=h)


# =====================================================================
# STYLES
# =====================================================================
def S(name, **kw):
    d = dict(fontName='Helvetica', fontSize=10, leading=14, textColor=TEXT_DARK, alignment=TA_LEFT)
    d.update(kw)
    return ParagraphStyle(name, **d)

# Section headers (matching v6 ■■ style)
s_section = S('Section', fontName='Helvetica-Bold', fontSize=13, leading=17, textColor=NAVY, spaceBefore=4, spaceAfter=8)
s_subsection = S('Sub', fontName='Helvetica-Bold', fontSize=11, leading=15, textColor=TEXT_BLACK, spaceBefore=8, spaceAfter=4)
s_body = S('Body', fontSize=9.5, leading=14, textColor=TEXT_DARK, spaceAfter=6, alignment=TA_JUSTIFY)
s_body_left = S('BodyL', fontSize=9.5, leading=14, textColor=TEXT_DARK, spaceAfter=6)
s_bullet = S('Bullet', fontSize=9.5, leading=14, textColor=TEXT_DARK, leftIndent=14, bulletIndent=0, spaceBefore=2, spaceAfter=2)
s_label = S('Label', fontName='Helvetica-Bold', fontSize=8.5, leading=12, textColor=TEXT_MED, spaceBefore=8, spaceAfter=3)
s_band = S('Band', fontName='Helvetica-Bold', fontSize=9, leading=12, textColor=TEXT_BLACK, spaceBefore=12, spaceAfter=6)
s_caption = S('Cap', fontSize=8, leading=11, textColor=TEXT_LIGHT, alignment=TA_CENTER)
s_th = S('TH', fontName='Helvetica-Bold', fontSize=8.5, leading=12, textColor=TEXT_BLACK)
s_td = S('TD', fontSize=8.5, leading=12, textColor=TEXT_DARK)
s_td_sm = S('TDs', fontSize=8, leading=11, textColor=TEXT_DARK)
s_quote = S('Q', fontName='Helvetica-Oblique', fontSize=10, leading=15, textColor=TEXT_MED, leftIndent=12, rightIndent=12, spaceBefore=8, spaceAfter=4)
s_quote_attr = S('QA', fontName='Helvetica-Bold', fontSize=9, leading=12, textColor=TEXT_MED, leftIndent=12)


# =====================================================================
# SECTION HEADER FLOWABLE (■■ style with blue underline)
# =====================================================================
class SectionHead(Flowable):
    def __init__(self, num, title, w=CONTENT_W):
        Flowable.__init__(self)
        self.num = num; self.title = title; self.width = w; self.height = 34
    def draw(self):
        c = self.canv; y = 12
        # Blue squares
        c.setFillColor(NAVY_LIGHT)
        c.rect(0, y+2, 8, 8, fill=1, stroke=0)
        c.rect(12, y+2, 8, 8, fill=1, stroke=0)
        # Number + title
        c.setFillColor(NAVY)
        c.setFont("Helvetica-Bold", 20)
        txt = f"{self.num} \u00b7 {self.title}"
        c.drawString(28, y, txt)
        # Underline
        c.setStrokeColor(NAVY_LIGHT); c.setLineWidth(1.5)
        c.line(0, 0, self.width, 0)


# =====================================================================
# COVER PAGE FLOWABLE
# =====================================================================
class CoverPage(Flowable):
    """Draws the exact cover design from the screenshot."""
    def __init__(self):
        Flowable.__init__(self)
        self.width = CONTENT_W - 12  # Slightly narrower to fit frame
        self.height = PAGE_H - MARGIN_T - MARGIN_B - FOOTER_H - 20

    def draw(self):
        c = self.canv
        W = self.width
        
        # --- Hero blue block ---
        hero_h = 480
        hero_y = self.height - hero_h
        c.setFillColor(NAVY)
        c.rect(0, hero_y, W, hero_h, fill=1, stroke=0)
        
        # Top tag inside hero
        c.setFillColor(HexColor("#7b8fba"))
        c.setFont("Helvetica-Bold", 9)
        c.drawString(24, hero_y + hero_h - 34, "AI PRODUCT PORTFOLIO \u00b7 CASE STUDY")
        
        # Big title
        c.setFillColor(TEXT_WHITE)
        c.setFont("Helvetica-Bold", 36)
        c.drawString(24, hero_y + hero_h - 130, "Mechanic Trust")
        
        # Subtitle
        c.setFillColor(TEXT_HERO_SUB)
        c.setFont("Helvetica", 14)
        c.drawString(24, hero_y + hero_h - 180, "Closing the Trust Gap in Auto Repair")
        
        # Author info
        c.setFillColor(TEXT_HERO_SUB)
        c.setFont("Helvetica", 12)
        c.drawString(24, hero_y + hero_h - 290, "Ruthvik Arepelly \u00b7 AI Product Manager \u00b7 Tampa, FL")
        
        # Beta line at bottom of hero
        c.setFillColor(TEXT_HERO_SMALL)
        c.setFont("Helvetica", 9)
        c.drawString(24, hero_y + 20, "Beta prototype \u00b7 Built with v0 by Vercel \u00b7 Pre-launch")
        
        # --- Tag strip below hero ---
        tag_y = hero_y - 30
        tags = ["CONSUMER MOBILE", "AI / LLM", "AUTO REPAIR", "TRUST INFRASTRUCTURE"]
        tag_w = W / len(tags)
        for i, tag in enumerate(tags):
            x = i * tag_w
            # Tag box
            c.setStrokeColor(TAG_BORDER)
            c.setLineWidth(0.75)
            c.setFillColor(TAG_BG)
            c.roundRect(x + 2, tag_y, tag_w - 4, 20, 2, fill=1, stroke=1)
            # Tag text
            c.setFillColor(NAVY_LIGHT)
            c.setFont("Helvetica-Bold", 7.5)
            tw = c.stringWidth(tag, "Helvetica-Bold", 7.5)
            c.drawString(x + (tag_w - tw) / 2, tag_y + 6, tag)
        
        # --- Metadata row ---
        meta_y = tag_y - 40
        meta = [
            ("Type", "Consumer mobile app"),
            ("Stage", "Beta, pre-launch"),
            ("Built with", "v0 by Vercel, AI image analysis"),
            ("Domain", "Auto repair / trust"),
        ]
        col_w = W / len(meta)
        for i, (label, value) in enumerate(meta):
            x = i * col_w
            c.setFillColor(TEXT_BLACK)
            c.setFont("Helvetica-Bold", 9)
            c.drawString(x + 4, meta_y + 12, label)
            c.setFillColor(TEXT_MED)
            c.setFont("Helvetica", 8.5)
            c.drawString(x + 4, meta_y, value)


# =====================================================================
# HELPERS
# =====================================================================
def screenshot_band(title, items, img_w=None):
    els = [Spacer(1, 8), Paragraph(f"<b>{title}</b>", s_band)]
    n = len(items)
    col_w = CONTENT_W / n
    if img_w is None:
        img_w = min(col_w - 10, 1.8 * inch)
    imgs = [make_img(p, img_w) for p, _ in items]
    caps = [Paragraph(l, s_caption) for _, l in items]
    t = Table([imgs, caps], colWidths=[col_w]*n)
    t.setStyle(TableStyle([
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
        ('VALIGN', (0,0), (-1,0), 'BOTTOM'),
        ('VALIGN', (0,1), (-1,1), 'TOP'),
        ('TOPPADDING', (0,1), (-1,1), 4),
        ('BOTTOMPADDING', (0,0), (-1,0), 2),
        ('LEFTPADDING', (0,0), (-1,-1), 3),
        ('RIGHTPADDING', (0,0), (-1,-1), 3),
    ]))
    els.append(t)
    els.append(Spacer(1, 4))
    return els

def tbl(data, cw, header=True):
    t = Table(data, colWidths=cw, repeatRows=1 if header else 0)
    cmds = [
        ('ALIGN', (0,0), (-1,-1), 'LEFT'),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
        ('LEFTPADDING', (0,0), (-1,-1), 7),
        ('RIGHTPADDING', (0,0), (-1,-1), 7),
        ('GRID', (0,0), (-1,-1), 0.5, BORDER),
        ('BACKGROUND', (0,1), (-1,-1), HexColor("#ffffff")),
    ]
    if header:
        cmds += [
            ('BACKGROUND', (0,0), (-1,0), BG_TABLE_HEAD),
            ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
        ]
    t.setStyle(TableStyle(cmds))
    return t


# =====================================================================
# PAGE TEMPLATES
# =====================================================================
def footer_bar(canvas, doc):
    """Full-width dark blue footer bar with white text."""
    canvas.saveState()
    # Blue bar
    canvas.setFillColor(NAVY)
    canvas.rect(0, 0, PAGE_W, FOOTER_H, fill=1, stroke=0)
    # Left text
    canvas.setFillColor(TEXT_WHITE)
    canvas.setFont("Helvetica-Oblique", 8)
    canvas.drawString(MARGIN_LR, 9, "Mechanic Trust \u2014 AI Product Portfolio")
    # Right text
    canvas.setFont("Helvetica", 8)
    canvas.drawRightString(PAGE_W - MARGIN_LR, 9, f"Ruthvik Arepelly \u00b7 Page {doc.page}")
    canvas.restoreState()


doc = BaseDocTemplate(
    OUTPUT, pagesize=letter,
    leftMargin=MARGIN_LR, rightMargin=MARGIN_LR,
    topMargin=MARGIN_T, bottomMargin=MARGIN_B + FOOTER_H,
)
frame = Frame(MARGIN_LR, MARGIN_B + FOOTER_H, CONTENT_W, 
              PAGE_H - MARGIN_T - MARGIN_B - FOOTER_H, id='main')
doc.addPageTemplates([PageTemplate(id='main', frames=frame, onPage=footer_bar)])

story = []

# =====================================================================
# PAGE 1 — COVER (exact screenshot match)
# =====================================================================
story.append(CoverPage())
story.append(PageBreak())

# =====================================================================
# PAGE 2 — PROBLEM STATEMENT (expanded with story + market size + why now)
# =====================================================================
story.append(SectionHead("01", "Problem Statement"))
story.append(Spacer(1, 12))

story.append(Paragraph("<b>One-Sentence Problem</b>", s_subsection))
story.append(Paragraph(
    "People facing car repairs have no reliable way to find a trustworthy mechanic, understand "
    "whether a quoted price is fair, or get a second opinion \u2014 leaving them vulnerable to "
    "overcharging and bad service with no recourse.",
    s_body))

story.append(Spacer(1, 10))
story.append(Paragraph("<b>The Deeper Gap</b>", s_subsection))
story.append(Paragraph(
    "Here\u2019s a situation most people have lived through: your car breaks down, you Google "
    "\u201cmechanic near me,\u201d and you\u2019re staring at a wall of 4.5-star reviews that all feel "
    "fake. You have no idea if the $1,400 quote is fair, whether the repair is even necessary, "
    "or if the shop is padding the bill because they can tell you don\u2019t know better. You\u2019re "
    "anxious, time-pressured, and making a high-stakes decision with almost zero reliable information.",
    s_body))
story.append(Paragraph(
    "This isn\u2019t niche \u2014 <b>Americans spend over $80 billion annually</b> on auto repair. "
    "It\u2019s one of the largest consumer service categories, and it runs almost entirely on "
    "<b>information asymmetry</b>: the mechanic knows what\u2019s wrong; the driver doesn\u2019t. "
    "Google and Yelp haven\u2019t closed this gap \u2014 their ratings are inflated, often gamed, and "
    "tell you nothing about whether a shop is competent for <i>your specific repair</i> at a "
    "<i>fair price</i>. And the problem is worsening: modern vehicles \u2014 especially hybrids and "
    "EVs \u2014 are more complex, repair costs are rising, and the pool of qualified independent "
    "mechanics is shrinking. The trust gap is getting worse, not better.",
    s_body))

# Larger screenshots to fill the page
for el in screenshot_band("APP SCREENS \u2014 DISCOVERY & SHOP FINDING", [
    (IMG["home_filters"], "Home \u2014 Find Trusted Mechanics"),
    (IMG["home_shops_list"], "Top Shops with Trust Scores"),
    (IMG["home_map_pwa"], "PWA Install Prompt"),
], img_w=2.0*inch):
    story.append(el)

story.append(PageBreak())

# =====================================================================
# PAGE 3 — COMPANY CONTEXT & CONSTRAINTS
# =====================================================================
story.append(SectionHead("02", "Company Context & Constraints"))
story.append(Spacer(1, 12))

left = [
    Paragraph("<b>STAGE</b>", s_label),
    Paragraph("Solo founder, pre-launch beta. No team, investors, or revenue. Built to demonstrate AI PM capability through a production-quality prototype.", s_body_left),
    Paragraph("<b>TECHNICAL MATURITY</b>", s_label),
    Paragraph("Rapid-prototype stack (v0 for UI). AI image analysis for diagnostics. No live backend or real shop database yet.", s_body_left),
    Paragraph("<b>RISK TOLERANCE</b>", s_label),
    Paragraph("High velocity, low infra investment. Acceptable to show a working UX with simulated data while deferring live shop API and pricing integrations.", s_body_left),
]
right = [
    Paragraph("<b>KEY CONSTRAINTS</b>", s_label),
    Paragraph("\u2022 Solo build \u2014 no eng team", s_bullet),
    Paragraph("\u2022 No live shop-data partnership yet", s_bullet),
    Paragraph("\u2022 AI diagnosis is not mechanically certified", s_bullet),
    Paragraph("\u2022 Social trust layer requires contacts integration (future)", s_bullet),
    Spacer(1, 8),
    Paragraph("<b>Why This Was the Right Bet</b>", S('WB', fontName='Helvetica-Bold', fontSize=9.5, leading=14, textColor=TEXT_BLACK, spaceAfter=4)),
    Paragraph(
        "Auto repair is a proven high-anxiety, high-spend category \u2014 Americans spend over $80B annually. "
        "Trust-deficit markets are consistently underserved by incumbent review platforms. The social proof "
        "layer (friends who\u2019ve used a shop) is a zero-cost differentiator unavailable on Google or Yelp. "
        "Building as a beta let me validate the UX hypothesis \u2014 multimodal input + transparent pricing + "
        "social trust \u2014 before needing live shop partnerships.", s_body_left),
]
ct = Table([[left, right]], colWidths=[CONTENT_W*0.48, CONTENT_W*0.48])
ct.setStyle(TableStyle([
    ('VALIGN', (0,0), (-1,-1), 'TOP'),
    ('LEFTPADDING', (0,0), (0,0), 0), ('LEFTPADDING', (1,0), (1,0), 12),
    ('RIGHTPADDING', (0,0), (0,0), 12), ('RIGHTPADDING', (1,0), (1,0), 0),
    ('TOPPADDING', (0,0), (-1,-1), 0),
]))
story.append(ct)
story.append(PageBreak())

# =====================================================================
# PAGE 4 — TECH STACK + TRADEOFFS + SUCCESS METRICS
# =====================================================================
story.append(SectionHead("03", "Tech Stack & APIs"))
story.append(Spacer(1, 6))

tech = [
    [Paragraph("<b>LAYER</b>", s_th), Paragraph("<b>DETAILS</b>", s_th)],
    [Paragraph("Frontend", s_td_sm), Paragraph("v0 \u2192 React / Next.js for production. Component-first; fast flow iteration without backend coupling.", s_td_sm)],
    [Paragraph("AI / LLM", s_td_sm), Paragraph("Multimodal LLM (OpenAI or equivalent): confidence score, priority tier (Low/Moderate/High), plain-language assessment, ranked next steps.", s_td_sm)],
    [Paragraph("Pricing", s_td_sm), Paragraph("RepairPal / Mitchell API \u2014 price ranges calibrated by repair type + ZIP. Not model inference alone.", s_td_sm)],
    [Paragraph("Trust &amp; Social", s_td_sm), Paragraph("Contacts API (Google / Apple) for \u2018friends who used this shop.\u2019 Trust scores: verification status + review quality + social signal.", s_td_sm)],
    [Paragraph("Backend", s_td_sm), Paragraph("Node / FastAPI service orchestrating AI calls, pricing lookups, contacts matching, trust scoring. Stateless by design.", s_td_sm)],
]
story.append(tbl(tech, [1.0*inch, CONTENT_W - 1.0*inch]))

story.append(Spacer(1, 8))
story.append(SectionHead("04", "Key Tradeoffs"))
story.append(Spacer(1, 6))

tradeoffs = [
    [Paragraph("<b>CHOSE TO DO</b>", s_th), Paragraph("<b>DID NOT DO</b>", s_th), Paragraph("<b>WHY</b>", s_th)],
    [Paragraph("Rapid UI with v0", s_td_sm), Paragraph("Custom React / Next.js", s_td_sm), Paragraph("Validate UX flows fast; tech ownership deferred.", s_td_sm)],
    [Paragraph("AI diagnosis + confidence score", s_td_sm), Paragraph("Rule-based diagnostic engine", s_td_sm), Paragraph("LLMs handle the long tail better; confidence score keeps output honest.", s_td_sm)],
    [Paragraph("Price range ($800\u2013$1,100) + anchor", s_td_sm), Paragraph("Single \u2018recommended price\u2019", s_td_sm), Paragraph("Range is defensible; single number implies false precision.", s_td_sm)],
    [Paragraph("Social proof via contacts sync", s_td_sm), Paragraph("Community review system", s_td_sm), Paragraph("No cold-start problem; contacts bootstrap trust from existing relationships.", s_td_sm)],
    [Paragraph("Multimodal: photo, voice, text", s_td_sm), Paragraph("Text-only input", s_td_sm), Paragraph("High-stress mobile-first moment; voice + photo cut friction.", s_td_sm)],
]
story.append(tbl(tradeoffs, [CONTENT_W*0.30, CONTENT_W*0.28, CONTENT_W*0.42]))

story.append(Spacer(1, 8))
story.append(SectionHead("05", "Success Metrics"))
story.append(Spacer(1, 6))

metrics = [
    [Paragraph("<b>METRIC</b>", s_th), Paragraph("<b>TARGET</b>", s_th), Paragraph("<b>STATUS</b>", s_th), Paragraph("<b>SIGNAL</b>", s_th)],
    [Paragraph("Diagnosis accuracy", s_td_sm), Paragraph("\u226575% rated \u2018useful\u2019", s_td_sm), Paragraph("Beta \u2014 not yet measured", s_td_sm), Paragraph("Defined; test pending", s_td_sm)],
    [Paragraph("Price range fair", s_td_sm), Paragraph("\u226570% agree plausible", s_td_sm), Paragraph("Needs user testing", s_td_sm), Paragraph("Needs user testing", s_td_sm)],
    [Paragraph("Social proof engagement", s_td_sm), Paragraph("20%+ CTR on friend shops", s_td_sm), Paragraph("Built; no live data yet", s_td_sm), Paragraph("Awaiting contacts API", s_td_sm)],
    [Paragraph("Full-flow: diagnosis \u2192 shop", s_td_sm), Paragraph("\u226560% in one session", s_td_sm), Paragraph("Validated in walkthroughs", s_td_sm), Paragraph("Qualitative only", s_td_sm)],
    [Paragraph("Time to first result", s_td_sm), Paragraph("< 60 sec from open", s_td_sm), Paragraph("~45 sec manual walkthrough", s_td_sm), Paragraph("On track", s_td_sm)],
]
story.append(tbl(metrics, [CONTENT_W*0.22, CONTENT_W*0.22, CONTENT_W*0.28, CONTENT_W*0.28]))

story.append(PageBreak())

# =====================================================================
# PAGE 5 — AI SYSTEMS THINKING (SCREENSHOTS)
# =====================================================================
story.append(SectionHead("06", "AI Systems Thinking & Eval Framework"))
story.append(Spacer(1, 8))

for el in screenshot_band("APP SCREENS \u2014 DIAGNOSE FLOW", [
    (IMG["diagnose_text"], "Text Input"),
    (IMG["diagnose_voice"], "Voice Input"),
    (IMG["diagnose_photo"], "Photo Input"),
    (IMG["diagnose_analyzing"], "Analyzing\u2026"),
], img_w=1.4*inch):
    story.append(el)

for el in screenshot_band("APP SCREENS \u2014 AI DIAGNOSIS RESULTS", [
    (IMG["result_brake_87"], "Confidence + Priority"),
    (IMG["result_assessment"], "Assessment + Recs"),
    (IMG["result_recs_shops"], "Trusted Shops"),
    (IMG["result_low_72"], "Tire Vibration Result"),
], img_w=1.4*inch):
    story.append(el)

story.append(PageBreak())

# =====================================================================
# PAGE 6 — EVAL DETAILS (TWO-COLUMN)
# =====================================================================
left_eval = [
    Paragraph("<b>HOW MODEL QUALITY WAS EVALUATED</b>", s_label),
    Paragraph("Quality assessed across three dimensions:", s_body_left),
    Paragraph("1. <b>Relevance</b> \u2014 Does the output name a plausible issue?", s_body_left),
    Paragraph("2. <b>Calibration</b> \u2014 Does confidence reflect real uncertainty? (Vague photo \u2192 lower score.)", s_body_left),
    Paragraph("3. <b>Actionability</b> \u2014 Does it produce a useful recommendation and price range, not just a label?", s_body_left),
    Spacer(1, 6),
    Paragraph("<b>HOW FAILURE MODES WERE DEFINED</b>", s_label),
    Paragraph("<b>Silent failure:</b> Confident-sounding but wrong answer. Mitigation: confidence score always surfaced.", s_body_left),
    Paragraph("<b>Overconfidence:</b> Serious issue flagged at high confidence on ambiguous input. Mitigation: Moderate vs. High Priority framing with explicit next steps.", s_body_left),
    Paragraph("<b>Underspecification:</b> Too little user input. Mitigation: common-issue chips pre-populate inputs; voice mode reduces friction.", s_body_left),
]
right_eval = [
    Paragraph("<b>OBSERVABILITY & GUARDRAIL DECISIONS</b>", s_label),
    Paragraph("<b>Transparency over authority:</b> Never \u2018your brakes need replacement.\u2019 Always \u2018approximately 60% worn \u2014 inspect within 2 weeks.\u2019 The AI informs; it does not prescribe.", s_body_left),
    Paragraph("<b>Source attribution:</b> Price ranges labeled \u2018based on Tampa-area verified shop pricing,\u2019 grounding output in real data.", s_body_left),
    Paragraph("<b>Priority tiering:</b> Low / Moderate / High with visual distinction prevents alarm fatigue.", s_body_left),
    Paragraph("<b>No hallucinated shops:</b> Recommendations scoped to verified shops for the specific repair type.", s_body_left),
    Spacer(1, 6),
    Paragraph("<b>EVAL FRAMEWORK \u2014 WHAT I WOULD BUILD NEXT</b>", s_label),
    Paragraph("\u2022 Diagnosis acceptance rate \u2014 did users book at a recommended shop?", s_bullet),
    Paragraph("\u2022 Price-range accuracy \u2014 did actual cost fall within the predicted range?", s_bullet),
    Paragraph("\u2022 Confidence calibration curve \u2014 does 80% confidence \u2248 80% accuracy?", s_bullet),
    Paragraph("\u2022 Re-diagnosis rate \u2014 did users re-submit for the same issue?", s_bullet),
]
et = Table([[left_eval, right_eval]], colWidths=[CONTENT_W*0.48, CONTENT_W*0.48])
et.setStyle(TableStyle([
    ('VALIGN', (0,0), (-1,-1), 'TOP'),
    ('LEFTPADDING', (0,0), (0,0), 0), ('LEFTPADDING', (1,0), (1,0), 12),
    ('RIGHTPADDING', (0,0), (0,0), 12), ('RIGHTPADDING', (1,0), (1,0), 0),
    ('TOPPADDING', (0,0), (-1,-1), 0),
]))
story.append(et)
story.append(PageBreak())

# =====================================================================
# PAGE 7 — PRODUCT JUDGMENT + WHAT WOULD BREAK
# =====================================================================
story.append(SectionHead("07", "Product Judgment Under Uncertainty"))
story.append(Spacer(1, 8))

judgment = [
    [Paragraph("<b>JUDGMENT CALL</b>", s_th), Paragraph("<b>REASONING</b>", s_th)],
    [Paragraph("Ship social-proof UI before contacts data", s_td), Paragraph("The differentiator requires contacts integration \u2192 which requires user trust \u2192 which requires a working product. Built UI with simulated signals first. Bet: if UX validates concept, integration is tractable; if UX fails, contacts don\u2019t matter.", s_td)],
    [Paragraph("Show price range, not single estimate", s_td), Paragraph("Chose $800\u2013$1,100 + $950 anchor. Every comparable product omits pricing or shows a suspicious single number. A wrong single number destroys credibility; a range the actual quote falls within reinforces trust.", s_td)],
    [Paragraph("Scope shops to repair type, not geography", s_td), Paragraph("All nearby shops = noise. Verified shops for that repair type = smaller list, higher signal. Deliberate IA decision: reduce choice, increase confidence in the options shown.", s_td)],
    [Paragraph("Three input modes on day one", s_td), Paragraph("Someone in a parking lot with a leaking engine is not going to type carefully. Photo, voice, and text cover the full range of use-moment contexts \u2014 high-stress, mobile-first.", s_td)],
]
story.append(tbl(judgment, [CONTENT_W*0.30, CONTENT_W*0.70]))

story.append(Spacer(1, 12))
story.append(SectionHead("08", "What Would Break If I Was Wrong"))
story.append(Spacer(1, 8))

risks = [
    [Paragraph("<b>ASSUMPTION</b>", s_th), Paragraph("<b>WHAT BREAKS IF WRONG</b>", s_th)],
    [Paragraph("Social proof drives no engagement", s_td), Paragraph("Core differentiator collapses. Product becomes a trust-score app \u2014 useful but not different from a well-curated Yelp filter.", s_td)],
    [Paragraph("AI diagnosis perceived as untrustworthy", s_td), Paragraph("Users skip Diagnose flow. App becomes a shop-finder \u2014 a much thinner product. This is why guardrails are load-bearing, not decorative.", s_td)],
    [Paragraph("Price range too wide to be useful", s_td), Paragraph("$100\u2013$2,000 is accurate but useless. Range only anchors expectations if calibrated to local, repair-type, verified-shop data.", s_td)],
    [Paragraph("Trust score doesn\u2019t feel earned", s_td), Paragraph("94 vs 87 must feel grounded. If users sense scores are opaque or gameable, the trust infrastructure is undermined \u2014 hardest platform risk to rebuild.", s_td)],
]
story.append(tbl(risks, [CONTENT_W*0.30, CONTENT_W*0.70]))

story.append(PageBreak())

# =====================================================================
# PAGE 8 — SCOPE OWNERSHIP + FLOW + QUOTE
# =====================================================================
story.append(SectionHead("09", "Scope Ownership & Leadership Signal"))
story.append(Spacer(1, 10))

own_data = [
    [[Paragraph("<b>SCOPE OWNERSHIP</b>", s_label), Spacer(1,3),
      Paragraph("100% solo. Every product decision, UX flow, AI prompt design, trust-scoring logic, and UI architecture \u2014 owned and executed by Ruthvik with no team or delegation.", s_body_left)],
     [Paragraph("<b>LEADERSHIP IN AMBIGUITY</b>", s_label), Spacer(1,3),
      Paragraph("Pre-launch: no users, no pricing-data partnership, no contacts API. Made product bets on the core loop (diagnose \u2192 price \u2192 book) being sufficient to validate before solving data and integration challenges.", s_body_left)]],
    [[Paragraph("<b>INDEPENDENT PRODUCT JUDGMENT</b>", s_label), Spacer(1,3),
      Paragraph("Built against no existing PRD. All prioritization decisions \u2014 multimodal input, social proof layer, price-range framing \u2014 made independently through user empathy and product reasoning.", s_body_left)],
     [Paragraph("<b>AI SYSTEMS THINKING</b>", s_label), Spacer(1,3),
      Paragraph("Confidence scoring, failure-mode definition, transparency guardrails, repair-type scoping, and a defined eval framework \u2014 applied before a single real user. Pre-market thinking, not post-launch cleanup.", s_body_left)]],
]
ot = Table(own_data, colWidths=[CONTENT_W*0.48, CONTENT_W*0.48])
ot.setStyle(TableStyle([
    ('VALIGN', (0,0), (-1,-1), 'TOP'),
    ('BOX', (0,0), (0,0), 0.5, BORDER), ('BOX', (1,0), (1,0), 0.5, BORDER),
    ('BOX', (0,1), (0,1), 0.5, BORDER), ('BOX', (1,1), (1,1), 0.5, BORDER),
    ('LEFTPADDING', (0,0), (-1,-1), 10),
    ('RIGHTPADDING', (0,0), (-1,-1), 10),
    ('TOPPADDING', (0,0), (-1,-1), 6),
    ('BOTTOMPADDING', (0,0), (-1,-1), 6),
]))
story.append(ot)

for el in screenshot_band("APP SCREENS \u2014 COMPLETE FLOW OVERVIEW", [
    (IMG["home_shops_list"], "Home & Discovery"),
    (IMG["diagnose_text"], "AI Diagnose"),
    (IMG["result_brake_87"], "Results + Pricing"),
    (IMG["result_recs_shops"], "Trusted Shops"),
], img_w=1.3*inch):
    story.append(el)

# Quote box
story.append(Spacer(1, 10))
qdata = [
    [Paragraph(
        "\u201cThe mechanic space is one instance of a pattern I keep returning to as a PM: information "
        "asymmetry creates anxiety, and anxiety creates bad decisions. The design principles here \u2014 "
        "social trust layers, transparent pricing, multimodal input, AI with explainability \u2014 transfer "
        "to any domain where users are underserved by the information they need to act confidently.\u201d",
        s_quote)],
    [Paragraph("\u2014 Ruthvik Arepelly, Mechanic Trust", s_quote_attr)],
]
qt = Table(qdata, colWidths=[CONTENT_W - 20])
qt.setStyle(TableStyle([
    ('BOX', (0,0), (-1,-1), 0.75, NAVY_LIGHT),
    ('BACKGROUND', (0,0), (-1,-1), HexColor("#f8f9fb")),
    ('LEFTPADDING', (0,0), (-1,-1), 14),
    ('RIGHTPADDING', (0,0), (-1,-1), 14),
    ('TOPPADDING', (0,0), (0,0), 12),
    ('BOTTOMPADDING', (-1,-1), (-1,-1), 12),
]))
story.append(qt)

# --- Build ---
doc.build(story)
print(f"PDF: {OUTPUT} ({os.path.getsize(OUTPUT)/1024/1024:.1f} MB)")
