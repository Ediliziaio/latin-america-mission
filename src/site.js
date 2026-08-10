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

  // ---------------------------------------------------------------- countdown
  var heroMeta = document.getElementById('heroMeta');
  if (heroMeta) {
    var start = new Date('__START__T00:00:00');
    var days = Math.ceil((start - new Date()) / 86400000);
    var box = document.createElement('div');
    box.className = 'count';
    if (days > 0) {
      box.innerHTML = '__COUNT_LABEL__<strong>' + days + ' __COUNT_UNIT__</strong>';
    } else if (days > -8) {
      box.innerHTML = '<strong>__COUNT_TODAY__</strong>';
    }
    if (box.innerHTML) heroMeta.appendChild(box);
  }

  // ---------------------------------------------------------------- add to calendar
  var icsBtn = document.getElementById('icsBtn');
  if (icsBtn) {
    icsBtn.addEventListener('click', function () {
      var pad = function (n) { return String(n).padStart(2, '0'); };
      var d = function (s, add) {
        var x = new Date(s + 'T00:00:00');
        if (add) x.setDate(x.getDate() + add);
        return x.getFullYear() + pad(x.getMonth() + 1) + pad(x.getDate());
      };
      var ics = [
        'BEGIN:VCALENDAR', 'VERSION:2.0', 'PRODID:-//Latin America Mission//IT',
        'BEGIN:VEVENT',
        'UID:latin-america-mission-2026@' + location.hostname,
        'DTSTART;VALUE=DATE:' + d('__START__'),
        'DTEND;VALUE=DATE:' + d('__END__', 1), // DTEND e' esclusivo
        'SUMMARY:__ICS_TITLE__',
        'LOCATION:Fortaleza, Ceara, Brasile',
        'DESCRIPTION:' + location.origin + location.pathname,
        'URL:' + location.origin + location.pathname,
        'END:VEVENT', 'END:VCALENDAR'
      ].join('\r\n');
      var a = document.createElement('a');
      a.href = 'data:text/calendar;charset=utf-8,' + encodeURIComponent(ics);
      a.download = 'latin-america-mission-2026.ics';
      a.click();
    });
  }

  // ---------------------------------------------------------------- sticky CTA + to top
  var sticky = document.getElementById('stickyCta');
  var toTop = document.getElementById('toTop');
  var joinSection = document.getElementById('adesioni');
  function onScroll2() {
    var past = window.scrollY > window.innerHeight * 0.9;
    if (sticky) {
      // nascosta quando si e' gia' sul modulo di adesione
      var onForm = joinSection &&
        joinSection.getBoundingClientRect().top < window.innerHeight &&
        joinSection.getBoundingClientRect().bottom > 0;
      var show = past && !onForm;
      sticky.hidden = false;
      sticky.classList.toggle('in', show);
    }
    if (toTop) {
      toTop.hidden = false;
      toTop.classList.toggle('in', window.scrollY > window.innerHeight * 1.5);
    }
  }
  onScroll2();
  window.addEventListener('scroll', onScroll2, { passive: true });
  if (toTop) {
    toTop.addEventListener('click', function () {
      window.scrollTo({ top: 0, behavior: 'smooth' });
    });
  }

  // ---------------------------------------------------------------- lightbox galleria
  var lb = document.getElementById('lightbox');
  if (lb && typeof lb.showModal === 'function') {
    var lbImg = document.getElementById('lbImg');
    var lbCap = document.getElementById('lbCap');
    // anche le schede dati: su mobile il testo impresso e' piccolo, servono a schermo pieno
    document.querySelectorAll('.gal-item img, .data-card').forEach(function (im) {
      im.addEventListener('click', function () {
        lbImg.src = im.currentSrc || im.src;
        lbImg.alt = im.alt;
        var cap = im.parentElement.querySelector('figcaption');
        lbCap.textContent = cap ? cap.textContent : '';
        lb.showModal();
      });
    });
    document.getElementById('lbClose').addEventListener('click', function () { lb.close(); });
    lb.addEventListener('click', function (e) { if (e.target === lb) lb.close(); });
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
