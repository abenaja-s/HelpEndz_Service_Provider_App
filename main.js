/* Helpendz landing page: language switch, dark mode, menu, "How it works" steps, waitlist form. */
(function () {
  'use strict';
  var doc = document.documentElement;
  var DICT = window.HZ_I18N || {};
  var store = {
    get: function (k) { try { return localStorage.getItem(k); } catch (e) { return null; } },
    set: function (k, v) { try { localStorage.setItem(k, v); } catch (e) { /* private mode */ } }
  };

  /* ---------- Language ---------- */
  var current = 'en';
  function t(key) { var d = DICT[current] || DICT.en; return (d && d[key]) || (DICT.en && DICT.en[key]) || ''; }

  function applyLang(lang, save) {
    if (!DICT[lang]) lang = 'en';
    current = lang;
    doc.setAttribute('lang', lang);
    document.querySelectorAll('[data-i18n]').forEach(function (el) {
      var v = t(el.getAttribute('data-i18n'));
      if (v) el.textContent = v;
    });
    document.querySelectorAll('[data-i18n-html]').forEach(function (el) {
      var v = t(el.getAttribute('data-i18n-html'));
      if (v) el.innerHTML = v; /* strings are our own, from src/strings.py */
    });
    document.querySelectorAll('[data-i18n-attr]').forEach(function (el) {
      el.getAttribute('data-i18n-attr').split(';').forEach(function (pair) {
        var p = pair.split(':'); var v = t(p[1]);
        if (v) el.setAttribute(p[0], v);
      });
    });
    document.querySelectorAll('.lang button').forEach(function (b) {
      b.setAttribute('aria-pressed', String(b.getAttribute('data-lang') === lang));
    });
    var title = document.querySelector('.theme');
    if (title) title.title = t('theme.label');
    /* Hero phone shows the Tamil home screen when Tamil is chosen. */
    var hp = document.querySelector('#hero-phone img');
    if (hp) hp.src = 'assets/screens/' + (lang === 'ta' ? 'h15' : 'h03') + '.webp';
    setMenuLabel();
    doc.classList.remove('i18n-pending');
    if (save) {
      store.set('hz-lang', lang);
      try {
        var u = new URL(location.href);
        if (lang === 'en') u.searchParams.delete('lang'); else u.searchParams.set('lang', lang);
        history.replaceState(null, '', u.pathname + u.search + u.hash);
      } catch (e) { /* sandboxed preview */ }
    }
  }

  document.querySelectorAll('.lang button').forEach(function (b) {
    b.addEventListener('click', function () { applyLang(b.getAttribute('data-lang'), true); });
  });
  var q = new URLSearchParams(location.search).get('lang');
  applyLang(q || store.get('hz-lang') || 'en', false);

  /* ---------- Theme ---------- */
  var themeBtn = document.querySelector('.theme');
  function setTheme(mode, save) {
    doc.setAttribute('data-theme', mode);
    if (themeBtn) themeBtn.setAttribute('aria-pressed', String(mode === 'dark'));
    if (save) store.set('hz-theme', mode);
  }
  setTheme(doc.getAttribute('data-theme') === 'dark' ? 'dark' : 'light', false);
  if (themeBtn) themeBtn.addEventListener('click', function () {
    setTheme(doc.getAttribute('data-theme') === 'dark' ? 'light' : 'dark', true);
  });
  if (window.matchMedia) {
    var mq = matchMedia('(prefers-color-scheme: dark)');
    var onChange = function (e) { if (!store.get('hz-theme')) setTheme(e.matches ? 'dark' : 'light', false); };
    if (mq.addEventListener) mq.addEventListener('change', onChange);
  }

  /* ---------- Mobile menu ---------- */
  var menuBtn = document.querySelector('.menu');
  var nav = document.getElementById('nav');
  function setMenuLabel() {
    if (!menuBtn) return;
    var open = menuBtn.getAttribute('aria-expanded') === 'true';
    menuBtn.querySelector('span').textContent = t(open ? 'nav.close' : 'nav.menu');
  }
  function closeMenu() { if (!menuBtn) return; nav.classList.remove('open'); menuBtn.setAttribute('aria-expanded', 'false'); setMenuLabel(); }
  if (menuBtn && nav) {
    menuBtn.addEventListener('click', function () {
      var open = nav.classList.toggle('open');
      menuBtn.setAttribute('aria-expanded', String(open));
      setMenuLabel();
      if (open) { var first = nav.querySelector('a'); if (first) first.focus(); }
    });
    nav.querySelectorAll('a').forEach(function (a) { a.addEventListener('click', closeMenu); });
    document.addEventListener('keydown', function (e) { if (e.key === 'Escape' && nav.classList.contains('open')) { closeMenu(); menuBtn.focus(); } });
  }

  /* ---------- How it works: steps drive the phone ---------- */
  var steps = Array.prototype.slice.call(document.querySelectorAll('.step'));
  var howImg = document.querySelector('#how-phone img');
  function showStep(i) {
    steps.forEach(function (s, j) {
      s.classList.toggle('on', i === j);
      s.querySelector('.step-btn').setAttribute('aria-pressed', String(i === j));
    });
    if (howImg) {
      var s = steps[i];
      howImg.src = 'assets/screens/' + s.getAttribute('data-screen') + '.webp';
      howImg.setAttribute('data-i18n-attr', 'alt:' + s.getAttribute('data-alt'));
      howImg.alt = t(s.getAttribute('data-alt'));
    }
  }
  steps.forEach(function (s, i) {
    s.querySelector('.step-btn').addEventListener('click', function () { showStep(i); });
  });
  var wide = window.matchMedia ? matchMedia('(min-width: 900px)') : { matches: true };
  if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (entries) {
      if (!wide.matches) return;
      entries.forEach(function (en) { if (en.isIntersecting) showStep(steps.indexOf(en.target)); });
    }, { rootMargin: '-45% 0px -45% 0px' });
    steps.forEach(function (s) { io.observe(s); });
  }

  /* ---------- "Join as a provider" preselects the role ---------- */
  document.querySelectorAll('[data-role="provider"]').forEach(function (a) {
    a.addEventListener('click', function () {
      var r = document.querySelector('input[name="role"][value="provider"]');
      if (r) r.checked = true;
    });
  });
  var heroPro = document.querySelector('.hero .btn.ghost');
  if (heroPro) heroPro.addEventListener('click', function () {
    var r = document.querySelector('input[name="role"][value="provider"]'); if (r) r.checked = true;
  });

  /* ---------- Waitlist form ---------- */
  var form = document.getElementById('waitlist-form');
  if (!form) return;
  var statusEl = document.getElementById('form-status');
  function fieldError(id, key) {
    var input = document.getElementById('f-' + id), err = document.getElementById('e-' + id);
    if (key) { err.textContent = t(key); err.hidden = false; input.setAttribute('aria-invalid', 'true'); }
    else { err.textContent = ''; err.hidden = true; input.removeAttribute('aria-invalid'); }
  }
  function status(key, ok) { statusEl.textContent = key ? t(key) : ''; statusEl.className = 'status ' + (ok ? 'ok' : 'bad'); }
  function validContact(v) {
    var phone = /^(\+94|0)7\d{8}$/;
    var email = /^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/;
    return phone.test(v.replace(/[\s-]/g, '')) || email.test(v);
  }
  ['name', 'contact'].forEach(function (id) {
    document.getElementById('f-' + id).addEventListener('input', function () { fieldError(id, null); });
  });
  document.getElementById('f-consent').addEventListener('change', function () { fieldError('consent', null); });

  form.addEventListener('submit', function (e) {
    e.preventDefault();
    status(null, true);
    var name = form.name.value.trim(), contact = form.contact.value.trim();
    var role = form.querySelector('input[name="role"]:checked').value, area = form.area.value;
    var bad = null;
    if (!name) { fieldError('name', 'wl.e.name'); bad = bad || 'f-name'; } else fieldError('name', null);
    if (!validContact(contact)) { fieldError('contact', 'wl.e.contact'); bad = bad || 'f-contact'; } else fieldError('contact', null);
    if (!form.consent.checked) { fieldError('consent', 'wl.e.consent'); bad = bad || 'f-consent'; } else fieldError('consent', null);
    if (bad) { document.getElementById(bad).focus(); return; }

    var cfg = window.HELPENDZ_CONFIG || {};
    if (!cfg.supabaseUrl || cfg.supabaseUrl.indexOf('YOUR-PROJECT') !== -1) {
      status('wl.demo', true); form.reset(); return;
    }
    var btn = form.querySelector('button[type=submit]');
    btn.disabled = true; btn.textContent = t('wl.sending');
    fetch(cfg.supabaseUrl + '/rest/v1/waitlist', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json', apikey: cfg.supabaseAnonKey, Authorization: 'Bearer ' + cfg.supabaseAnonKey, Prefer: 'return=minimal' },
      body: JSON.stringify({ name: name, contact: contact, role: role, area: area, language: current, consent: true })
    }).then(function (res) {
      if (!res.ok) throw new Error(String(res.status));
      status('wl.ok', true); form.reset();
    }).catch(function () { status('wl.fail', false); })
      .then(function () { btn.disabled = false; btn.textContent = t('wl.btn'); });
  });
})();
