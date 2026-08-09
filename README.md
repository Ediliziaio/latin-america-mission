# Latin America Mission — Ceará, Brasile · 16–23 novembre 2026

Sito ufficiale della missione imprenditoriale promossa dallo **Studio Armando Rossi & Partners**
con la partecipazione di Italink e il supporto istituzionale del Governo dello Stato del Ceará,
della FIEC, della Camera Italo-Brasiliana di Commercio e Industria e del Sistema Italia.

HTML statico, zero dipendenze a runtime. Due pagine indipendenti (IT ed EN) generate da un
unico sorgente di contenuti.

## Struttura

```
index.html            pagina IT   (generata — non modificare a mano)
en/index.html         pagina EN   (generata — non modificare a mano)
robots.txt sitemap.xml llms.txt 404.html   (generati)
assets/
  fonts/              Inter Tight variable, subset latin + latin-ext, self-hosted
  img/                loghi istituzionali (WebP), favicon, immagine OG
src/
  content.py          TUTTI i testi, IT ed EN  ←  si modifica qui
  styles.css          design system
  site.js             header, menu, reveal, scrollspy, form
  build.py            generatore
  audit.mjs           audit automatico (Playwright)
```

## Comandi

Rigenerare il sito dopo una modifica ai testi o al CSS:

```bash
python3 src/build.py
```

Server locale di anteprima:

```bash
python3 -m http.server 8231
```

Audit automatico (screenshot full-page, errori console, risorse rotte, gerarchia heading,
alt mancanti, target touch WCAG 2.2, contrasto AA, overflow orizzontale, meta e JSON-LD):

```bash
npm install && npx playwright install chromium
node src/audit.mjs http://localhost:8231
```

Esce con codice 1 se trova problemi. Gli screenshot finiscono in `.audit/`.

## Modificare i contenuti

Tutti i testi stanno in [`src/content.py`](src/content.py), nei dizionari `IT` e `EN`.
Le due lingue hanno la stessa struttura: se aggiungi una chiave in una, aggiungila anche
nell'altra. Poi `python3 src/build.py`.

Dati di sito (email, telefono, date, dominio) nel dizionario `SITE` in cima allo stesso file.

## Modulo di adesione

Di default il form **non ha un endpoint**: alla conferma apre il client di posta con tutti i
campi precompilati verso `info@studioavvocatorossi.it`.

Per farlo inviare davvero in background, imposta l'endpoint in `SITE["form_endpoint"]`
(`src/content.py`) e rigenera. Il form fa un `POST` JSON con i campi
`company, contact, role, email, phone, country, participants, sector, interest, message,
privacy, page`. Funziona con Formspree, Make, n8n, Zapier o un webhook proprio.
È già presente un honeypot anti-bot (campo `website`).

## Performance

Il CSS e il JS sono **inlinati** nelle pagine: nessuna richiesta bloccante in render.
Peso totale per pagina ~132 kB, 5 richieste, di cui 3 loghi in lazy-load.

## SEO

- Pagine separate per lingua con `hreflang` reciproci e `x-default` sull'italiano
- Canonical, Open Graph, Twitter Card, immagine OG 1200×630 dedicata
- JSON-LD: `Organization`, `BusinessEvent`, `FAQPage`, `WebPage`
- `sitemap.xml` con alternate per lingua, `robots.txt` con crawler AI abilitati, `llms.txt` per GEO/AEO

## Da completare

- [ ] Endpoint del modulo di adesione (`SITE["form_endpoint"]`)
- [ ] Verificare in FAQ costi, tempi di adesione e servizi inclusi: i testi attuali sono
      formulati in modo prudente e vanno confermati dallo Studio
- [ ] Pagina privacy policy e cookie policy (il form raccoglie dati personali)
- [ ] Collegare il dominio `latinamericamission.armandorossi.it`
