(function () {
  'use strict';

  var FORM_ENDPOINT = '__ENDPOINT__';
  var CONTACT_EMAIL = '__EMAIL__';
  var TXT_SENDING = '__SENDING__';
  var TXT_ERROR = '__ERROR__';
  var TXT_SUBJECT = '__SUBJECT__';

  // ---------------------------------------------------------------- header
  var header = document.getElementById('header');
  var scrolled = false;
  function onScroll() {
    var now = window.scrollY > 24;
    if (now !== scrolled) {
      scrolled = now;
      header.classList.toggle('scrolled', now);
    }
  }
  onScroll();
  window.addEventListener('scroll', onScroll, { passive: true });

  // ---------------------------------------------------------------- mobile menu
  var toggle = document.getElementById('menuToggle');
  var links = document.getElementById('navLinks');
  function closeMenu() {
    links.classList.remove('open');
    toggle.setAttribute('aria-expanded', 'false');
  }
  toggle.addEventListener('click', function () {
    var open = links.classList.toggle('open');
    toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
    if (open) header.classList.add('scrolled');
  });
  links.addEventListener('click', function (e) {
    if (e.target.tagName === 'A') closeMenu();
  });
  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape') closeMenu();
  });

  // ---------------------------------------------------------------- reveal on scroll
  var reveals = document.querySelectorAll('.reveal');
  if ('IntersectionObserver' in window &&
      !window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) {
          en.target.classList.add('in');
          io.unobserve(en.target);
        }
      });
    }, { rootMargin: '0px 0px -8% 0px', threshold: 0.06 });
    reveals.forEach(function (el) { io.observe(el); });
  } else {
    reveals.forEach(function (el) { el.classList.add('in'); });
  }

  // ---------------------------------------------------------------- scrollspy
  var navMap = {};
  document.querySelectorAll('.nav-links a[href^="#"]').forEach(function (a) {
    navMap[a.getAttribute('href').slice(1)] = a;
  });
  var spied = Object.keys(navMap).map(function (id) { return document.getElementById(id); })
                    .filter(Boolean);
  if ('IntersectionObserver' in window && spied.length) {
    var current = null;
    var spy = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (!en.isIntersecting) return;
        if (current) current.removeAttribute('aria-current');
        current = navMap[en.target.id];
        if (current) current.setAttribute('aria-current', 'true');
      });
    }, { rootMargin: '-45% 0px -50% 0px' });
    spied.forEach(function (el) { spy.observe(el); });
  }

  // ---------------------------------------------------------------- form
  var form = document.getElementById('joinForm');
  if (!form) return;
  var card = document.getElementById('formCard');
  var status = document.getElementById('formStatus');
  var btn = document.getElementById('submitBtn');
  var btnLabel = btn.textContent;

  function collect() {
    var fd = new FormData(form);
    var data = {};
    fd.forEach(function (v, k) {
      if (k === 'interest') {
        data.interest = data.interest ? data.interest + ', ' + v : v;
      } else {
        data[k] = v;
      }
    });
    data.privacy = form.privacy.checked ? 'yes' : 'no';
    data.page = location.href;
    return data;
  }

  function mailtoFallback(data) {
    var lines = [];
    Object.keys(data).forEach(function (k) {
      if (k !== 'website' && data[k]) lines.push(k + ': ' + data[k]);
    });
    return 'mailto:' + CONTACT_EMAIL +
      '?subject=' + encodeURIComponent(TXT_SUBJECT) +
      '&body=' + encodeURIComponent(lines.join('\n'));
  }

  form.addEventListener('submit', function (e) {
    e.preventDefault();
    status.classList.remove('err');
    status.textContent = '';

    if (!form.checkValidity()) {
      form.reportValidity();
      return;
    }
    // honeypot
    if (form.website && form.website.value) {
      card.classList.add('sent');
      return;
    }

    var data = collect();
    delete data.website;

    if (!FORM_ENDPOINT) {
      window.location.href = mailtoFallback(data);
      card.classList.add('sent');
      return;
    }

    btn.disabled = true;
    status.textContent = TXT_SENDING;

    fetch(FORM_ENDPOINT, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json', Accept: 'application/json' },
      body: JSON.stringify(data)
    }).then(function (r) {
      if (!r.ok) throw new Error(r.status);
      card.classList.add('sent');
      card.scrollIntoView({ behavior: 'smooth', block: 'center' });
    }).catch(function () {
      status.classList.add('err');
      status.textContent = TXT_ERROR;
      btn.disabled = false;
      btn.textContent = btnLabel;
    });
  });
})();
