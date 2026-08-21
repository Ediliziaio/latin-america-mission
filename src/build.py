#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generatore statico del sito Latin America Mission — Ceará 2026.

    python3 src/build.py

Produce: index.html (IT), en/index.html (EN), robots.txt, sitemap.xml, llms.txt, 404.html.
CSS e JS vengono inlinati nelle pagine: zero richieste bloccanti in render.
"""
import json
import os
import re
import shutil
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from content import SITE, LOGOS, IMAGES, LANGS  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "src")
BASE = SITE["base_url"].rstrip("/")


# --------------------------------------------------------------------------- helpers
def strip_tags(s):
    return re.sub(r"<[^>]+>", "", s)


def unescape(s):
    return (s.replace("&amp;", "&").replace("&nbsp;", " ")
             .replace("&lt;", "<").replace("&gt;", ">").replace("&quot;", '"'))


def plain(s):
    """Testo puro per attributi e JSON-LD."""
    return unescape(strip_tags(s)).strip()


def minify_css(css):
    css = re.sub(r"/\*.*?\*/", "", css, flags=re.S)
    css = re.sub(r"\s*([{}:;,>~])\s*", r"\1", css)
    css = re.sub(r";}", "}", css)
    css = re.sub(r"\s+", " ", css)
    return css.strip()


def minify_js(js):
    js = re.sub(r"^\s*//.*$", "", js, flags=re.M)
    js = re.sub(r"/\*.*?\*/", "", js, flags=re.S)
    js = re.sub(r"\n\s*\n", "\n", js)
    js = re.sub(r"^[ \t]+", "", js, flags=re.M)
    return js.strip()


# --------------------------------------------------------------------------- JSON-LD
def build_jsonld(t):
    canonical = BASE + t["path"]
    org = {
        "@type": "Organization",
        "@id": BASE + "/#promoter",
        "name": SITE["promoter"],
        "email": SITE["email"],
        "telephone": "+" + SITE["phone_href"].lstrip("+"),
        "url": BASE + "/",
    }
    event = {
        "@type": "BusinessEvent",
        "@id": BASE + "/#event",
        "name": "Latin America Mission 2026 — Ceará",
        "description": t["meta_desc"],
        "startDate": SITE["start_date"],
        "endDate": SITE["end_date"],
        "eventStatus": "https://schema.org/EventScheduled",
        "eventAttendanceMode": "https://schema.org/OfflineEventAttendanceMode",
        "inLanguage": t["lang"],
        "url": canonical,
        "image": BASE + "/assets/img/og-latin-america-mission.jpg",
        "location": {
            "@type": "Place",
            "name": "Fortaleza, Ceará, Brasile",
            "address": {
                "@type": "PostalAddress",
                "addressLocality": SITE["city"],
                "addressRegion": "CE",
                "addressCountry": "BR",
            },
        },
        "organizer": {"@id": org["@id"]},
        "performer": {"@id": org["@id"]},
        "about": [
            "internazionalizzazione", "export", "partnership industriali",
            "design", "materiali", "energia", "logistica",
        ],
    }
    faq = {
        "@type": "FAQPage",
        "@id": canonical + "#faq",
        "mainEntity": [
            {
                "@type": "Question",
                "name": plain(q),
                "acceptedAnswer": {"@type": "Answer", "text": plain(a)},
            }
            for q, a in t["faq"]
        ],
    }
    page = {
        "@type": "WebPage",
        "@id": canonical + "#webpage",
        "url": canonical,
        "name": t["title"],
        "description": t["meta_desc"],
        "inLanguage": t["lang"],
        "isPartOf": {"@type": "WebSite", "@id": BASE + "/#website",
                     "url": BASE + "/", "name": "Latin America Mission",
                     "publisher": {"@id": org["@id"]}},
        "about": {"@id": event["@id"]},
    }
    return json.dumps({"@context": "https://schema.org",
                       "@graph": [org, event, faq, page]},
                      ensure_ascii=False, separators=(",", ":"))


# --------------------------------------------------------------------------- immagini
IMG_STATUS = {}


def has_img(slot):
    """True se il file dello slot esiste davvero in assets/img/."""
    spec = IMAGES[slot]
    ok = os.path.exists(os.path.join(ROOT, "assets", "img", spec["file"]))
    IMG_STATUS[slot] = ok
    return ok


def img(slot, t, cls="", eager=False, dark=False, sizes=None):
    """Rende l'immagine dello slot, o un segnaposto che dice cosa fornire.

    Gli slot marcati "silent" non producono segnaposto: se il file manca
    semplicemente non rendono nulla (usato per lo sfondo del hero).
    """
    spec = IMAGES[slot]
    w, h, f = spec["w"], spec["h"], spec["file"]
    if has_img(slot):
        # varianti responsive: usate solo se il file esiste davvero
        # (le genera src/make_variants.py, che e' opzionale)
        srcset = ""
        stem, ext = os.path.splitext(f)
        widths = [
            v for v in spec.get("responsive", [])
            if os.path.exists(os.path.join(ROOT, "assets", "img",
                                           "{}-{}{}".format(stem, v, ext)))
        ]
        if widths:
            parts = ["{p}assets/img/{s}-{v}{e} {v}w".format(
                p=t["_asset_prefix"], s=stem, v=v, e=ext) for v in widths]
            parts.append("{p}assets/img/{f} {w}w".format(p=t["_asset_prefix"], f=f, w=w))
            srcset = ' srcset="{}"'.format(", ".join(parts))
            sizes = sizes or "100vw"
        return (
            '<img class="{cls}" src="{p}assets/img/{f}" width="{w}" height="{h}" '
            'alt="{a}" {ld} decoding="async"{ss}{sz}>'
        ).format(
            cls=cls, p=t["_asset_prefix"], f=f, w=w, h=h,
            a=spec.get("alt_" + t["lang"], ""),
            ld='fetchpriority="high"' if eager else 'loading="lazy"',
            ss=srcset, sz=' sizes="{}"'.format(sizes) if sizes else "",
        )
    if spec.get("silent"):
        return ""
    return (
        '<div class="img-ph{dk} {cls}" style="aspect-ratio:{w}/{h}">'
        '<span class="ph-ic" aria-hidden="true"></span>'
        '<span class="ph-lbl">{lbl}</span>'
        '<span class="ph-spec">{w}&#215;{h} px &middot; assets/img/{f}</span>'
        "</div>"
    ).format(dk=" on-dark" if dark else "", cls=cls, w=w, h=h,
             lbl=spec["label_" + t["lang"]], f=f)


def figure(slot, t, cls="", dark=False, eager=False):
    """Immagine con didascalia, se lo slot ne ha una."""
    cap = IMAGES[slot].get("cap_" + t["lang"])
    inner = img(slot, t, eager=eager, dark=dark)
    if not inner:
        return ""
    if not cap:
        return '<div class="{}">{}</div>'.format(cls, inner) if cls else inner
    return '<figure class="{c}">{i}<figcaption>{cap}</figcaption></figure>'.format(
        c=cls, i=inner, cap=cap)


# --------------------------------------------------------------------------- partials
GALLERY_SLOTS = 13

# Schede dati fornite dal Governo del Ceará: il testo e' impresso nell'immagine,
# ed e' in italiano. Finche' non arrivano le versioni EN/PT le mostriamo solo
# sulla pagina italiana — meglio nessuna scheda che una scheda illeggibile.
DATA_CARDS = [("dato_hub_portuale", ""), ("dato_energie_rinnovabili", ""),
              ("dato_hub_tecnologico", ""), ("dato_crescita_pil", " wide")]
DATA_CARDS_LANGS = ("it",)

# Documento scaricabile: il bollettino economico ufficiale della SDE.
DOC_FILE = "docs/economic-report-ceara-2026-07.pdf"


def rinascimento_logo(t):
    """Marchio del distretto, in un riquadro chiaro perche' la sezione e' scura."""
    inner = img("rinascimento_logo", t, cls="rin-logo-img")
    return '<p class="rin-logo">{}</p>'.format(inner) if inner else ""


def data_cards_html(t):
    if t["lang"] not in DATA_CARDS_LANGS:
        return ""
    cards = "".join(img(slot, t, cls="data-card" + extra) for slot, extra in DATA_CARDS)
    if not cards:
        return ""
    return (
        '<div class="data-strip reveal">'
        '<p class="eyebrow">{lbl}</p>'
        '<div class="data-grid">{cards}</div>'
        '<p class="data-note">{note}</p>'
        "</div>"
    ).format(lbl=t["data_lbl"], cards=cards, note=t["data_note"])


def doc_card_html(t):
    """Card di download del report; sparisce se il PDF non e' in assets/."""
    if not os.path.exists(os.path.join(ROOT, "assets", DOC_FILE)):
        return ""
    size = os.path.getsize(os.path.join(ROOT, "assets", DOC_FILE))
    return (
        '<div class="doc-card reveal">'
        '<div class="doc-copy">'
        '<p class="eyebrow">{eyebrow}</p>'
        "<h3>{h3}</h3><p>{p}</p>"
        '<p class="doc-meta">{meta}</p>'
        "</div>"
        '<a class="btn btn-gold" href="{prefix}assets/{f}" '
        'download type="application/pdf">{cta}'
        '<span class="doc-size">{kb}&nbsp;kB</span></a>'
        "</div>"
    ).format(
        eyebrow=t["doc_eyebrow"], h3=t["doc_h3"], p=t["doc_p"], meta=t["doc_meta"],
        prefix=t["_asset_prefix"], f=DOC_FILE, cta=t["doc_cta"],
        kb="{:,}".format(round(size / 1024)).replace(",", "."),
    )


