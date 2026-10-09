import { read, write } from './store.js';

const root = document.querySelector('[data-test]');
if (root) {
  const slug = root.dataset.test;
  const qs = [...root.querySelectorAll('.q')];
  const store = read();
  const rec = (store.tests[slug] = store.tests[slug] || { ans: [], best: 0, group: root.dataset.group });
  const $ = (id) => document.getElementById(id);
  const total = qs.length;

  function paint(i) {
    const q = qs[i], a = rec.ans[i], right = +q.dataset.a;
    const opts = [...q.querySelectorAll('.opt')];
    opts.forEach((b, k) => {
      b.disabled = a != null;
      b.classList.toggle('right', a != null && k === right);
      b.classList.toggle('wrong', a != null && k === a && k !== right);
    });
    if (a != null) q.querySelector('.why').open = true;
  }
  function stats() {
    let ans = 0, ok = 0;
    rec.ans.forEach((a, i) => { if (a != null && qs[i]) { ans++; if (a === +qs[i].dataset.a) ok++; } });
    $('s-ans').textContent = ans; $('s-ok').textContent = ok; $('s-no').textContent = ans - ok;
    $('s-pct').textContent = ans ? Math.round((ok / ans) * 100) + '%' : '0%';
    $('s-bar').style.width = (ans / total) * 100 + '%';
    const res = $('result');
    if (ans === total) {
      const pct = Math.round((ok / total) * 100);
      rec.best = Math.max(rec.best || 0, pct);
      $('r-big').textContent = `${ok} / ${total}`;
      $('r-msg').textContent = pct >= 80 ? 'Outstanding. You are exam ready on this topic.' : pct >= 60 ? 'Good. Review the ones you missed and retry.' : pct >= 40 ? 'Keep going. Read each explanation carefully.' : 'Do not worry. Study the explanations and try again.';
      res.classList.remove('hidden');
    } else res.classList.add('hidden');
    write(store);
  }
  qs.forEach((q, i) => {
    q.querySelectorAll('.opt').forEach((b, k) => b.addEventListener('click', () => {
      if (rec.ans[i] != null) return;
      rec.ans[i] = k; paint(i); stats();
    }));
    paint(i);
  });
  $('b-reset').addEventListener('click', () => {
    if (!confirm('Clear your answers for this test?')) return;
    rec.ans = []; qs.forEach((q, i) => { paint(i); q.querySelector('.why').open = false; }); stats(); window.scrollTo({ top: 0, behavior: 'smooth' });
  });
  let all = false;
  $('b-study').addEventListener('click', (e) => {
    all = !all;
    qs.forEach((q) => (q.querySelector('.why').open = all || false));
    qs.forEach((q, i) => { if (all) q.querySelectorAll('.opt')[+q.dataset.a].classList.add('right'); else paint(i); });
    e.target.textContent = all ? 'Hide answers' : 'Show all answers';
  });
  stats();
}
