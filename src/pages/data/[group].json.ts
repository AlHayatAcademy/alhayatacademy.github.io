import { groups, testsOfGroup } from '../../lib.js';

export function getStaticPaths() {
  return groups.map((g) => ({ params: { group: 'pool-' + g.slug } }));
}
export function GET({ params }) {
  const slug = params.group.replace(/^pool-/, '');
  const g = groups.find((x) => x.slug === slug);
  const qs = testsOfGroup(g.name).flatMap((t) => t.questions.map((q) => [q.q, q.o, q.a, q.e]));
  return new Response(JSON.stringify(qs), { headers: { 'Content-Type': 'application/json' } });
}