def eco_html(t):
    """Blocco 'ecosistema connesso all'Europa': testo + operatori europei."""
    ops = "".join(
        '<div class="eco-op"><span class="eco-flag">{fl}</span>'
        "<b>{nm}</b><small>{role}</small></div>".format(fl=fl, nm=nm, role=role)
        for nm, fl, role in t["eco_ops"])
    paras = "".join("<p>{}</p>".format(x) for x in t["eco_p"])
    return (
        '<div class="eco reveal">'
        '<div class="eco-copy"><p class="eyebrow">{eb}</p><h3>{h3}</h3>{paras}</div>'
        '<div class="eco-ops">{ops}</div>'
        "</div>"
    ).format(eb=t["eco_eyebrow"], h3=t["eco_h3"], paras=paras, ops=ops)


def prog_img_html(t):
    """Infografica del programma. Testo impresso in italiano: solo pagina IT."""
    if t["lang"] not in DATA_CARDS_LANGS:
        return ""
    return figure("programma_lam", t, cls="prog-cover reveal")


def nav_html(t, assets):
    items = "".join(
        '<a href="{}">{}</a>'.format(h, l) for h, l in t["nav"]
    )
    other = t["other_path"]
    it_href = "/" if t["lang"] == "en" else "#"
    return items, other


