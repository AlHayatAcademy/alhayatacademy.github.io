import { getCollection } from 'astro:content';
import { site, abs } from '../lib.js';
const esc = (s) => s.replace(/[&<>"]/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]));
export async function GET() {
  const items = (await getCollection('news')).sort((a, b) => +b.data.date - +a.data.date).slice(0, 50);
  const xml = `<?xml version="1.0" encoding="UTF-8"?><rss version="2.0"><channel><title>${esc(site.name)} news</title><link>${site.url}</link><description>${esc(site.tagline)}</description>` +
    items.map((i) => `<item><title>${esc(i.data.title)}</title><link>${abs(`/news/${i.id.split('/').pop()}/`)}</link><guid>${abs(`/news/${i.id.split('/').pop()}/`)}</guid><pubDate>${i.data.date.toUTCString()}</pubDate><description>${esc(i.data.description)}</description></item>`).join('') +
    `</channel></rss>`;
  return new Response(xml, { headers: { 'Content-Type': 'application/rss+xml; charset=utf-8' } });
}
