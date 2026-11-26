# Helpendz landing page (www.helpendz.com)

This is a one-page marketing site for Helpendz (Computer Science Group 73, ATP CW1).

- **Languages:** English (default), Sinhala and Tamil, with a switch in the header.
- **Display modes:** light and dark, with a switch in the header.
- **Tech:** plain HTML, CSS and JavaScript. There is no framework and no build step to run the site.

## Files

| File | Purpose |
|---|---|
| `index.html` | The page, in English. It is generated; see "Editing text" below. |
| `i18n.js` | All page text in en/si/ta (generated from `src/strings.py`). |
| `main.js` | Language switch, dark mode, mobile menu, the "How it works" steps and the waitlist form. |
| `styles.css` | All styles. Colours and sizes follow `DESIGN.md`. |
| `privacy.html` | Privacy notice for the waitlist. |
| `config.js` | Public Supabase URL and anon key for the waitlist. |
| `supabase_waitlist.sql` | Creates the insert-only `waitlist` table (now includes a `language` column). |
| `assets/photos/` | Ten Unsplash photos, as WebP at 720 and 1280 px. |
| `assets/screens/` | App screens H01–H17 from the Figma prototype. |
| `assets/fonts/` | Self-hosted Inter, Familjen Grotesk, Noto Sans Sinhala and Noto Sans Tamil, with their OFL licences. |
| `assets/og-image.jpg` | 1200×630 social preview image. |
| `src/strings.py`, `src/build.py` | The source of all text, and the script that writes `index.html` and `i18n.js`. |

## Editing text

All copy lives in `src/strings.py`. Each entry has three versions: (English, Sinhala, Tamil).

After editing, run:

```
python3 src/build.py
```

This rewrites `index.html` and `i18n.js`.

**Before launch:** a native Sinhala speaker and a native Tamil speaker should read both language versions on a phone.

## Language and theme

**Language**
- The page opens in English.
- Visitors switch with **EN / සිං / தமி** in the header.
- The choice is kept in the browser (`localStorage`) and in the address as `?lang=si` or `?lang=ta`, so a Tamil or Sinhala link can be shared.

**Dark mode**
- The first visit follows the phone or computer setting.
- The moon/sun button overrides that, and the choice is remembered.


## Checks done

- Rendered at 375 / 390 px (phone), 768 px (tablet) and 1440 px (desktop), in light and dark, in all three languages.
- No horizontal scrolling at any of these widths.
- Keyboard only:
  - every link, button, FAQ item and form field is reachable;
  - all of them have a visible amber focus ring;
  - there is a skip link;
  - the menu closes with Esc.
- Form:
  - empty submit shows the error message under each field and moves focus to the first one;
  - a valid submit shows the success message.
- No console errors.
