import site from './data/site.json';
import groups from './data/groups.json';
import posts from './data/posts.json';
import qualPosts from './data/qualification-posts.json';
import jobsBase from './data/jobs.json';
import jobsSheet from './data/jobs.sheet.json';

const files = import.meta.glob('./data/tests/*.json', { eager: true });
export const tests = Object.values(files).map((m) => m.default).sort((a, b) => a.id - b.id);
export { site, groups, posts, qualPosts };

export const groupByName = Object.fromEntries(groups.map((g) => [g.name, g]));
export const testsOfGroup = (name) => tests.filter((t) => t.group === name);
export const poolSize = (name) => testsOfGroup(name).reduce((n, t) => n + t.questions.length, 0);
export const totalQuestions = tests.reduce((n, t) => n + t.questions.length, 0);
export const letters = ['A', 'B', 'C', 'D'];
export const abs = (path) => new URL(path, site.url).href;
export const mixTotal = (mix) => Object.values(mix || {}).reduce((a, b) => a + b, 0);
export const colorOf = (groupName) => (groupByName[groupName] || {}).color || '#7c3aed';

// Split `days` study days across subjects in proportion to their weight in the mix (largest remainder).
export function planDays(mix, days) {
  const entries = Object.entries(mix || {});
  const total = entries.reduce((n, [, c]) => n + c, 0);
  if (!total) return [];
  const raw = entries.map(([g, c]) => ({ g, exact: (c / total) * days }));
  raw.forEach((r) => (r.d = Math.max(1, Math.floor(r.exact))));
  let used = raw.reduce((n, r) => n + r.d, 0);
  const byFrac = [...raw].sort((a, b) => b.exact - Math.floor(b.exact) - (a.exact - Math.floor(a.exact)));
  for (let i = 0; used < days && i < byFrac.length * 3; i++, used++) byFrac[i % byFrac.length].d++;
  while (used > days) { const big = raw.sort((a, b) => b.d - a.d)[0]; if (big.d <= 1) break; big.d--; used--; }
  return raw.sort((a, b) => b.d - a.d);
}
export const ads_total = (p) => (p.ads || []).reduce((n, a) => n + (a.posts || 0), 0);

// Jobs: built-in list merged with rows from the Google Sheet (sheet wins on the same case number), newest first.
export const jobs = [...new Map([...jobsBase, ...jobsSheet].map((j) => [j.case, j])).values()]
  .sort((a, b) => (b.date || '').localeCompare(a.date || ''));
