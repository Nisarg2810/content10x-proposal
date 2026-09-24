/* Tiny timeline engine: replays a list of actions on a fixed 1280x720 stage. */
(function () {
  var embed = window.self !== window.top;
  if (embed) document.documentElement.classList.add('embed');
  var S = [], T = 0, ACTS = [], stage, vp, K = 1, tap = { x: 880, y: 360 }, cfg;

  function $(s) { return stage.querySelector(s); }
  function ease(p) { return p < .5 ? 2 * p * p : 1 - Math.pow(-2 * p + 2, 2) / 2; }
  function place() { var c = $('#tap'); if (!c) return; c.style.left = tap.x + 'px'; c.style.top = tap.y + 'px'; }
  function pos(sel) {
    var e = $(sel).getBoundingClientRect(), s = stage.getBoundingClientRect();
    return { x: (e.left - s.left) / K + e.width / K * .5, y: (e.top - s.top) / K + e.height / K * .5 };
  }

  var H = {
    $: $,
    view: function (id) { return function () { stage.querySelectorAll('.fm-v,.scr').forEach(function (v) { v.classList.toggle('on', v.id === id); }); }; },
    tab: function (name) { return function () { stage.querySelectorAll('.tb').forEach(function (v) { v.classList.toggle('on', v.dataset.t === name); }); }; },
    add: function (sel, c) { return function () { stage.querySelectorAll(sel).forEach(function (e) { e.classList.add(c || 'in'); }); }; },
    rem: function (sel, c) { return function () { stage.querySelectorAll(sel).forEach(function (e) { e.classList.remove(c || 'in'); }); }; },
    move: function (sel) {
      return function (p, st) {
        if (!st.s) st.s = { x: tap.x, y: tap.y };
        var t = pos(sel), e = ease(p);
        tap.x = st.s.x + (t.x - st.s.x) * e; tap.y = st.s.y + (t.y - st.s.y) * e; place();
      };
    },
    press: function (sel) {
      return function (p, st) {
        if (st.d) return; st.d = 1;
        var c = $('#tap'); if (c) { c.classList.remove('hit'); void c.offsetWidth; c.classList.add('hit'); }
        if (sel) { var b = $(sel); if (b) { b.classList.add('act'); setTimeout(function () { b.classList.remove('act'); }, 200); } }
      };
    },
    type: function (sel, txt) { return function (p) { var e = $(sel); e.textContent = txt.slice(0, Math.round(txt.length * p)); e.classList.toggle('car', p < 1); }; },
    count: function (sel, to, from) { from = from || 0; return function (p) { $(sel).textContent = Math.round(from + (to - from) * ease(p)); }; },
    html: function (sel, h) { return function () { $(sel).innerHTML = h; }; },
    cls: function (sel, c) { return function () { $(sel).className = c; }; },
    style: function (sel, prop, fn) { return function (p) { stage.querySelectorAll(sel).forEach(function (el, i) { el.style[prop] = fn(ease(p), i); }); }; },
    note: function (h) { return function () { var n = $('#note'); n.innerHTML = h; n.classList.add('in'); }; },
    noteOff: function () { return function () { $('#note').classList.remove('in'); }; }
  };
  window.D = H;

  H.scene = function (title, sub, dur, acts) {
    var t0 = T, i = S.length;
    var list = [{ at: t0, dur: 0, fn: function () {
      var h = '<span class="n">' + ('0' + (i + 1)).slice(-2) + '</span><h2>' + title + '</h2><p>' + sub + '</p>';
      var c = $('#cap');
      c.innerHTML = h;
      c.classList.remove('in'); void c.offsetWidth; c.classList.add('in');
      var m = document.getElementById('mcap');
      if (m) { m.innerHTML = h; m.classList.remove('in'); void m.offsetWidth; m.classList.add('in'); }
    } }];
    acts.forEach(function (a) { list.push({ at: t0 + a[0], dur: a[1], fn: a[2] }); });
    S.push({ t0: t0, dur: dur }); ACTS = ACTS.concat(list); T += dur;
  };

  var PLAY = '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M7 4l13 8-13 8z"/></svg>';
  var PAUSE = '<svg viewBox="0 0 24 24" fill="currentColor"><rect x="5" y="4" width="5" height="16" rx="1"/><rect x="14" y="4" width="5" height="16" rx="1"/></svg>';

  H.init = function (c) {
    cfg = c;
    var mount = document.getElementById('filmMount');
    var shell =
      '<div class="film"><div class="vp" id="vp"><div id="stage"></div></div>' +
      '<div class="ctl"><button id="play" aria-label="Play or pause"></button>' +
      '<button id="again" aria-label="Restart"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4"><path d="M3 12a9 9 0 1 0 3-6.7L3 8"/><path d="M3 3v5h5"/></svg></button>' +
      '<div class="track" id="track"><div class="tb2"><i id="prog"></i></div></div><div class="tm" id="time">0:00</div></div>' +
      '<div class="mcap" id="mcap"></div>' +
      
      '<p class="fnote">' + (c.note || '') + '</p></div>';
    if (mount) mount.innerHTML = shell; else document.body.insertAdjacentHTML('afterbegin', shell);
    stage = document.getElementById('stage'); vp = document.getElementById('vp');
    function fit() {
      var w = vp.clientWidth, root = document.documentElement;
      if (w < 780) {                       /* phone: zoom into the browser window, caption drops below */
        root.classList.add('fm-narrow');
        K = (w - 16) / 716;
        stage.style.transform = 'translate(' + (8 - 420 * K) + 'px,' + (8 - 40 * K) + 'px) scale(' + K + ')';
        vp.style.height = (620 * K + 16) + 'px';
      } else {
        root.classList.remove('fm-narrow');
        K = w / 1180;
        stage.style.transform = 'scale(' + K + ')';
        vp.style.height = (700 * K) + 'px';
      }
    }
    function post() {
      if (!embed) return;
      var f = document.querySelector('.film');
      if (f) parent.postMessage({ filmH: Math.ceil(f.getBoundingClientRect().height) + 6 }, '*');
    }
    addEventListener('resize', function () { fit(); post(); }); fit();
    if (window.ResizeObserver) new ResizeObserver(post).observe(document.querySelector('.film'));
    addEventListener('load', post); setTimeout(post, 300); setTimeout(post, 1200);
    ACTS.sort(function (a, b) { return a.at - b.at; });

    var track = document.getElementById('track');
    S.forEach(function (s, i) {
      var l = s.t0 / T * 100;
      if (i) { var k = document.createElement('span'); k.className = 'tk'; k.style.left = l + '%'; track.appendChild(k); }
      var b = document.createElement('span'); b.className = 'lb'; b.style.left = l + '%'; b.textContent = c.chapters[i]; track.appendChild(b);
    });
    var labels = track.querySelectorAll('.lb');
    var t = 0, playing = false, last = null;

    function reset() { stage.innerHTML = c.stage; tap = { x: 880, y: 360 }; place(); ACTS.forEach(function (a) { a.st = {}; a.done = false; }); }
    function apply() { ACTS.forEach(function (a) { if (a.done || t < a.at) return; var p = a.dur ? Math.min(1, (t - a.at) / a.dur) : 1; a.fn(p, a.st); if (p >= 1) a.done = true; }); }
    function seek(nt) { t = Math.max(0, Math.min(T - .01, nt)); reset(); stage.classList.add('snap'); apply(); void stage.offsetWidth; stage.classList.remove('snap'); ui(); }
    function mmss(x) { x = Math.round(x); return Math.floor(x / 60) + ':' + ('0' + x % 60).slice(-2); }
    function ui() {
      document.getElementById('prog').style.width = (t / T * 100) + '%';
      document.getElementById('time').textContent = mmss(Math.floor(t)) + ' / ' + mmss(T);
      labels.forEach(function (l, i) { l.classList.toggle('on', t >= S[i].t0 && t < S[i].t0 + S[i].dur); });
      document.getElementById('play').innerHTML = playing ? PAUSE : PLAY;
    }
    function loop(ts) {
      if (last !== null && playing) { t += Math.min(.1, (ts - last) / 1000); if (t >= T) { t = T; playing = false; } apply(); ui(); }
      last = ts; requestAnimationFrame(loop);
    }
    document.getElementById('play').onclick = function () { if (!playing && t >= T) seek(0); playing = !playing; ui(); };
    document.getElementById('again').onclick = function () { seek(0); playing = true; ui(); };
    track.onclick = function (e) { var r = track.getBoundingClientRect(); seek((e.clientX - r.left) / r.width * T); };
    addEventListener('keydown', function (e) { if (e.code === 'Space') { e.preventDefault(); document.getElementById('play').click(); } });
    window.__seek = function (x) { playing = false; seek(x); };

    reset(); apply(); ui(); requestAnimationFrame(loop);
    var started = false;
    if ('IntersectionObserver' in window) {
      new IntersectionObserver(function (en) {
        if (en[0].isIntersecting && !started) { started = true; playing = true; ui(); }
      }, { threshold: .4 }).observe(vp);
    } else { playing = true; ui(); }
  };
})();
