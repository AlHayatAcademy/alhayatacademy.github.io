import { defineConfig } from 'astro/config';
import sitemap from '@astrojs/sitemap';
import { readFileSync } from 'node:fs';

const site = JSON.parse(readFileSync(new URL('./src/data/site.json', import.meta.url), 'utf8'));

export default defineConfig({
  site: site.url,
  trailingSlash: 'always',
  build: { format: 'directory' },
  integrations: [sitemap()],
});
