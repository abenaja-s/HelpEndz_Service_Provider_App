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

## Placeholders still to fill

- Team member names: `[Member 1 name]` … `[Member 4 name]` in `src/build.py` (the roles are already there).
- The contact email `hello@helpendz.com`: set up the mailbox, or change it in `src/strings.py`, `src/build.py` and `privacy.html`.
- Social links: none are shown until real Facebook/Instagram pages exist. Add them to the footer in `src/build.py`.
- The waitlist database: fill in `config.js`. Until then the form shows "Demo mode" and stores nothing.

## Run locally

```
python3 -m http.server 8000
```

Then open http://localhost:8000. Use a local server rather than double-clicking the file, so the fonts load.

## Connect the waitlist

1. Create a free Supabase project.
2. Run `supabase_waitlist.sql` in the SQL Editor.
3. Put the Project URL and the anon public key into `config.js`.

## Deploy on www.helpendz.com (GitHub Pages)

1. Push this folder to the team repository and enable **Settings → Pages**.
2. Under **Custom domain**, enter `www.helpendz.com`.
3. At your domain registrar:
   - add a `CNAME` record for `www` pointing to `<your-github-user>.github.io`;
   - add the four GitHub `A` records for the bare domain so that `helpendz.com` redirects to `www`.
4. Tick **Enforce HTTPS**.

The canonical URL, `hreflang` links and Open Graph tags already use `https://www.helpendz.com/`.

## Photo credits (Unsplash License)

| Photographer | Subject |
|---|---|
| Sushmita Nag | woman with phone |
| Timur Shakerzianov | plumber |
| Ankit Manoharan | builders |
| Giorgio Trovato | cleaner |
| Defrino Maasy | ladder |
| Johan Mouchet | mechanic |
| Isaac Berrocal | flat tyre |
| Jura | three-wheelers |
| Marc Zeman | electrician |
| Indu Pandey | woman at home |

The footer links each name to the original photo. The people shown are not Helpendz users.

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