def logos_html(t):
    alt_key = "alt_" + t["lang"]
    out = []
    for lg in LOGOS:
        out.append(
            '<div class="logo-card"><img src="{p}assets/img/{f}" width="{w}" height="{h}" '
            'alt="{a}" loading="lazy" decoding="async"></div>'.format(
                p=t["_asset_prefix"], f=lg["file"], w=lg["w"], h=lg["h"], a=lg[alt_key])
        )
    for b, s in t["sup_text_cards"]:
        out.append('<div class="logo-card is-text"><b>{}</b><small>{}</small></div>'.format(b, s))
    return "".join(out)


# --------------------------------------------------------------------------- page
def render(t, css, js):
    p = t["_asset_prefix"]
    canonical = BASE + t["path"]
    hreflangs = "".join(
        '<link rel="alternate" hreflang="{l}" href="{u}">'.format(l=o["lang"], u=BASE + o["path"])
        for o in LANGS
    ) + '<link rel="alternate" hreflang="x-default" href="{}/">'.format(BASE)
    nav_items, _ = nav_html(t, p)

    def lang_item(o):
        code = o["lang"]
        if t["lang"] == code:
            return '<span aria-current="true">{}</span>'.format(code.upper())
        return '<a href="{h}" hreflang="{c}" lang="{c}">{u}</a>'.format(
            h=o["path"], c=code, u=code.upper())

    lang_switch = '<div class="lang-switch" role="group" aria-label="{lbl}">{items}</div>'.format(
        lbl=t["lang_label"], items="".join(lang_item(o) for o in LANGS))

    hero_meta = "".join(
        "<div>{}<strong>{}</strong></div>".format(k, v) for k, v in t["hero_meta"]
    )
    facts = "".join(
        '<div class="fact-row"><span class="k">{}</span><span class="v">{}</span></div>'.format(k, v)
        for k, v in t["facts"]
    )
    why_cells = "".join(
        '<article class="why-cell"><div class="num">{}</div><h3>{}</h3><p>{}</p></article>'.format(n, h, d)
        for n, h, d in t["why_cells"]
    )
    sectors = "".join(
        '<article class="sector-card"><div class="ic" aria-hidden="true">{}</div><h3>{}</h3><p>{}</p></article>'.format(i, h, d)
        for i, h, d in t["sectors"]
    )
    values = "".join(
        '<article class="value-card"><div class="vnum" aria-hidden="true">{}</div><h3>{}</h3><p>{}</p></article>'.format(n, h, d)
        for n, h, d in t["values"]
    )
    audience = "".join("<li>{}</li>".format(a) for a in t["audience"])
    narrative = "".join(
        "<li><b>0{}</b><span>{}</span></li>".format(i + 1, x)
        for i, x in enumerate(t["narrative_list"])
    )
    segments = "".join(
        '<article class="seg-cell"><h3>{}</h3><p>{}</p></article>'.format(h, d)
        for h, d in t["segments"]
    )
    programme = "".join(
        '<article class="prog-card"><div class="step">{}</div><h3>{}</h3><p>{}</p></article>'.format(s, h, d)
        for s, h, d in t["programme"]
    )
    unions = "".join(
        '<div class="part-item"><span class="tag">{}</span><span class="desc">{}</span></div>'.format(k, v)
        for k, v in t["unions"]
    )
    bodies = "".join(
        '<div class="part-item"><span class="tag">{}</span><span class="desc">{}</span></div>'.format(k, v)
        for k, v in t["bodies"]
    )
    faq = "".join(
        '<details class="faq"><summary>{}</summary><div class="ans">{}</div></details>'.format(q, a)
        for q, a in t["faq"]
    )
    perks = "".join("<li>{}</li>".format(x) for x in t["form_perks"])
    sector_opts = "".join('<option>{}</option>'.format(s) for s in t["f_sectors"])
    interests = "".join(
        '<label class="check"><input type="checkbox" name="interest" value="{v}"><span>{v}</span></label>'.format(v=x)
        for x in t["f_interests"]
    )
    foot_nav = "".join('<a href="{}">{}</a>'.format(h, l)
                       for h, l in t["nav"] + t["nav_extra"])

    head = """<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{canonical}">
{hreflangs}
<meta name="robots" content="index,follow,max-image-preview:large,max-snippet:-1,max-video-preview:-1">
<meta name="theme-color" content="#0a1729">
<meta name="author" content="{promoter}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Latin America Mission">
<meta property="og:locale" content="{locale}">
<meta property="og:title" content="{og_title}">
<meta property="og:description" content="{og_desc}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{base}/assets/img/og-latin-america-mission.jpg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="{og_title}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{og_title}">
<meta name="twitter:description" content="{og_desc}">
<meta name="twitter:image" content="{base}/assets/img/og-latin-america-mission.jpg">
<link rel="icon" href="{p}assets/img/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="{p}assets/img/apple-touch-icon.png">
<link rel="preload" href="{p}assets/fonts/inter-tight-latin-normal.woff2" as="font" type="font/woff2" crossorigin>
<style>{css}</style>
<script type="application/ld+json">{jsonld}</script>
</head>
<body>
<a class="skip" href="#main">{skip}</a>

<header class="site-header" id="header">
  <div class="wrap nav">
    <a href="#top" class="brand" aria-label="Latin America Mission">
      <span class="b-main">Latin America Mission</span>
      <span class="b-sub">Ceará · Brasile — 2026</span>
    </a>
    <nav class="nav-links" id="navLinks" aria-label="{nav_label}">{nav_items}</nav>
    <div class="nav-actions">
      {lang_switch}
      <a href="#adesioni" class="btn btn-gold nav-cta">{nav_cta}</a>
      <button class="menu-toggle" id="menuToggle" aria-label="{menu_label}" aria-expanded="false" aria-controls="navLinks">
        <span></span><span></span><span></span>
      </button>
    </div>
  </div>
</header>
""".format(
        lang=t["lang"], title=t["title"], desc=plain(t["meta_desc"]), canonical=canonical,
        hreflangs=hreflangs, promoter=plain(SITE["promoter"]),
        locale=t["locale"], og_title=plain(t["og_title"]), og_desc=plain(t["og_desc"]),
        base=BASE, p=p, css=css, jsonld=build_jsonld(t), skip=t["skip"],
        nav_label=t["nav_aria"], nav_items=nav_items, lang_switch=lang_switch,
        nav_cta=t["nav_cta"], menu_label=t["menu_label"],
    )

    body = """
<main id="main">

<section class="hero" id="top">
  <div class="hero-bg" aria-hidden="true"></div>
  <div class="hero-photo" aria-hidden="true">{hero_img}</div>
  <div class="wrap">
    <p class="hero-flag"><span class="dot" aria-hidden="true"></span><span>{hero_flag}</span></p>
    <h1>{h1a} <span class="accent">{h1b}</span></h1>
    <p class="hero-place">{place}</p>
    <p class="hero-dates"><span class="sep" aria-hidden="true"></span><time datetime="{start}/{end}">{dates}</time></p>
    <p class="hero-ics"><button type="button" id="icsBtn" class="linkish">{ics_label}</button></p>
    <p class="hero-sub">{hero_sub}</p>
    <div class="hero-cta">
      <a href="#adesioni" class="btn btn-gold">{cta1}</a>
      <a href="#missione" class="btn btn-ghost">{cta2}</a>
    </div>
    <div class="hero-meta" id="heroMeta">{hero_meta}</div>
  </div>
  <div class="hero-scroll" aria-hidden="true"><span>{scroll}</span><span class="line"></span></div>
</section>

<section class="supporters" aria-label="{sup_support}">
  <div class="wrap">
    <p class="sup-lbl">{sup_promoted}</p>
    <p class="sup-promoters"><span>{promoter}</span><span class="with">{sup_with}</span></p>
    <p class="sup-lbl">{sup_support}</p>
    <div class="logo-row">{logos}</div>
  </div>
</section>

<section id="missione">
  <div class="wrap">
    <div class="mission-grid">
      <div class="mission-copy reveal">
        <p class="eyebrow">{mission_eyebrow}</p>
        <div class="rule"></div>
        <h2>{mission_h2}</h2>
        {mission_p}
      </div>
      <aside class="fact-card reveal">
        <h3>{fact_h3}</h3>
        {facts}
        <div class="fact-row col"><span class="k">{fsk}</span><span class="v">{fsv}</span></div>
        <div class="fact-row"><span class="k">{fok}</span><span class="v fact-open">{fov}</span></div>
      </aside>
    </div>
    {mission_band}
  </div>
</section>

<section id="ceara" class="bg-paper">
  <div class="wrap">
    <div class="sec-head reveal">
      <p class="eyebrow">{why_eyebrow}</p>
      <div class="rule"></div>
      <h2>{why_h2}</h2>
      <p class="lede">{why_lede}</p>
    </div>
    <div class="why-grid reveal">{why_cells}</div>
    <div class="img-duo reveal">{ceara_porto}{ceara_industria}</div>
    <div class="pecem reveal">
      <p class="eyebrow on-dark">{pecem_eyebrow}</p>
      <h3>{pecem_h3}</h3>
      <div class="pecem-stats">{pecem_stats}</div>
      <p class="pecem-lede">{pecem_p}</p>
      <p class="pecem-lbl">{pecem_pillars_lbl}</p>
      <div class="pecem-pillars">{pecem_pillars}</div>
    </div>
    {eco_block}
    {data_cards}
    {doc_card}
  </div>
</section>

<section id="settori">
  <div class="wrap">
    <div class="sec-head reveal">
      <p class="eyebrow">{sect_eyebrow}</p>
      <div class="rule"></div>
      <h2>{sect_h2}</h2>
      <p class="lede">{sect_lede}</p>
    </div>
    <div class="sectors-grid reveal">{sectors}</div>
    <div class="callout reveal"><p>{sect_callout}</p></div>
  </div>
</section>

<section id="perche" class="bg-paper">
  <div class="wrap">
    <div class="sec-head reveal">
      <p class="eyebrow">{val_eyebrow}</p>
      <div class="rule"></div>
      <h2>{val_h2}</h2>
      <p class="lede">{val_lede}</p>
    </div>
    <div class="value-grid reveal">{values}</div>
    <div class="audience reveal">
      <p class="eyebrow on-dark">{aud_eyebrow}</p>
      <h3>{aud_h3}</h3>
      <ul>{audience}</ul>
    </div>
  </div>
</section>

<section id="rinascimento" class="bg-ink">
  <div class="wrap">
    <div class="rinasc-lead reveal">
      <div>
        {rin_logo}
        <p class="badge">{rin_badge}</p>
        <h2>{rin_h2a}<em>{rin_h2b}</em></h2>
        {rin_p}
        <a href="#adesioni" class="btn btn-outline on-dark" style="margin-top:18px">{rin_cta}</a>
      </div>
      <div class="rinasc-visual">{rin_img}</div>
    </div>
    <div class="why-now reveal">
      <div>
        <p class="eyebrow on-dark">{why_now_eyebrow}</p>
        <h3>{why_now_h3}</h3>
        <p>{why_now_p}</p>
      </div>
      <div>
        <p class="narrative">{narrative}</p>
        <ul class="narrative-list">{narrative_items}</ul>
        <p class="note-dark">{narrative_note}</p>
      </div>
    </div>
    <p class="eyebrow on-dark reveal" style="margin-bottom:26px">{seg_eyebrow}</p>
    <div class="seg-grid reveal">{segments}</div>
    <div class="fair reveal">
      <div>
        <p class="lbl">{fair_lbl}</p>
        <p class="ttl">{fair_ttl}</p>
      </div>
      <p>{fair_p}</p>
    </div>
  </div>
</section>

<section id="programma" class="bg-paper">
  <div class="wrap">
    <div class="sec-head reveal">
      <p class="eyebrow">{prog_eyebrow}</p>
      <div class="rule"></div>
      <h2>{prog_h2}</h2>
      <p class="lede">{prog_lede}</p>
    </div>
    {prog_img}
    <div class="prog-grid reveal">{programme}</div>
    <div class="callout reveal" style="background:#fff"><p>{prog_note}</p></div>
  </div>
</section>

<section id="partner">
  <div class="wrap">
    <div class="sec-head reveal">
      <p class="eyebrow">{part_eyebrow}</p>
      <div class="rule"></div>
      <h2>{part_h2}</h2>
      <p class="lede">{part_lede}</p>
    </div>
    <div class="part-wrap reveal">
      <div class="part-col">
        <h3>{part_col1_h3}</h3>
        <p class="sub">{part_col1_sub}</p>
        <div class="part-list">{unions}</div>
      </div>
      <div class="part-col">
        <h3>{part_col2_h3}</h3>
        <p class="sub">{part_col2_sub}</p>
        <div class="part-list">{bodies}</div>
        <div class="inst-box">
          <p class="eyebrow on-dark">{inst_eyebrow}</p>
          <p>{inst_p}</p>
        </div>
      </div>
    </div>
  </div>
</section>

<section id="faq" class="bg-paper">
  <div class="wrap">
    <div class="sec-head center reveal">
      <p class="eyebrow">{faq_eyebrow}</p>
      <div class="rule"></div>
      <h2>{faq_h2}</h2>
    </div>
    <div class="faq-list reveal">{faq}</div>
  </div>
</section>

<section id="adesioni" class="form-section">
  <div class="bg" aria-hidden="true"></div>
  <div class="wrap">
    <div class="form-shell">
      <div class="form-intro reveal">
        <p class="eyebrow on-dark">{form_eyebrow}</p>
        <div class="rule"></div>
        <h2>{form_h2}</h2>
        <p>{form_p}</p>
        <ul class="form-perks">{perks}</ul>
      </div>
      <div class="form-card reveal" id="formCard">
        <form id="joinForm" novalidate>
          <h3>{form_h3}</h3>
          <p class="fc-sub">{form_sub}</p>

          <div class="field">
            <label for="f-company">{f_company} <span class="req">*</span></label>
            <input id="f-company" type="text" name="company" required autocomplete="organization">
          </div>
          <div class="field-row">
            <div class="field">
              <label for="f-contact">{f_contact} <span class="req">*</span></label>
              <input id="f-contact" type="text" name="contact" required autocomplete="name">
            </div>
            <div class="field">
              <label for="f-role">{f_role}</label>
              <input id="f-role" type="text" name="role" autocomplete="organization-title">
            </div>
          </div>
          <div class="field-row">
            <div class="field">
              <label for="f-email">{f_email} <span class="req">*</span></label>
              <input id="f-email" type="email" name="email" required autocomplete="email" inputmode="email">
            </div>
            <div class="field">
              <label for="f-phone">{f_phone}</label>
              <input id="f-phone" type="tel" name="phone" autocomplete="tel" inputmode="tel">
            </div>
          </div>
          <div class="field-row">
            <div class="field">
              <label for="f-country">{f_country}</label>
              <input id="f-country" type="text" name="country" value="{country_default}" autocomplete="country-name">
            </div>
            <div class="field">
              <label for="f-part">{f_participants}</label>
              <input id="f-part" type="number" name="participants" min="1" max="20" value="1" inputmode="numeric">
            </div>
          </div>
          <div class="field">
            <label for="f-sector">{f_sector}</label>
            <select id="f-sector" name="sector">
              <option value="">{f_sector_ph}</option>
              {sector_opts}
            </select>
          </div>
          <fieldset class="field">
            <legend>{f_interest}</legend>
            <div class="checks">{interests}</div>
          </fieldset>
          <div class="field">
            <label for="f-msg">{f_message}</label>
            <textarea id="f-msg" name="message" placeholder="{f_message_ph}"></textarea>
          </div>
          <p class="hp" aria-hidden="true"><label>Website<input type="text" name="website" tabindex="-1" autocomplete="off"></label></p>
          <label class="privacy">
            <input type="checkbox" name="privacy" required>
            <span>{f_privacy}</span>
          </label>
          <button type="submit" class="btn btn-gold" id="submitBtn">{f_submit}</button>
          <p class="form-status" id="formStatus" role="status" aria-live="polite"></p>
          <p class="form-note">{f_note} <a href="mailto:{email}">{email}</a> · <a href="tel:{phone_href}">{phone}</a></p>
        </form>
        <div class="form-success" id="formSuccess">
          <div class="ok" aria-hidden="true">&#10003;</div>
          <h3>{f_success_h3}</h3>
          <p>{f_success_p}</p>
        </div>
      </div>
    </div>
  </div>
</section>

<section id="galleria">
  <div class="wrap">
    <div class="sec-head reveal">
      <p class="eyebrow">{gal_eyebrow}</p>
      <div class="rule"></div>
      <h2>{gal_h2}</h2>
      <p class="lede">{gal_lede}</p>
    </div>
    <div class="gallery reveal">{gallery}</div>
  </div>
</section>

<section id="promotore" class="bg-paper">
  <div class="wrap">
    <div class="promoter reveal">
      <div class="promoter-img">{prom_img}</div>
      <div class="promoter-copy">
        <p class="eyebrow">{prom_eyebrow}</p>
        <div class="rule"></div>
        <h2>{prom_h2}</h2>
        <p class="promoter-role">{prom_role}</p>
        {prom_p}
        <a href="#adesioni" class="btn btn-outline">{prom_cta}</a>
      </div>
    </div>
  </div>
</section>

<section id="contatti">
  <div class="wrap">
    <div class="sec-head center reveal">
      <p class="eyebrow">{ct_eyebrow}</p>
      <div class="rule"></div>
      <h2>{ct_h2}</h2>
      <p class="lede">{ct_lede}</p>
    </div>
    <div class="contact-grid reveal">
      <div class="contact-card"><p class="ct-lbl">{ct_email}</p><a href="mailto:{email}">{email}</a></div>
      <div class="contact-card"><p class="ct-lbl">{ct_phone}</p><a href="tel:{phone_href}">{phone}</a></div>
      <div class="contact-card"><p class="ct-lbl">{ct_promoter}</p><span class="val">{promoter}</span></div>
    </div>
  </div>
</section>

</main>

<footer>
  <div class="wrap">
    <div class="foot-top">
      <div class="foot-brand">
        <p class="b-main">Latin America Mission</p>
        <p class="b-sub">{foot_sub}</p>
        <p>{foot_p}</p>
      </div>
      <nav class="foot-col" aria-label="{foot_nav_h}">
        <h2>{foot_nav_h}</h2>
        {foot_nav}
      </nav>
      <div class="foot-col">
        <h2>{foot_ct_h}</h2>
        <a href="mailto:{email}">{email}</a>
        <a href="tel:{phone_href}">{phone}</a>
        <a href="{base}/">latinamericamission.armandorossi.it</a>
      </div>
    </div>
    <div class="foot-bot">
      <span>{foot_copy}</span>
      <span>{foot_note}</span>
    </div>
  </div>
</footer>
<div class="sticky-cta" id="stickyCta" hidden>
  <div>
    <strong>{sticky_cta}</strong>
    <span>{sticky_dates}</span>
  </div>
  <a href="#adesioni" class="btn btn-gold">{nav_cta}</a>
</div>
<button class="to-top" id="toTop" aria-label="{top_label}" hidden></button>
<dialog class="lightbox" id="lightbox" aria-label="{zoom_label}">
  <button class="lb-close" id="lbClose" aria-label="{close_label}">&#215;</button>
  <img id="lbImg" alt="">
  <p id="lbCap"></p>
</dialog>
<script>{js}</script>
</body>
</html>
""".format(
        hero_flag=t["hero_flag"], h1a=t["hero_h1_a"], h1b=t["hero_h1_b"],
        place=t["hero_place"], dates=t["hero_dates"],
        start=SITE["start_date"], end=SITE["end_date"],
        hero_sub=t["hero_sub"], cta1=t["hero_cta_1"], cta2=t["hero_cta_2"],
        hero_meta=hero_meta, scroll=t["scroll"],
        sup_promoted=t["sup_promoted"], sup_with=t["sup_with"],
        sup_support=t["sup_support"], promoter=SITE["promoter"].replace("&", "&amp;"),
        logos=logos_html(t),
        mission_eyebrow=t["mission_eyebrow"], mission_h2=t["mission_h2"],
        mission_p="".join("<p>{}</p>".format(x) for x in t["mission_p"]),
        fact_h3=t["fact_h3"], facts=facts,
        fsk=t["fact_support_k"], fsv=t["fact_support_v"],
        fok=t["fact_open_k"], fov=t["fact_open_v"],
        why_eyebrow=t["why_eyebrow"], why_h2=t["why_h2"], why_lede=t["why_lede"],
        why_cells=why_cells,
        pecem_eyebrow=t["pecem_eyebrow"], pecem_h3=t["pecem_h3"],
        pecem_stats="".join(
            '<div><span class="big">{}</span><span class="cap">{}</span></div>'.format(v, c)
            for v, c in t["pecem_stats"]),
        pecem_p=t["pecem_p"], pecem_pillars_lbl=t["pecem_pillars_lbl"],
        pecem_pillars="".join(
            "<div><h4>{}</h4><p>{}</p></div>".format(h, d) for h, d in t["pecem_pillars"]),
        sect_eyebrow=t["sect_eyebrow"], sect_h2=t["sect_h2"], sect_lede=t["sect_lede"],
        sectors=sectors, sect_callout=t["sect_callout"],
        val_eyebrow=t["val_eyebrow"], val_h2=t["val_h2"], val_lede=t["val_lede"],
        values=values, aud_eyebrow=t["aud_eyebrow"], aud_h3=t["aud_h3"], audience=audience,
        rin_badge=t["rin_badge"], rin_h2a=t["rin_h2_a"], rin_h2b=t["rin_h2_b"],
        rin_p="".join("<p>{}</p>".format(x) for x in t["rin_p"]),
        rin_cta=t["rin_cta"],
        why_now_eyebrow=t["why_now_eyebrow"], why_now_h3=t["why_now_h3"], why_now_p=t["why_now_p"],
        narrative=t["narrative"], narrative_items=narrative, narrative_note=t["narrative_note"],
        seg_eyebrow=t["seg_eyebrow"], segments=segments,
        fair_lbl=t["fair_lbl"], fair_ttl=t["fair_ttl"], fair_p=t["fair_p"],
        prog_eyebrow=t["prog_eyebrow"], prog_h2=t["prog_h2"], prog_lede=t["prog_lede"],
        programme=programme, prog_note=t["prog_note"],
        part_eyebrow=t["part_eyebrow"], part_h2=t["part_h2"], part_lede=t["part_lede"],
        part_col1_h3=t["part_col1_h3"], part_col1_sub=t["part_col1_sub"], unions=unions,
        part_col2_h3=t["part_col2_h3"], part_col2_sub=t["part_col2_sub"], bodies=bodies,
        inst_eyebrow=t["inst_eyebrow"], inst_p=t["inst_p"],
        faq_eyebrow=t["faq_eyebrow"], faq_h2=t["faq_h2"], faq=faq,
        form_eyebrow=t["form_eyebrow"], form_h2=t["form_h2"], form_p=t["form_p"], perks=perks,
        form_h3=t["form_h3"], form_sub=t["form_sub"],
        f_company=t["f_company"], f_contact=t["f_contact"], f_role=t["f_role"],
        f_email=t["f_email"], f_phone=t["f_phone"], f_country=t["f_country"],
        f_participants=t["f_participants"], f_sector=t["f_sector"],
        f_sector_ph=t["f_sector_placeholder"], sector_opts=sector_opts,
        f_interest=t["f_interest"], interests=interests,
        f_message=t["f_message"], f_message_ph=t["f_message_ph"],
        f_privacy=t["f_privacy"], f_submit=t["f_submit"], f_note=t["f_note"],
        f_success_h3=t["f_success_h3"], f_success_p=t["f_success_p"],
        country_default={"it": "Italia", "en": "Italy", "pt": "Itália"}[t["lang"]],
        ct_eyebrow=t["ct_eyebrow"], ct_h2=t["ct_h2"], ct_lede=t["ct_lede"],
        ct_email=t["ct_email"], ct_phone=t["ct_phone"], ct_promoter=t["ct_promoter"],
        foot_sub=t["foot_sub"], foot_p=t["foot_p"], foot_nav_h=t["foot_nav_h"],
        foot_nav=foot_nav, foot_ct_h=t["foot_ct_h"],
        foot_copy=t["foot_copy"], foot_note=t["foot_note"],
        email=SITE["email"], phone=SITE["phone_display"], phone_href=SITE["phone_href"],
        base=BASE, js=js,
        hero_img=img("hero", t, cls="hero-photo-img", eager=True),
        mission_band=figure("mission_band", t, cls="band reveal"),
        ceara_porto=figure("ceara_porto", t, cls="duo-item"),
        ceara_industria=figure("ceara_industria", t, cls="duo-item"),
        rin_img=img("rinascimento", t, dark=True),
        rin_logo=rinascimento_logo(t),
        eco_block=eco_html(t),
        prog_img=prog_img_html(t),
        data_cards=data_cards_html(t),
        doc_card=doc_card_html(t),
        gallery="".join(
            figure("gallery_{}".format(i), t, cls="gal-item")
            for i in range(1, GALLERY_SLOTS + 1)),
        prom_img=img("promoter", t),
        gal_eyebrow=t["gal_eyebrow"], gal_h2=t["gal_h2"], gal_lede=t["gal_lede"],
        prom_eyebrow=t["prom_eyebrow"], prom_h2=t["prom_h2"], prom_role=t["prom_role"],
        prom_p="".join("<p>{}</p>".format(x) for x in t["prom_p"]),
        prom_cta=t["prom_cta"],
        ics_label=t["ics_label"], sticky_cta=t["sticky_cta"],
        sticky_dates=t["sticky_dates"], top_label=t["top_label"],
        close_label=t["close_label"], zoom_label=t["zoom_label"],
        nav_cta=t["nav_cta"],
    )
    return head + body


