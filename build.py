# -*- coding: utf-8 -*-
"""Builds index.html (English by default) and i18n.js (en/si/ta) from strings.py."""
import json, os, html
from strings import S

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EN = {k: v[0] for k, v in S.items()}


def T(tag, key, attrs='', cls=''):
    """Element whose text comes from a string key."""
    c = f' class="{cls}"' if cls else ''
    a = f' {attrs}' if attrs else ''
    if key.endswith('_h'):
        return f'<{tag}{c}{a} data-i18n-html="{key}">{EN[key]}</{tag}>'
    return f'<{tag}{c}{a} data-i18n="{key}">{html.escape(EN[key], quote=False)}</{tag}>'


def A(key):
    """Attribute value in English (escaped)."""
    return html.escape(EN[key])


def photo(name, alt_key, sizes, cls='', eager=False, w=1280, h=853):
    load = 'fetchpriority="high"' if eager else 'loading="lazy" decoding="async"'
    return (f'<img class="{cls}" src="assets/photos/{name}-1280.webp" '
            f'srcset="assets/photos/{name}-720.webp 720w, assets/photos/{name}-1280.webp 1280w" sizes="{sizes}" '
            f'width="{w}" height="{h}" alt="{A(alt_key)}" data-i18n-attr="alt:{alt_key}" {load}>')


def phone(code, alt_key, cls='', eager=False, extra=''):
    load = '' if eager else 'loading="lazy" decoding="async"'
    return (f'<div class="phone {cls}" {extra}><img src="assets/screens/{code}.webp" width="585" height="1266" '
            f'alt="{A(alt_key)}" data-i18n-attr="alt:{alt_key}" {load}></div>')


ICON = {
    'check': '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M5 12.5l4.2 4.2L19 7"/></svg>',
    'x': '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M7 7l10 10M17 7L7 17"/></svg>',
    'id': '<svg viewBox="0 0 24 24" aria-hidden="true"><rect x="3" y="5" width="18" height="14" rx="2.5"/><circle cx="9" cy="11" r="2.2"/><path d="M5.8 16c.6-1.5 1.8-2.3 3.2-2.3s2.6.8 3.2 2.3M14.5 10h4M14.5 13.5h3"/></svg>',
    'lock': '<svg viewBox="0 0 24 24" aria-hidden="true"><rect x="5" y="10.5" width="14" height="10" rx="2.5"/><path d="M8.5 10.5V8a3.5 3.5 0 017 0v2.5M12 14.5v2.5"/></svg>',
    'code': '<svg viewBox="0 0 24 24" aria-hidden="true"><rect x="3" y="7" width="18" height="10" rx="2.5"/><path d="M7 12h.01M10.5 12h.01M14 12h.01M17.5 12h.01"/></svg>',
    'pin': '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 21s-6.5-6.1-6.5-11a6.5 6.5 0 0113 0c0 4.9-6.5 11-6.5 11z"/><circle cx="12" cy="10" r="2.3"/></svg>',
    'card': '<svg viewBox="0 0 24 24" aria-hidden="true"><rect x="3" y="5.5" width="18" height="13" rx="2.5"/><path d="M3 10h18M7 15h3"/></svg>',
    'sun': '<svg viewBox="0 0 24 24" aria-hidden="true" class="i-sun"><circle cx="12" cy="12" r="4"/><path d="M12 2.5v2M12 19.5v2M4.6 4.6l1.4 1.4M18 18l1.4 1.4M2.5 12h2M19.5 12h2M4.6 19.4L6 18M18 6l1.4-1.4"/></svg>',
    'moon': '<svg viewBox="0 0 24 24" aria-hidden="true" class="i-moon"><path d="M20 14.5A8 8 0 019.5 4a8 8 0 1010.5 10.5z"/></svg>',
    'arrow': '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"/></svg>',
    'globe': '<svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c2.5 2.6 3.7 5.6 3.7 9s-1.2 6.4-3.7 9c-2.5-2.6-3.7-5.6-3.7-9S9.5 5.6 12 3z"/></svg>',
    'menu': '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 7h16M4 12h16M4 17h16"/></svg>',
}

