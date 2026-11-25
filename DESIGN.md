# Helpendz — DESIGN.md (landing page)

Helpendz is a local service app for Kalmunai and Nintavur. The site should feel
like a dependable neighbourhood business that happens to have a good app:
plain-spoken, warm and practical. It should not feel like a venture-funded SaaS.
The colours come from the existing app prototype (Figma H01–H17), so the site
and the app look like one product.

Direction note: UXKIN searches were not available (no plan on the account), so
this direction is based on the app's own brand and the rules below, not on a
comparison of real websites.

## Colour

There is a light theme (the default, or whatever the visitor's system prefers) and a dark theme. The visitor switches between them with the moon/sun button, and the choice is remembered in their browser.

| Token | Value | Role |
|---|---|---|
| `--ink` | #0E1A3D | Body text, headings |
| `--ink-2` | #475569 | Secondary text, captions |
| `--ink-3` | #64748B | Meta text, placeholders (large text or ≥14px only) |
| `--navy` | #14235A | Brand: logo, footer, dark bands, selected chips |
| `--blue` | #2563EB | Primary actions and links (the only action colour) |
| `--blue-700` | #1D4ED8 | Hover and pressed state of primary actions |
| `--blue-50` | #EAF1FE | Tinted panels: arrival code, info notes |
| `--red` | #E23B3B | Emergency Mode only. Never used for decoration. |
| `--red-50` | #FDF1F1 | Emergency band background |
| `--green` | #16A34A | Success, "ID verified", live location |
| `--green-50` | #DCFCE7 | Badge background |
| `--amber` | #F59E0B | Accent: the pin dot in the logo, star ratings, highlights |
| `--amber-50` | #FEF8E7 | Notes and form hints |
| `--paper` | #FBFAF7 | Page background (warm off-white, not blue-grey) |
| `--sand` | #F3EFE6 | Alternate band background |
| `--line` | #E5E1D8 | Borders and dividers on paper and sand |
| `--white` | #FFFFFF | Cards, phone screens, inputs |

Dark theme values (same roles): ink #EEF1F7, ink-2 #B8C1D3, ink-3 #94A0B8,
paper #0D1222, sand #131A2E, card #161D33, line #27304A, blue #5B8CFF (links) and
#2F63D6 (button fill), red #FF6B6B, green #4ADE80, amber #FBBF24. Photos and app
screens stay as they are.

Contrast: ink on paper 16:1. ink-2 on paper 7.4:1. White on blue 5.2:1. White on
navy 13:1. White on red is 4.0:1, so red buttons use 17px bold text (large text).

## Typography

- Display: **Familjen Grotesk** 600/700 (English headings only). Used for h1, h2 and big numbers. It is
  sturdy and slightly quirky, which reads as made-for-this rather than default.
- Text: **Inter** 400/500/600/700. This is the app's font, used for body text,
  UI and labels.
- Local scripts: **Noto Sans Sinhala** and **Noto Sans Tamil** 400–700, used
  wherever Sinhala or Tamil text appears (`:lang(si)`, `:lang(ta)` and a
  `unicode-range`, so the files load only when needed).
- All four fonts are self-hosted WOFF2 subsets in `assets/fonts` (SIL Open Font
  License), so no requests go to Google.
- Sinhala and Tamil headings use smaller sizes and a taller line height than
  English (Tamil h1 is 28–42px), because the words are longer.

| Step | Size / line height | Use |
|---|---|---|
| display | clamp(40px, 6vw, 68px) / 1.02 | Hero h1 |
| h2 | clamp(30px, 4vw, 44px) / 1.08 | Section titles |
| h3 | 22px / 1.25 | Sub-heads |
| lead | 19px / 1.55 | Hero support line, section intros |
| body | 17px / 1.6 | Paragraphs (max 66ch) |
| small | 15px / 1.5 | Captions, card meta |
| micro | 13px / 1.4, 600 | Labels, badges (sentence case) |

## Spacing

The base unit is 4px. The scale is 4, 8, 12, 16, 24, 32, 48, 64, 96, 128.

- Section padding is 96px on desktop and 64px on phone.
- Content width is 1180px, with gutters of 20px on phone and 32px on tablet and up.
- Text blocks are at most 66 characters wide.

## Shape and depth

- Radius: 8px for inputs and badges, 14px for buttons and small cards, 22px for
  panels, 40px for phone frames, and 999px for chips.
- Shadows: two in total.
  - `--shadow-1` 0 1px 2px rgba(14,26,61,.06), 0 4px 14px rgba(14,26,61,.06), for cards.
  - `--shadow-phone` 0 30px 60px -20px rgba(14,26,61,.35), for phone mockups only.
- No glassmorphism, no gradients on text, and no purple.

## Components

- **Button primary**: blue background, white 16px/600 text, 48px tall, 14px
  radius. Hover uses blue-700. Focus shows a 3px amber ring with a 2px offset.
  Disabled is 50% opacity.
- **Button secondary**: white background, 1.5px line border, ink text. Hover
  changes the border to ink.
- **Button quiet**: a text link in blue with an arrow "→" and underline on hover.
- **Emergency button**: red, used only inside the Emergency band.
- **Links**: blue with a 1px underline offset by 3px. On navy they are white.
- **Inputs**: 48px tall, white, 1.5px line border, 8px radius. Labels always
  sit above the field. Focus shows a blue border and the amber ring. Errors show
  red text under the field and `aria-invalid`.
- **Badge**: green-50 with green text, "✓ ID verified". This is the only badge style.
- **Phone mockup**: navy frame with a 40px radius and a real app screen inside.
- **Navigation**: a sticky bar on paper with the logo left and links right,
  collapsing to a "Menu" button under 860px.
- **Footer**: navy band with white text.

## Imagery and icons

- **Photos**: ten free Unsplash photos (Unsplash License) of local-feeling scenes:
  a customer with her phone, a plumber, builders, a cleaner, a ladder, a mechanic,
  a roadside flat tyre, three-wheelers outside shops, an electrician, and a woman
  at home. Each gets a 22px radius, the `--shadow-1` shadow, and a gradient only
  where text sits on it. Every photographer is credited in the footer, and the
  footer says the people shown are not Helpendz users.
- **Product**: real screens from the Figma prototype (H01–H17), always shown in
  the navy phone frame. A photo and a phone are paired and overlap slightly.
- **Icons**: simple 2px stroke line icons drawn as inline SVG at 24px, in
  `currentColor`. No emoji used as icons on the site.
- **Illustration**: a hand-drawn-feel map line (route from provider to home) is
  the only decorative graphic, reused in the hero and the tracking section.
