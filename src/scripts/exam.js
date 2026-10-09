import { read, write } from './store.js';

const root = document.getElementById('exam');
if (root) {
  const cfg = JSON.parse(document.getElementById('exam-cfg').textContent);
  const $ = (id) => document.getElementById(id);
  const L = ['A', 'B', 'C', 'D'];
  const NEG = 0.25;
  const shuffle = (a) => { for (let i = a.length - 1; i > 0; i--) { const j = Math.floor(Math.random() * (i + 1)); [a[i], a[j]] = [a[j], a[i]]; } return a; };
  let mix = cfg.mix;
  const v = new URLSearchParams(location.search).get('v');
  if (v === '2' && cfg.mix2) mix = cfg.mix2;
  let qs = [], ans = [], idx = 0, end = 0, tick = null, startedAt = 0, total = 0;

  const esc = (s) => String(s).replace(/[&<>]/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;' }[c]));
  const fmt = (s) => { const m = Math.floor(s / 60), r = s % 60; return (m < 10 ? '0' : '') + m + ':' + (r < 10 ? '0' : '') + r; };

  async function start() {
    $('go').disabled = true; $('go').textContent = 'Preparing your paper…';
    try {
      const groups = Object.keys(mix);
      const pools = await Promise.all(groups.map((g) => fetch('/data/pool-' + cfg.slugOf[g] + '.json').then((r) => r.json())));
      qs = [];
      groups.forEach((g, i) => shuffle(pools[i].slice()).slice(0, mix[g]).forEach((q) => qs.push({ q: q[0], o: q[1], a: q[2], e: q[3], g })));
      shuffle(qs);
    } catch (e) { $('go').disabled = false; $('go').textContent = 'Could not load. Tap to retry'; return; }
    total = qs.length; ans = new Array(total).fill(null); idx = 0;
    const secs = Math.round(total * 0.9 * 60);
    startedAt = Date.now(); end = startedAt + secs * 1000;
    $('intro').classList.add('hidden'); $('run').classList.remove('hidden');
    buildPal(); render(); window.scrollTo(0, 0);
    tick = setInterval(() => {
      const left = Math.max(0, Math.round((end - Date.now()) / 1000));
      $('timer').textContent = fmt(left); $('timer').classList.toggle('low', left < 600);
      if (left <= 0) submit(true);
    }, 500);
  }
  function buildPal() {
    const p = $('pal'); p.innerHTML = '';
    qs.forEach((_, i) => { const b = document.createElement('button'); b.textContent = i + 1; b.type = 'button'; b.onclick = () => { idx = i; render(); }; p.appendChild(b); });
  }
  function paint() {
    [...$('pal').children].forEach((b, i) => { b.className = (ans[i] != null ? 'done ' : '') + (i === idx ? 'cur' : ''); });
    $('answered').textContent = ans.filter((a) => a != null).length;
  }
  function render() {
    const q = qs[idx];
    $('qn').textContent = `Question ${idx + 1} of ${total}`;
    $('qsub').textContent = q.g;
    $('qt').textContent = q.q;
    const o = $('opts'); o.innerHTML = '';
    q.o.forEach((t, k) => {
      const li = document.createElement('li'); const b = document.createElement('button');
      b.type = 'button'; b.className = 'opt' + (ans[idx] === k ? ' right' : '');
      b.innerHTML = `<span class="l">${L[k]}</span><span style="unicode-bidi:plaintext">${esc(t)}</span>`;
      b.onclick = () => { ans[idx] = ans[idx] === k ? null : k; render(); };
      li.appendChild(b); o.appendChild(li);
    });
    $('prev').disabled = idx === 0; $('next').disabled = idx === total - 1;
    paint();
  }
  function submit(auto) {
    const un = ans.filter((a) => a == null).length;
    if (!auto && un && !confirm(un + ' question(s) unanswered. Submit the exam?')) return;
    clearInterval(tick);
    let c = 0, w = 0; const by = {};
    qs.forEach((q, i) => {
      by[q.g] = by[q.g] || { c: 0, w: 0, u: 0, n: 0 }; by[q.g].n++;
      if (ans[i] == null) by[q.g].u++; else if (ans[i] === q.a) { c++; by[q.g].c++; } else { w++; by[q.g].w++; }
    });
    const score = Math.round((c - w * NEG) * 100) / 100;
    const used = Math.min(Math.round((Date.now() - startedAt) / 1000), Math.round(total * 0.9 * 60));
    const s = read(); s.exams = s.exams || [];
    s.exams.push({ d: Date.now(), slug: cfg.slug, v: v === '2' ? 2 : 1, c, w, u: un, total, score, by });
    s.exams = s.exams.slice(-60); write(s);
    $('run').classList.add('hidden'); $('done').classList.remove('hidden');
    $('r-score').textContent = score; $('r-of').textContent = '/ ' + total;
    const pct = score / total;
    $('r-msg').textContent = pct >= 0.7 ? 'Strong. You are above a typical cut-off.' : pct >= 0.4 ? 'Above 40%, but aim for 70% or more to be safe.' : 'Below 40%. Study the explanations below and retake.';
    $('r-c').textContent = c; $('r-w').textContent = w; $('r-u').textContent = un; $('r-t').textContent = fmt(used);
    $('by').innerHTML = Object.entries(by).sort((a, b) => (a[1].c / a[1].n) - (b[1].c / b[1].n)).map(([g, x]) =>
      `<tr><td>${esc(g)}</td><td>${x.c}/${x.n}</td><td>${x.w}</td><td>${x.u}</td><td>${Math.round((x.c / x.n) * 100)}%</td></tr>`).join('');
    $('review').innerHTML = qs.map((q, i) => {
      const a = ans[i]; const st = a == null ? '⚪ Skipped' : a === q.a ? '✅ Correct' : '❌ Wrong';
      return `<article class="q"><h3><span class="qn">${i + 1}</span><span>${esc(q.q)}</span></h3><p style="margin:0 0 8px;font-weight:700">${st} · ${esc(q.g)}</p><ol class="opts" type="A">` +
        q.o.map((t, k) => `<li><div class="opt ${k === q.a ? 'right' : (k === a ? 'wrong' : '')}"><span class="l">${L[k]}</span><span style="unicode-bidi:plaintext">${esc(t)}</span></div></li>`).join('') +
        `</ol><details class="why" open><summary>Explanation</summary><p>${esc(q.e)}</p></details></article>`;
    }).join('');
    window.scrollTo(0, 0);
  }
  $('go').addEventListener('click', start);
  $('prev').addEventListener('click', () => { if (idx > 0) { idx--; render(); } });
  $('next').addEventListener('click', () => { if (idx < total - 1) { idx++; render(); } });
  $('clear').addEventListener('click', () => { ans[idx] = null; render(); });
  $('submit').addEventListener('click', () => submit(false));
  $('again').addEventListener('click', () => location.reload());
  window.addEventListener('beforeunload', (e) => { if (tick) { e.preventDefault(); e.returnValue = ''; } });
}
