(function () {
  var doc = document, html = doc.documentElement;
  var tb = doc.getElementById('themeBtn');
  if (tb) tb.onclick = function () {
    var m = html.getAttribute('data-theme') === 'light' ? 'dark' : 'light';
    html.setAttribute('data-theme', m); try { localStorage.setItem('c10-theme', m); } catch (e) {}
  };
  var bg = doc.getElementById('burger');
  if (bg) bg.onclick = function () { html.classList.toggle('nav-open'); };
  doc.querySelectorAll('.sheet a').forEach(function (a) { a.onclick = function () { html.classList.remove('nav-open'); }; });
  /* headline word reveal */
  doc.querySelectorAll('h1.split, h2.split').forEach(function (h) {
    var parts = h.innerHTML.split(/(<[^>]+>[^<]*<\/[^>]+>|<[^>]+>)/).filter(Boolean), i = 0, out = '';
    h.querySelectorAll('.squig').forEach(function () {});
    var frag = doc.createElement('div'); frag.innerHTML = h.innerHTML;
    function walk(node, into) {
      node.childNodes.forEach(function (n) {
        if (n.nodeType === 3) {
          n.textContent.split(/(\s+)/).forEach(function (w) {
            if (!w.trim()) { into.appendChild(doc.createTextNode(w)); return; }
            var o = doc.createElement('span'); o.className = 'w';
            var inner = doc.createElement('span'); inner.style.setProperty('--i', i++); inner.textContent = w;
            o.appendChild(inner); into.appendChild(o);
          });
        } else if (n.nodeType === 1) {
          if (n.classList.contains('squig') || n.classList.contains('nw')) {
            var o2 = doc.createElement('span'); o2.className = 'w';
            var in2 = doc.createElement('span'); in2.style.setProperty('--i', i++); in2.appendChild(n.cloneNode(true));
            o2.appendChild(in2); into.appendChild(o2);
          } else { var c = n.cloneNode(false); walk(n, c); into.appendChild(c); }
        }
      });
    }
    var box = doc.createElement('span'); walk(frag, box);
    h.innerHTML = ''; h.appendChild(box);
  });
  /* reveal */
  if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (es) {
      es.forEach(function (e) { if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); } });
    }, { threshold: .1, rootMargin: '0px 0px -6% 0px' });
    doc.querySelectorAll('.rev,.stag,.steps,h1.split,h2.split').forEach(function (e) { io.observe(e); });
  } else doc.querySelectorAll('.rev,.stag,.steps,h1.split,h2.split').forEach(function (e) { e.classList.add('in'); });
  /* greeting: once per session, dismissed on its own or by the reader */
  var hey = doc.getElementById('hey');
  if (hey) {
    var seen = false;
    try { seen = sessionStorage.getItem('c10-hey') === '1'; } catch (e) {}
    if (seen) hey.parentNode.removeChild(hey);
    else {
      doc.documentElement.classList.add('hey-on');
      try { sessionStorage.setItem('c10-hey', '1'); } catch (e) {}
      var gone = false;
      var close = function () {
        if (gone) return; gone = true;
        hey.classList.add('out');
        doc.documentElement.classList.remove('hey-on');
        setTimeout(function () { if (hey.parentNode) hey.parentNode.removeChild(hey); }, 700);
      };
      var t = setTimeout(close, 3300);
      var early = function () { clearTimeout(t); close(); };
      hey.addEventListener('click', early);
      doc.addEventListener('keydown', early, { once: true });
      window.addEventListener('wheel', early, { once: true, passive: true });
      window.addEventListener('touchmove', early, { once: true, passive: true });
    }
  }
  var y = doc.getElementById('yr'); if (y) y.textContent = new Date().getFullYear();
})();