# --------------------------------------------------------------------------- main
def main():
    with open(os.path.join(SRC, "styles.css"), encoding="utf-8") as f:
        css_raw = f.read()
    with open(os.path.join(SRC, "site.js"), encoding="utf-8") as f:
        js_raw = f.read()

    for t in LANGS:
        t["_asset_prefix"] = "" if t["path"] == "/" else "../"
        css = minify_css(css_raw.replace("/assets/", t["_asset_prefix"] + "assets/"))
        js = minify_js(
            js_raw
            .replace("__ENDPOINT__", SITE["form_endpoint"])
            .replace("__EMAIL__", SITE["email"])
            .replace("__SENDING__", t["f_sending"])
            .replace("__ERROR__", t["f_error"].format(email=SITE["email"]))
            .replace("__SUBJECT__", t["f_mail_subject"])
            .replace("__START__", SITE["start_date"])
            .replace("__END__", SITE["end_date"])
            .replace("__COUNT_LABEL__", t["countdown_label"])
            .replace("__COUNT_UNIT__", t["countdown_unit"])
            .replace("__COUNT_TODAY__", t["countdown_today"])
            .replace("__ICS_TITLE__", "Latin America Mission 2026 - Ceara, Brasile")
        )
        html = render(t, css, js)
        out = (os.path.join(ROOT, "index.html") if t["path"] == "/"
               else os.path.join(ROOT, t["path"].strip("/"), "index.html"))
        os.makedirs(os.path.dirname(out), exist_ok=True)
        with open(out, "w", encoding="utf-8") as f:
            f.write(html)
        print("  {:<22} {:>7,} bytes".format(os.path.relpath(out, ROOT), len(html.encode())))

    # robots.txt
    robots = """User-agent: *
Allow: /

# Crawler AI / GEO — accesso consentito
User-agent: GPTBot
Allow: /
User-agent: OAI-SearchBot
Allow: /
User-agent: ChatGPT-User
Allow: /
User-agent: ClaudeBot
Allow: /
User-agent: Claude-Web
Allow: /
User-agent: PerplexityBot
Allow: /
User-agent: Google-Extended
Allow: /
User-agent: Applebot-Extended
Allow: /
User-agent: CCBot
Allow: /

Sitemap: {base}/sitemap.xml
""".format(base=BASE)
    open(os.path.join(ROOT, "robots.txt"), "w", encoding="utf-8").write(robots)

    # sitemap.xml
    urls = []
    for t in LANGS:
        loc = BASE + t["path"]
        alts = "".join(
            '<xhtml:link rel="alternate" hreflang="{}" href="{}"/>'.format(o["lang"], BASE + o["path"])
            for o in LANGS
        ) + '<xhtml:link rel="alternate" hreflang="x-default" href="{}/"/>'.format(BASE)
        urls.append(
            "<url><loc>{}</loc>{}<changefreq>weekly</changefreq><priority>{}</priority></url>".format(
                loc, alts, "1.0" if t["path"] == "/" else "0.9")
        )
    sitemap = (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" '
        'xmlns:xhtml="http://www.w3.org/1999/xhtml">\n' + "\n".join(urls) + "\n</urlset>\n"
    )
    open(os.path.join(ROOT, "sitemap.xml"), "w", encoding="utf-8").write(sitemap)

    # llms.txt (GEO / AEO)
    it = LANGS[0]
    llms = """# Latin America Mission — Ceará, Brasile

> Missione imprenditoriale italiana nello Stato del Ceará (Brasile), 16–23 novembre 2026.
> Promossa dallo Studio Armando Rossi & Partners con la partecipazione di Italink e il
> supporto istituzionale del Governo dello Stato del Ceará, della FIEC, della Camera
> Italo-Brasiliana di Commercio e Industria e del Sistema Italia.

## In breve
- Date: 16–23 novembre 2026
- Luogo: Fortaleza, Stato del Ceará, Brasile
- Formato: incontri B2B, visite istituzionali e tecniche (Porto di Pecém, FTZ Ceará), networking
- Settori della missione: {sectors}
- Progetto di punta presentato: Rinascimento Design District, con le filiere di {segments}
- Adesioni: aperte fino a esaurimento posti
- Contatti: {email} · {phone}

## Pagine
- [Sito ufficiale (IT)]({base}/): programma, settori, partner, FAQ e modulo di adesione
- [Official website (EN)]({base}/en/): programme, sectors, partners, FAQ and application form
- [Site oficial (PT-BR)]({base}/pt/): programação, setores, parceiros, perguntas frequentes e formulário de inscrição

## Documenti
- [Economic Report del Governo dello Stato del Ceará (PDF, inglese, 1º luglio 2026)]({base}/assets/{doc}):
  bollettino della Segreteria dello Sviluppo Economico (SDE) con l'arrivo di MG Motor nel polo
  automotive, la crescita del PIL statale, la FTZ Ceará e la presentazione del Pecém Multimodal
  Hub insieme alla Latin America Mission.

## Domande frequenti
{faq}
""".format(
        base=BASE, email=SITE["email"], phone=SITE["phone_display"], doc=DOC_FILE,
        sectors=", ".join(plain(s[1]) for s in it["sectors"]).lower(),
        segments=", ".join(plain(s[0]) for s in it["segments"]).lower(),
        faq="\n".join("- **{}** {}".format(plain(q), plain(a)) for q, a in it["faq"]),
    )
    open(os.path.join(ROOT, "llms.txt"), "w", encoding="utf-8").write(llms)

    # 404
    n404 = """<!doctype html><html lang="it"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1"><title>Pagina non trovata — Latin America Mission</title>
<meta name="robots" content="noindex"><style>{css}</style></head>
<body style="background:#0a1729;color:#e9e4d8;min-height:100vh;display:grid;place-items:center;text-align:center">
<div class="wrap"><p class="eyebrow on-dark">Errore 404</p>
<h1 style="font-size:clamp(2rem,6vw,3.4rem);color:#fff;margin:14px 0 16px">Pagina non trovata</h1>
<p style="color:#a6b2c1;max-width:52ch;margin:0 auto 30px">La pagina che cerchi non esiste o è stata spostata. Torna alla home della Latin America Mission.</p>
<a href="/" class="btn btn-gold">Torna alla home</a></div></body></html>
""".format(css=minify_css(css_raw))
    open(os.path.join(ROOT, "404.html"), "w", encoding="utf-8").write(n404)

    # .nojekyll per GitHub Pages
    open(os.path.join(ROOT, ".nojekyll"), "w").write("")

    print("  robots.txt · sitemap.xml · llms.txt · 404.html")

    print("\n  Zone immagine")
    missing = 0
    for slot, spec in IMAGES.items():
        ok = IMG_STATUS.get(slot, False)
        missing += 0 if ok else 1
        print("    {mark} {slot:<16} {w}x{h:<6} assets/img/{f}{note}".format(
            mark="ok" if ok else "--", slot=slot, w=spec["w"], h=spec["h"],
            f=spec["file"],
            note="" if ok else ("   (opzionale)" if spec.get("silent") else "   DA FORNIRE")))
    print("    {}/{} slot ancora vuoti".format(missing, len(IMAGES)))


if __name__ == "__main__":
    main()
