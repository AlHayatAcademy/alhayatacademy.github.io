// Pulls jobs and news from published Google Sheet CSVs so the site updates itself on every scheduled build.
// Set repository variables SHEET_JOBS_CSV_URL and SHEET_NEWS_CSV_URL. If unset or unreachable, the build continues unchanged.
import { writeFileSync, mkdirSync, rmSync, existsSync } from 'node:fs';

function parseCSV(text) {
  const rows = []; let row = [], cur = '', q = false;
  for (let i = 0; i < text.length; i++) {
    const c = text[i];
    if (q) { if (c === '"') { if (text[i + 1] === '"') { cur += '"'; i++; } else q = false; } else cur += c; }
    else if (c === '"') q = true;
    else if (c === ',') { row.push(cur); cur = ''; }
    else if (c === '\n') { row.push(cur); rows.push(row); row = []; cur = ''; }
    else if (c !== '\r') cur += c;
  }
  if (cur || row.length) { row.push(cur); rows.push(row); }
  const head = rows.shift().map((h) => h.trim().toLowerCase());
  return rows.filter((r) => r.some((x) => x.trim())).map((r) => Object.fromEntries(head.map((h, i) => [h, (r[i] || '').trim()])));
}
async function get(url) {
  const r = await fetch(url, { redirect: 'follow' });
  if (!r.ok) throw new Error(`HTTP ${r.status}`);
  return parseCSV(await r.text());
}
const slug = (s) => s.toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, '').slice(0, 70);
const CATS = ['Jobs', 'Syllabus', 'Results', 'Test dates', 'Updates', 'Preparation'];

const jobsUrl = process.env.SHEET_JOBS_CSV_URL, newsUrl = process.env.SHEET_NEWS_CSV_URL;

if (jobsUrl) {
  try {
    const rows = await get(jobsUrl);
    const jobs = rows.filter((r) => r.case && r.title).map((r) => ({
      case: r.case, title: r.title, bps: r.bps, dept: r.dept,
      posts: r.posts ? Number(r.posts) || null : null, basis: r.basis || '', type: r.type || '',
      date: r.date || null, closing: r.closing_date || r.closing || null,
      link: r.link || '', official: r.official_url || r.official || '',
    }));
    writeFileSync('src/data/jobs.sheet.json', JSON.stringify(jobs, null, 1));
    console.log(`sync: ${jobs.length} jobs from sheet`);
  } catch (e) { console.warn('sync: jobs sheet skipped -', e.message); }
}
if (newsUrl) {
  try {
    const rows = await get(newsUrl);
    const dir = 'src/content/news/sheet';
    if (existsSync(dir)) rmSync(dir, { recursive: true });
    mkdirSync(dir, { recursive: true });
    let n = 0;
    for (const r of rows) {
      if (!r.title || !r.date || !r.description) continue;
      const cat = CATS.includes(r.category) ? r.category : 'Updates';
      const body = (r.body || r.description).replace(/\\n/g, '\n');
      const fm = ['---', `title: ${JSON.stringify(r.title)}`, `description: ${JSON.stringify(r.description)}`, `date: ${r.date}`, `category: ${cat}`, ...(r.post ? [`post: ${r.post}`] : []), '---', '', body, ''].join('\n');
      writeFileSync(`${dir}/${r.date}-${slug(r.title)}.md`, fm); n++;
    }
    console.log(`sync: ${n} news items from sheet`);
  } catch (e) { console.warn('sync: news sheet skipped -', e.message); }
}