LOGO = ('<svg class="logo" viewBox="0 0 120 120" aria-hidden="true"><path class="lg-house" d="M14 56 L60 16 L106 56M26 50 V100 a6 6 0 0 0 6 6 H88 a6 6 0 0 0 6 -6 V50"/>'
        '<path class="lg-pin" d="M60 104 C52 92 40 80 40 66 a20 20 0 0 1 40 0 C80 80 68 92 60 104 Z"/><circle class="lg-dot" cx="60" cy="66" r="8.5"/></svg>')

LANGS = '''<div class="lang" role="group" aria-label="Language" data-i18n-attr="aria-label:lang.label">
  <button type="button" data-lang="en" lang="en" aria-pressed="true">EN</button>
  <button type="button" data-lang="si" lang="si" aria-pressed="false">සිං</button>
  <button type="button" data-lang="ta" lang="ta" aria-pressed="false">தமி</button>
</div>'''

cats = [
    ('home', 'plumber', 'big'), ('build', 'construction', ''), ('daily', 'cleaning', ''),
    ('rent', 'ladder', ''), ('vehicle', 'mechanic', 'wide'),
]
cat_html = '\n'.join(
    f'''<li class="cat {c}">{photo(p, f'cat.{k}.alt', '(min-width: 900px) 40vw, 100vw', w=1280, h=1280)}
      <div class="cat-txt">{T('h3', f'cat.{k}')}{T('p', f'cat.{k}.d')}</div></li>''' for k, p, c in cats)

steps = [('h04', 'how.alt1'), ('h06', 'how.alt2'), ('h09', 'how.alt3'), ('h07', 'how.alt4'), ('h16', 'how.alt5'), ('h10', 'how.alt6')]
step_html = '\n'.join(
    f'''<li class="step{' on' if i == 0 else ''}" data-screen="{code}" data-alt="{alt}">
        <button type="button" class="step-btn" aria-controls="how-phone" aria-pressed="{'true' if i == 0 else 'false'}"><span class="num">{i+1}</span>{T('span', f'how.s{i+1}', cls='step-t')}</button>
        {T('p', f'how.s{i+1}.d')}
        <img class="step-shot" src="assets/screens/{code}.webp" width="585" height="1266" alt="{A(alt)}" data-i18n-attr="alt:{alt}" loading="lazy" decoding="async">
      </li>''' for i, (code, alt) in enumerate(steps))

safe_items = [('id', 1), ('lock', 2), ('code', 3), ('pin', 4), ('card', 5)]
safe_html = '\n'.join(f'<li><span class="ic">{ICON[ic]}</span><div>{T("h3", f"safe.{n}")}{T("p", f"safe.{n}.d")}</div></li>' for ic, n in safe_items)

faq_html = '\n'.join(f'<details>{T("summary", f"faq.q{i}")}{T("p", f"faq.a{i}")}</details>' for i in range(1, 9))

team_html = '\n'.join(
    f'<li><span class="avatar" aria-hidden="true">M{i}</span><b>[Member {i} name]</b>{T("span", f"team.r{i}")}</li>' for i in range(1, 5))

CREDITS = [('Sushmita Nag', 'jmTuwazuRB8'), ('Timur Shakerzianov', 'VAGbjhkxg6I'), ('Ankit Manoharan', 'GqHIevKIl7U'),
           ('Giorgio Trovato', '5TXz228u4eo'), ('Defrino Maasy', 'eJ3TTxG-CmE'), ('Johan Mouchet', 'eEiYhXX9aNE'),
           ('Isaac Berrocal', 'tQ3yGo-oX20'), ('Jura', 'Hqeb3fCo_MY'), ('Marc Zeman', 'SiC0S5Jx7Bw'), ('Indu Pandey', '3wacD2E3b-I')]
credit_html = ', '.join(f'<a href="https://unsplash.com/photos/{pid}" rel="noopener">{n}</a>' for n, pid in CREDITS)

