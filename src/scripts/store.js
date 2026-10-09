const KEY = 'pph_v1';
export function read() {
  try { return JSON.parse(localStorage.getItem(KEY)) || { tests: {}, exams: [] }; } catch (e) { return { tests: {}, exams: [] }; }
}
export function write(s) { try { localStorage.setItem(KEY, JSON.stringify(s)); } catch (e) {} }
