import site from '../data/site.json';
export const GET = () =>
  new Response(`User-agent: *\nAllow: /\nDisallow: /search/\nDisallow: /progress/\n\nSitemap: ${new URL('/sitemap-index.xml', site.url).href}\n`, { headers: { 'Content-Type': 'text/plain' } });