page = f'''<!doctype html>
<html lang="en" data-theme="light">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title data-i18n="meta.title">{html.escape(EN['meta.title'])}</title>
<meta name="description" content="{A('meta.desc')}" data-i18n-attr="content:meta.desc">
<link rel="canonical" href="https://www.helpendz.com/">
<link rel="alternate" hreflang="en" href="https://www.helpendz.com/?lang=en">
<link rel="alternate" hreflang="si" href="https://www.helpendz.com/?lang=si">
<link rel="alternate" hreflang="ta" href="https://www.helpendz.com/?lang=ta">
<link rel="alternate" hreflang="x-default" href="https://www.helpendz.com/">
<link rel="icon" href="assets/favicon.svg" type="image/svg+xml">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Helpendz">
<meta property="og:title" content="Helpendz — book trusted local help in Kalmunai and Nintavur">
<meta property="og:description" content="ID-verified plumbers, electricians, masons, cleaners, mechanics and tool rentals. Book a time, pay by card or cash and see them on the way. Free for customers. Coming soon.">
<meta property="og:image" content="https://www.helpendz.com/assets/og-image.jpg">
<meta property="og:image:width" content="1200"><meta property="og:image:height" content="630">
<meta property="og:url" content="https://www.helpendz.com/">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#FBFAF7" media="(prefers-color-scheme: light)">
<meta name="theme-color" content="#0D1222" media="(prefers-color-scheme: dark)">
<script>
/* Set theme and language before first paint (no flash). */
(function(){{try{{var d=document.documentElement,s=localStorage.getItem('hz-theme');
d.setAttribute('data-theme',s||(matchMedia('(prefers-color-scheme: dark)').matches?'dark':'light'));
var q=new URLSearchParams(location.search).get('lang'),l=q||localStorage.getItem('hz-lang');
if(l==='si'||l==='ta'){{d.setAttribute('lang',l);d.classList.add('i18n-pending');setTimeout(function(){{d.classList.remove('i18n-pending')}},1500);}}}}catch(e){{}}}})();
</script>
<link rel="preload" href="assets/fonts/Inter.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="assets/fonts/FamiljenGrotesk.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" as="image" href="assets/photos/customer-phone-1280.webp" imagesrcset="assets/photos/customer-phone-720.webp 720w, assets/photos/customer-phone-1280.webp 1280w" imagesizes="(min-width: 900px) 46vw, 100vw">
<link rel="stylesheet" href="styles.css">
</head>
<body>
<a class="skip" href="#main" data-i18n="skip">{EN['skip']}</a>

<header class="top" id="top">
  <div class="wrap bar">
    <a class="brand" href="#main" aria-label="Helpendz">{LOGO}<span>Helpendz</span></a>
    <nav id="nav" class="nav" aria-label="Main" data-i18n-attr="aria-label:nav.main">
      <a href="#how" data-i18n="nav.how">{EN['nav.how']}</a>
      <a href="#safety" data-i18n="nav.safety">{EN['nav.safety']}</a>
      <a href="#emergency" data-i18n="nav.emergency">{EN['nav.emergency']}</a>
      <a href="#providers" data-i18n="nav.providers">{EN['nav.providers']}</a>
      <a href="#faq" data-i18n="nav.faq">{EN['nav.faq']}</a>
      <a href="#waitlist" class="menu-only" data-i18n="nav.cta">{EN['nav.cta']}</a>
    </nav>
    <div class="tools">
      {LANGS}
      <button type="button" class="theme" aria-pressed="false" aria-label="Dark mode" data-i18n-attr="aria-label:theme.label" title="Dark mode">{ICON['moon']}{ICON['sun']}</button>
      <a class="btn sm hide-s" href="#waitlist" data-i18n="nav.cta.s">{EN['nav.cta.s']}</a>
      <button type="button" class="menu" aria-expanded="false" aria-controls="nav">{ICON['menu']}<span data-i18n="nav.menu">{EN['nav.menu']}</span></button>
    </div>
  </div>
</header>

<main id="main" tabindex="-1">

<section class="hero">
  <div class="wrap hero-grid">
    <div class="hero-copy">
      <p class="eyebrow"><span class="dot" aria-hidden="true"></span><span data-i18n="hero.eyebrow">{EN['hero.eyebrow']}</span></p>
      {T('h1', 'hero.h1')}
      {T('p', 'hero.lead', cls='lead')}
      <div class="ctas">
        <a class="btn" href="#waitlist" data-i18n="nav.cta">{EN['nav.cta']}</a>
        <a class="btn ghost" href="#providers" data-i18n="hero.cta2">{EN['hero.cta2']}</a>
      </div>
      <ul class="facts">
        <li>{ICON['check']}<span data-i18n="hero.f1">{EN['hero.f1']}</span></li>
        <li>{ICON['check']}<span data-i18n="hero.f2">{EN['hero.f2']}</span></li>
        <li>{ICON['globe']}<span><span lang="si">සිංහල</span> · <span lang="ta">தமிழ்</span> · <span lang="en">English</span></span></li>
      </ul>
    </div>
    <div class="hero-art">
      <figure class="hero-photo">{photo('customer-phone', 'hero.photo.alt', '(min-width: 900px) 46vw, 100vw', eager=True, w=1280, h=841)}</figure>
      {phone('h03', 'hero.screen.alt', cls='hero-phone', eager=True, extra='id="hero-phone"')}
      <div class="track-card" aria-hidden="true">
        <span class="live"></span>
        <div><b data-i18n="hero.card.t">{EN['hero.card.t']}</b><small data-i18n="hero.card.s">{EN['hero.card.s']}</small></div>
      </div>
      <div class="badge-card" aria-hidden="true">{ICON['check']}<span data-i18n="hero.badge">{EN['hero.badge']}</span></div>
      <svg class="route" viewBox="0 0 300 160" aria-hidden="true"><path d="M8 150 C70 140 60 70 130 78 S220 120 290 14"/></svg>
    </div>
  </div>
</section>

<section class="problem" aria-labelledby="prob-h">
  <div class="wrap">
    {T('p', 'prob.kicker', cls='kicker')}
    {T('h2', 'prob.h2', attrs='id="prob-h"')}
    <div class="vs">
      <div class="today">
        {T('h3', 'prob.today')}
        <ul>{''.join(f'<li>{ICON["x"]}<span data-i18n="prob.t{i}">{EN[f"prob.t{i}"]}</span></li>' for i in range(1,5))}</ul>
      </div>
      <div class="with">
        {T('h3', 'prob.with')}
        <ul>{''.join(f'<li>{ICON["check"]}<span data-i18n="prob.w{i}">{EN[f"prob.w{i}"]}</span></li>' for i in range(1,5))}</ul>
      </div>
    </div>
  </div>
</section>

<section class="cats-sec" id="services" aria-labelledby="cats-h">
  <div class="wrap">
    <div class="sec-head">
      <div>{T('p', 'cats.kicker', cls='kicker')}{T('h2', 'cats.h2', attrs='id="cats-h"')}</div>
      {T('p', 'cats.lead', cls='sec-lead')}
    </div>
    <ul class="cats">
{cat_html}
    </ul>
  </div>
</section>

<section class="how" id="how" aria-labelledby="how-h">
  <div class="wrap how-grid">
    <div>
      {T('p', 'how.kicker', cls='kicker')}
      {T('h2', 'how.h2', attrs='id="how-h"')}
      <ol class="steps">
{step_html}
      </ol>
    </div>
    <div class="how-phone-wrap" aria-live="polite">
      {phone('h04', 'how.alt1', cls='how-phone', extra='id="how-phone"')}
    </div>
  </div>
</section>

<section class="safety" id="safety" aria-labelledby="safe-h">
  <div class="wrap safe-grid">
    <div class="safe-art">
      <figure class="safe-photo">{photo('home-phone', 'safe.alt', '(min-width: 900px) 40vw, 100vw', w=1280, h=1600)}</figure>
      <div class="code-card" aria-hidden="true"><small data-i18n="safe.code">{EN['safe.code']}</small><b>482&nbsp;917</b><small data-i18n="safe.code.s">{EN['safe.code.s']}</small></div>
    </div>
    <div>
      {T('p', 'safe.kicker', cls='kicker')}
      {T('h2', 'safe.h2', attrs='id="safe-h"')}
      {T('p', 'safe.lead', cls='sec-lead')}
      <ul class="checks">
{safe_html}
      </ul>
      {T('p', 'safe.note', cls='fine')}
    </div>
  </div>
</section>

<section class="emergency" id="emergency" aria-labelledby="em-h">
  <div class="wrap em-grid">
    <div class="em-copy">
      <p class="kicker red" data-i18n="em.kicker">{EN['em.kicker']}</p>
      {T('h2', 'em.h2', attrs='id="em-h"')}
      {T('p', 'em.p', cls='sec-lead')}
      <p class="em-note" role="note" data-i18n-html="em.note_h">{EN['em.note_h']}</p>
    </div>
    <div class="em-art">
      <figure class="em-photo">{photo('flat-tyre', 'em.alt', '(min-width: 900px) 48vw, 100vw', w=1280, h=857)}</figure>
      {phone('h08', 'em.screen.alt', cls='em-phone')}
    </div>
  </div>
</section>

<section class="local" aria-labelledby="loc-h">
  <div class="wrap loc-grid">
    <figure class="loc-photo">{photo('tuk-tuks', 'loc.alt', '(min-width: 900px) 42vw, 100vw', w=1280, h=1707)}</figure>
    <div class="loc-copy">
      {T('p', 'loc.kicker', cls='kicker')}
      {T('h2', 'loc.h2', attrs='id="loc-h"')}
      {T('p', 'loc.p', cls='sec-lead')}
      <div class="langs-demo">
        {T('h3', 'lang.h3')}
        {T('p', 'lang.p')}
        <div class="two-phones">
          <figure>{phone('h03', 'lang.en.alt')}<figcaption lang="en">English</figcaption></figure>
          <figure>{phone('h15', 'lang.ta.alt')}<figcaption lang="ta">தமிழ்</figcaption></figure>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="providers" id="providers" aria-labelledby="pro-h">
  <div class="wrap pro-grid">
    <div class="pro-copy">
      {T('p', 'pro.kicker', cls='kicker light')}
      {T('h2', 'pro.h2', attrs='id="pro-h"')}
      <ul class="pro-list">{''.join(f'<li>{ICON["check"]}<span data-i18n="pro.{i}">{EN[f"pro.{i}"]}</span></li>' for i in range(1,6))}</ul>
      <div class="ctas"><a class="btn on-dark" href="#waitlist" data-role="provider" data-i18n="pro.cta">{EN['pro.cta']}</a></div>
      {T('p', 'pro.note', cls='fine light')}
    </div>
    <div class="pro-art">
      <figure class="pro-photo">{photo('electrician', 'pro.alt', '(min-width: 900px) 44vw, 100vw', w=1280, h=853)}</figure>
      {phone('h11', 'pro.screen.alt', cls='pro-phone')}
    </div>
  </div>
</section>

<section class="team" id="team" aria-labelledby="team-h">
  <div class="wrap team-grid">
    <div>{T('p', 'team.kicker', cls='kicker')}{T('h2', 'team.h2', attrs='id="team-h"')}{T('p', 'team.p', cls='sec-lead')}</div>
    <ul class="members">
{team_html}
    </ul>
  </div>
</section>

<section class="faq" id="faq" aria-labelledby="faq-h">
  <div class="wrap faq-grid">
    <div>{T('p', 'faq.kicker', cls='kicker')}{T('h2', 'faq.h2', attrs='id="faq-h"')}</div>
    <div class="qa">
{faq_html}
    </div>
  </div>
</section>

<section class="waitlist" id="waitlist" aria-labelledby="wl-h">
  <div class="wrap wl-grid">
    <div class="wl-copy">
      {T('p', 'wl.kicker', cls='kicker')}
      {T('h2', 'wl.h2', attrs='id="wl-h"')}
      {T('p', 'wl.p', cls='sec-lead')}
      <ul class="facts col">
        <li>{ICON['check']}<span data-i18n="wl.side1">{EN['wl.side1']}</span></li>
        <li>{ICON['check']}<span data-i18n="wl.side2">{EN['wl.side2']}</span></li>
        <li>{ICON['check']}<span data-i18n="wl.side3">{EN['wl.side3']}</span></li>
      </ul>
    </div>
    <form id="waitlist-form" class="form" novalidate>
      <div class="field">
        <label for="f-name" data-i18n="wl.name">{EN['wl.name']}</label>
        <input id="f-name" name="name" autocomplete="name" required maxlength="80" aria-describedby="e-name">
        <p class="err" id="e-name" hidden></p>
      </div>
      <div class="field">
        <label for="f-contact" data-i18n="wl.contact">{EN['wl.contact']}</label>
        <input id="f-contact" name="contact" autocomplete="tel" inputmode="email" required maxlength="120" placeholder="{A('wl.contact.ph')}" data-i18n-attr="placeholder:wl.contact.ph" aria-describedby="e-contact">
        <p class="err" id="e-contact" hidden></p>
      </div>
      <fieldset class="field">
        <legend data-i18n="wl.role">{EN['wl.role']}</legend>
        <div class="seg">
          <label><input type="radio" name="role" value="customer" checked><span data-i18n="wl.cust">{EN['wl.cust']}</span></label>
          <label><input type="radio" name="role" value="provider"><span data-i18n="wl.prov">{EN['wl.prov']}</span></label>
        </div>
      </fieldset>
      <div class="field">
        <label for="f-area" data-i18n="wl.area">{EN['wl.area']}</label>
        <select id="f-area" name="area">
          <option value="Kalmunai" data-i18n="wl.kal">{EN['wl.kal']}</option>
          <option value="Nintavur" data-i18n="wl.nin">{EN['wl.nin']}</option>
          <option value="Other" data-i18n="wl.oth">{EN['wl.oth']}</option>
        </select>
      </div>
      <div class="field check">
        <input type="checkbox" id="f-consent" name="consent" aria-describedby="e-consent">
        <label for="f-consent" data-i18n-html="wl.consent_h">{EN['wl.consent_h']}</label>
        <p class="err" id="e-consent" hidden></p>
      </div>
      <button class="btn full" type="submit" data-i18n="wl.btn">{EN['wl.btn']}</button>
      <p class="status" id="form-status" role="status" aria-live="polite"></p>
    </form>
  </div>
</section>
</main>

<footer class="foot">
  <div class="wrap foot-grid">
    <div>
      <a class="brand light" href="#main" aria-label="Helpendz">{LOGO}<span>Helpendz</span></a>
      {T('p', 'ft.tag')}
      <p class="muted-l"><span data-i18n="ft.contact">{EN['ft.contact']}</span>: <a href="mailto:hello@helpendz.com">hello@helpendz.com</a></p>
    </div>
    <nav aria-label="On this page" data-i18n-attr="aria-label:ft.page">
      {T('h2', 'ft.page', cls='foot-h')}
      <ul>
        <li><a href="#how" data-i18n="nav.how">{EN['nav.how']}</a></li>
        <li><a href="#safety" data-i18n="nav.safety">{EN['nav.safety']}</a></li>
        <li><a href="#emergency" data-i18n="nav.emergency">{EN['nav.emergency']}</a></li>
        <li><a href="#providers" data-i18n="nav.providers">{EN['nav.providers']}</a></li>
        <li><a href="#faq" data-i18n="nav.faq">{EN['nav.faq']}</a></li>
        <li><a href="privacy.html" data-i18n="ft.privacy">{EN['ft.privacy']}</a></li>
      </ul>
    </nav>
    <div class="foot-small">
      <p data-i18n="ft.screens">{EN['ft.screens']}</p>
      <p><span data-i18n="ft.credit">{EN['ft.credit']}</span>: {credit_html}.</p>
      <p data-i18n="ft.copy">{EN['ft.copy']}</p>
    </div>
  </div>
</footer>

<script src="config.js"></script>
<script src="i18n.js"></script>
<script src="main.js"></script>
</body>
</html>
'''

open(os.path.join(ROOT, 'index.html'), 'w', encoding='utf-8').write(page)
dicts = {lang: {k: v[i] for k, v in S.items()} for i, lang in enumerate(['en', 'si', 'ta'])}
open(os.path.join(ROOT, 'i18n.js'), 'w', encoding='utf-8').write(
    '/* Generated from src/strings.py — edit the strings there and run python3 src/build.py */\n'
    'window.HZ_I18N = ' + json.dumps(dicts, ensure_ascii=False, indent=0) + ';\n')
print('ok', len(page))
