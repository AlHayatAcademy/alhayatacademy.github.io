# PPSC Prep Hub — setup guide

Static Astro site (no database, no server). Hosts free on GitHub Pages / Cloudflare Pages / Netlify and handles traffic spikes because it is plain files on a CDN.

## 1. Before you launch (required)
Edit `src/data/site.json`:
- `url` → your real domain (also used in sitemap, canonical tags, robots.txt)
- `email` → your contact email (shown on About/Contact/Privacy pages)
- `adsenseClient` and `adsenseSlots` → fill after AdSense approval (ads render only when set)
- `gaId` → Google Analytics id (optional)
- `name` → your brand name

## 2. Run locally
```
npm install
npm run dev        # development
npm run build      # builds site + search index into dist/
```

## 3. Deploy (GitHub Pages)
1. Push this folder to a GitHub repo.
2. Settings → Pages → Source: GitHub Actions.
3. Add your custom domain in Pages settings (and a `public/CNAME` file with the domain).
4. `.github/workflows/deploy.yml` builds on every push **and every 6 hours**.

## 4. Auto-updating jobs and news (Google Sheets)
1. Create two Google Sheets using the columns in `docs/jobs-template.csv` and `docs/news-template.csv`.
2. In each: File → Share → Publish to web → choose the sheet, format **CSV** → copy the link.
3. In GitHub: Settings → Secrets and variables → Actions → Variables: add `SHEET_JOBS_CSV_URL` and `SHEET_NEWS_CSV_URL`.
4. Add a row in the sheet → within 6 hours the site rebuilds with it (or run the workflow manually for instant update).
If a sheet is unreachable the build keeps the existing data.

There is deliberately no PPSC scraper: copy new ads from ppsc.gop.pk into the sheet yourself (it takes a minute).

## 5. Adding content
- **New test**: add `src/data/tests/NN-slug.json` (same shape as the others, `group` must match a name in `groups.json`). Pages, sitemap, search and exam pools update automatically.
- **New post/syllabus**: add an entry in `src/data/posts.json` (see existing; `mix` drives the mock exam).
- **Guide**: add a Markdown file in `src/content/guides/` (frontmatter: title, description, order).
- **News**: add a Markdown file in `src/content/news/` (title, description, date, category).

## 6. SEO and monetisation checklist
- Verify the site in Google Search Console; submit `https://your-domain/sitemap-index.xml`.
- Publish news/guides regularly; fresh, accurate content is what ranks.
- Apply for AdSense once you have a domain, the legal pages (included) and steady original content.
- Keep facts verified against ppsc.gop.pk. Wrong dates/syllabi cost trust and rankings.

## Known limits
- Official CPO syllabus was not in the source archive; the CPO page says so.
- Accounting, law and mass-communication posts are marked "Not yet covered".
- The jobs list is compiled from syllabus PDFs (dates from file timestamps); it has no closing dates or fees.
