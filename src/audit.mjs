/**
 * Audit automatico del sito: screenshot full-page, errori console, risorse rotte,
 * gerarchia heading, alt mancanti, target touch, contrasto, overflow orizzontale.
 *
 *   node src/audit.mjs [baseUrl]
 */
import { chromium } from 'playwright';
import fs from 'node:fs';
import path from 'node:path';

const BASE = process.argv[2] || 'http://localhost:8231';
const OUT = path.join(process.cwd(), '.audit');
fs.mkdirSync(OUT, { recursive: true });

const PAGES = [
  { name: 'it', url: BASE + '/' },
  { name: 'en', url: BASE + '/en/' },
  { name: 'pt', url: BASE + '/pt/' },
];
const VIEWPORTS = [
  { name: 'desktop', width: 1440, height: 900 },
  { name: 'mobile', width: 390, height: 844, isMobile: true },
];

const problems = [];
const note = (page, vp, kind, msg) =>
  problems.push({ page, vp, kind, msg });

const browser = await chromium.launch();

for (const p of PAGES) {
  for (const vp of VIEWPORTS) {
    const ctx = await browser.newContext({
      viewport: { width: vp.width, height: vp.height },
      deviceScaleFactor: 1,
      reducedMotion: 'reduce',
    });
    const page = await ctx.newPage();
    page.on('console', (m) => {
      if (m.type() === 'error') note(p.name, vp.name, 'console', m.text());
    });
    page.on('pageerror', (e) => note(p.name, vp.name, 'js', String(e)));
    page.on('requestfailed', (r) =>
      note(p.name, vp.name, 'net', r.url() + ' — ' + (r.failure()?.errorText || '')));
    page.on('response', (r) => {
      if (r.status() >= 400) note(p.name, vp.name, 'net', r.status() + ' ' + r.url());
    });

    const t0 = Date.now();
    await page.goto(p.url, { waitUntil: 'networkidle' });
    const load = Date.now() - t0;
    await page.evaluate(() =>
      document.querySelectorAll('.reveal').forEach((e) => e.classList.add('in')));
    await page.waitForTimeout(250);

    await page.screenshot({
      path: path.join(OUT, `${p.name}-${vp.name}.png`),
      fullPage: true,
    });

    const report = await page.evaluate(() => {
      const r = {};
      // horizontal overflow
      r.scrollW = document.documentElement.scrollWidth;
      r.clientW = document.documentElement.clientWidth;
      r.overflowers = [...document.querySelectorAll('body *')]
        .filter((el) => {
          const b = el.getBoundingClientRect();
          return b.width > 0 && (b.right > document.documentElement.clientWidth + 2 || b.left < -2);
        })
        .slice(0, 8)
        .map((el) => el.tagName.toLowerCase() + '.' + (el.className || '').toString().split(' ')[0]);

      // headings
      r.headings = [...document.querySelectorAll('h1,h2,h3,h4,h5,h6')]
        .map((h) => ({ l: +h.tagName[1], t: h.textContent.trim().slice(0, 60) }));

      // images without alt / dimensions
      r.badImgs = [...document.images]
        .filter((i) => i.getAttribute('src')) // le <img> riempite via JS non hanno src a riposo
        .filter((i) => !i.hasAttribute('alt') || (!i.width && !i.getAttribute('width')))
        .map((i) => i.currentSrc || i.src);

      // links without accessible name
      r.emptyLinks = [...document.querySelectorAll('a')]
        .filter((a) => !a.textContent.trim() && !a.getAttribute('aria-label') &&
                       !a.querySelector('img[alt]:not([alt=""])'))
        .map((a) => a.getAttribute('href'));

      // form labels
      r.unlabelled = [...document.querySelectorAll('input:not([type=hidden]),select,textarea')]
        .filter((el) => {
          if (el.closest('label')) return false;
          if (el.id && document.querySelector(`label[for="${el.id}"]`)) return false;
          return !el.getAttribute('aria-label');
        })
        .map((el) => el.name || el.tagName);

      // touch targets (WCAG 2.2 SC 2.5.8, 24x24 CSS px)
      // - per un input il bersaglio reale e' la label che lo racchiude
      // - i link inline dentro un paragrafo di testo rientrano nell'eccezione "inline"
      r.smallTargets = [...document.querySelectorAll('a,button,input[type=checkbox],summary')]
        .filter((el) => {
          let box = el;
          if (el.tagName === 'INPUT' && el.closest('label')) box = el.closest('label');
          if (el.tagName === 'A') {
            const par = el.parentElement;
            const own = el.textContent.trim();
            if (par && par.textContent.trim().length > own.length + 3) return false; // inline
          }
          const b = box.getBoundingClientRect();
          return b.width > 0 && b.height > 0 && (b.height < 24 || b.width < 24);
        })
        .slice(0, 10)
        .map((el) => el.tagName.toLowerCase() + ':' + el.textContent.trim().slice(0, 24));

      // meta / SEO
      const m = (s) => document.querySelector(s)?.getAttribute('content') ||
                       document.querySelector(s)?.getAttribute('href') || null;
      r.seo = {
        title: document.title,
        titleLen: document.title.length,
        desc: m('meta[name=description]'),
        descLen: (m('meta[name=description]') || '').length,
        canonical: m('link[rel=canonical]'),
        h1: [...document.querySelectorAll('h1')].map((h) => h.textContent.trim()),
        lang: document.documentElement.lang,
        hreflang: [...document.querySelectorAll('link[rel=alternate]')]
          .map((l) => l.hreflang + '→' + l.getAttribute('href')),
        jsonldTypes: [...document.querySelectorAll('script[type="application/ld+json"]')]
          .flatMap((s) => {
            try {
              const j = JSON.parse(s.textContent);
              return (j['@graph'] || [j]).map((n) => n['@type']);
            } catch (e) { return ['PARSE_ERROR']; }
          }),
      };

      // internal anchors resolve
      r.deadAnchors = [...document.querySelectorAll('a[href^="#"]')]
        .map((a) => a.getAttribute('href'))
        .filter((h) => h !== '#' && !document.querySelector(h));

      // text/bg contrast on a sample of text nodes
      function lum(c) {
        const [r0, g0, b0] = c.map((v) => {
          v /= 255;
          return v <= 0.03928 ? v / 12.92 : ((v + 0.055) / 1.055) ** 2.4;
        });
        return 0.2126 * r0 + 0.7152 * g0 + 0.0722 * b0;
      }
      function parse(s) {
        const m2 = s.match(/rgba?\(([^)]+)\)/);
        if (!m2) return null;
        const p2 = m2[1].split(',').map((x) => parseFloat(x));
        return { rgb: p2.slice(0, 3), a: p2.length > 3 ? p2[3] : 1 };
      }
      // Risale al primo sfondo opaco. Restituisce null se incontra prima un
      // gradiente/immagine: il colore effettivo non e' calcolabile in modo affidabile
      // e produrrebbe falsi positivi.
      function bgOf(el) {
        let n = el;
        while (n && n !== document.documentElement) {
          const cs = getComputedStyle(n);
          if (cs.backgroundImage && cs.backgroundImage !== 'none') return null;
          const c = parse(cs.backgroundColor);
          if (c && c.a > 0.5) return c.rgb;
          // un contenitore fixed/sticky senza sfondo opaco fluttua su contenuto
          // arbitrario: il colore reale non e' deducibile dall'albero.
          if (cs.position === 'fixed' || cs.position === 'sticky') return null;
          n = n.parentElement;
        }
        return [255, 255, 255];
      }
      r.lowContrast = [];
      const sample = [...document.querySelectorAll('p,li,h1,h2,h3,h4,a,span,label,legend,summary')]
        .filter((el) => el.textContent.trim().length > 3 && el.offsetParent !== null);
      for (const el of sample) {
        const cs = getComputedStyle(el);
        if (el.children.length && !el.textContent.replace(el.children[0]?.textContent || '', '').trim()) continue;
        const fg = parse(cs.color);
        if (!fg) continue;
        const bg = bgOf(el);
        if (!bg) continue;
        const L1 = lum(fg.rgb), L2 = lum(bg);
        const ratio = (Math.max(L1, L2) + 0.05) / (Math.min(L1, L2) + 0.05);
        const size = parseFloat(cs.fontSize);
        const bold = +cs.fontWeight >= 700;
        const large = size >= 24 || (size >= 18.66 && bold);
        const min = large ? 3 : 4.5;
        if (ratio < min) {
          r.lowContrast.push({
            sel: el.tagName.toLowerCase() + '.' + (el.className || '').toString().split(' ')[0],
            txt: el.textContent.trim().slice(0, 40),
            ratio: +ratio.toFixed(2), min, color: cs.color, size,
          });
        }
      }
      r.lowContrast = r.lowContrast.slice(0, 20);

      r.weight = performance.getEntriesByType('resource')
        .reduce((a, e) => a + (e.transferSize || 0), 0);
      r.reqs = performance.getEntriesByType('resource').length;
      return r;
    });

    // heading order
    let prev = 0;
    for (const h of report.headings) {
      if (prev && h.l > prev + 1) note(p.name, vp.name, 'a11y', `salto heading h${prev}→h${h.l} "${h.t}"`);
      prev = h.l;
    }
    if (report.seo.h1.length !== 1) note(p.name, vp.name, 'seo', `h1 count = ${report.seo.h1.length}`);
    if (report.seo.titleLen > 65) note(p.name, vp.name, 'seo', `title ${report.seo.titleLen} char`);
    if (report.seo.descLen > 165 || report.seo.descLen < 110)
      note(p.name, vp.name, 'seo', `description ${report.seo.descLen} char`);
    if (report.scrollW > report.clientW + 1)
      note(p.name, vp.name, 'layout', `overflow orizzontale ${report.scrollW}>${report.clientW}: ${report.overflowers.join(', ')}`);
    report.badImgs.forEach((s) => note(p.name, vp.name, 'a11y', 'img senza alt/dimensioni: ' + s));
    report.emptyLinks.forEach((s) => note(p.name, vp.name, 'a11y', 'link senza nome: ' + s));
    report.unlabelled.forEach((s) => note(p.name, vp.name, 'a11y', 'campo senza label: ' + s));
    report.deadAnchors.forEach((s) => note(p.name, vp.name, 'link', 'anchor inesistente: ' + s));
    report.smallTargets.forEach((s) => note(p.name, vp.name, 'a11y', 'target < 24px: ' + s));
    report.lowContrast.forEach((c) =>
      note(p.name, vp.name, 'contrast', `${c.ratio}:1 (min ${c.min}) ${c.sel} "${c.txt}" ${c.color} ${c.size}px`));

    console.log(`\n── ${p.name} / ${vp.name} — ${load}ms, ${report.reqs} req, ${(report.weight / 1024).toFixed(1)} kB`);
    if (vp.name === 'desktop') {
      console.log('   title:', report.seo.title, `(${report.seo.titleLen})`);
      console.log('   desc :', report.seo.descLen, 'char | canonical:', report.seo.canonical);
      console.log('   lang :', report.seo.lang, '| hreflang:', report.seo.hreflang.join(' '));
      console.log('   ld+json:', report.seo.jsonldTypes.join(', '));
      console.log('   headings:', report.headings.map((h) => 'h' + h.l).join(' '));
    }
    await ctx.close();
  }
}

await browser.close();

console.log('\n════════ PROBLEMI ════════');
if (!problems.length) console.log('nessuno ✓');
const byKind = {};
problems.forEach((p) => (byKind[p.kind] = byKind[p.kind] || []).push(p));
for (const [k, list] of Object.entries(byKind)) {
  console.log(`\n[${k}] ${list.length}`);
  const seen = new Set();
  list.forEach((p) => {
    const key = p.kind + p.msg;
    if (seen.has(key)) return;
    seen.add(key);
    console.log(`  · (${p.page}/${p.vp}) ${p.msg}`);
  });
}
fs.writeFileSync(path.join(OUT, 'report.json'), JSON.stringify(problems, null, 2));
console.log(`\nScreenshot in ${OUT}`);
process.exit(problems.length ? 1 : 0);
