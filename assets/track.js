/* Visit and click notifications. Sends one email when a page is opened and one
   the first time a given button is clicked in a session, through the EmailJS
   REST endpoint with keepalive so a click that navigates away still reports. */
(function () {
  var PUBLIC_KEY = 'QX_zYoZlN7ibZXYNv';
  var SERVICE_ID = 'nisargmehta2810';
  var TEMPLATE_ID = 'template_wa24pe8';
  var API = 'https://api.emailjs.com/api/v1.0/email/send';
  var SEL = 'a[href], button, [data-track]';

  function ss(k, v) {
    try { if (v === undefined) return sessionStorage.getItem(k); sessionStorage.setItem(k, v); } catch (e) {}
    return null;
  }
  function once(k) { if (ss(k)) return false; ss(k, '1'); return true; }

  function stamp() {
    var now = new Date(), off = -now.getTimezoneOffset(), s = off >= 0 ? '+' : '-';
    var h = Math.floor(Math.abs(off) / 60), m = Math.abs(off) % 60;
    return now.toLocaleString('en-US', { hour12: true }) + ' GMT' + s + h + (m ? ':' + (m < 10 ? '0' + m : m) : '');
  }

  var locP = null;
  function place() {
    var c = ss('c10-loc');
    if (c) return Promise.resolve(c);
    if (locP) return locP;
    locP = fetch('https://ipapi.co/json/').then(function (r) { return r.json(); }).then(function (d) {
      var p = [d.city, d.region, d.country_name].filter(Boolean).join(', ') || 'Unknown location';
      ss('c10-loc', p); return p;
    }).catch(function () { return 'Unknown location'; });
    return locP;
  }

  function send(params) {
    return fetch(API, {
      method: 'POST', keepalive: true, headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ service_id: SERVICE_ID, template_id: TEMPLATE_ID, user_id: PUBLIC_KEY, template_params: params })
    }).then(function (r) { if (!r.ok) return r.text().then(function (t) { console.warn('notify failed', r.status, t); }); })
      .catch(function (e) { console.warn('notify failed', e); });
  }

  function report(kind, label) {
    var page = (document.title || 'Untitled page').replace(/ \|.*$/, '');
    var link = location.href;
    var time = stamp();
    return place().then(function (loc) {
      var msg = kind === 'click'
        ? 'Button clicked: "' + label + '" on ' + page + ' (' + link + ') at ' + time + ' from ' + loc + '.'
        : 'Page opened: "' + page + '" (' + link + ') at ' + time + ' from ' + loc + '.';
      return send({ page_name: page, link: link, time: time, location: loc, button_label: kind === 'click' ? label : '', event: kind === 'click' ? 'Button clicked' : 'Page opened', message: msg });
    });
  }

  function start() {
    if (once('c10-v:' + location.pathname)) report('view');
    document.addEventListener('click', function (e) {
      var el = e.target.closest && e.target.closest(SEL);
      if (!el || el.closest('[data-notrack]')) return;
      var label = (el.getAttribute('data-track') || el.textContent || el.getAttribute('aria-label') || 'unknown').replace(/\s+/g, ' ').trim().slice(0, 80);
      if (!label) return;
      if (once('c10-c:' + location.pathname + '|' + label)) report('click', label);
    }, true);
  }

  if (document.readyState === 'complete') start();
  else window.addEventListener('load', start);
})();
