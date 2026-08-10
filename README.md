# Latin America Mission — Ceará, Brasile · 16–23 novembre 2026

Sito ufficiale della missione imprenditoriale promossa dallo **Studio Armando Rossi & Partners**
con la partecipazione di Italink e il supporto istituzionale del Governo dello Stato del Ceará,
della FIEC, della Camera Italo-Brasiliana di Commercio e Industria e del Sistema Italia.

HTML statico, zero dipendenze a runtime. Tre pagine indipendenti (IT, EN, PT-BR) generate da un
unico sorgente di contenuti.

## Struttura

```
vercel.json           configurazione deploy
index.html            pagina IT    (generata — non modificare a mano)
en/index.html         pagina EN    (generata — non modificare a mano)
pt/index.html         pagina PT-BR (generata — non modificare a mano)
robots.txt sitemap.xml llms.txt 404.html   (generati)
assets/
  fonts/              Inter Tight variable, subset latin + latin-ext, self-hosted
  img/                foto della missione e schede dati (WebP), loghi, favicon, immagine OG
  docs/               documenti scaricabili (Economic Report del Governo del Ceará)
src/
  content.py          testi IT ed EN + registro delle immagini  ←  si modifica qui
  content_pt.py       testi PT-BR
  styles.css          design system
  site.js             header, menu, reveal, scrollspy, form
  build.py            generatore
  audit.mjs           audit automatico (Playwright)
  make_variants.py    genera le varianti responsive (richiede Pillow, opzionale)
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

## Deploy su Vercel

Il repo è già configurato: [`vercel.json`](vercel.json) disattiva la build (l'HTML è generato e
committato), imposta `cleanUrls` e `trailingSlash` in modo che `/en` e `/pt` servano `/en/` e
`/pt/` come nei canonical, e aggiunge cache e header di sicurezza. `.vercelignore` tiene fuori
`src/`, `node_modules/` e il tooling.

**Via dashboard (consigliato).** Su vercel.com → *Add New… → Project* → importa
`Ediliziaio/latin-america-mission` → Deploy. Da lì in poi ogni `git push` su `main` va in
produzione da solo e ogni branch ottiene la sua preview.

**Via CLI**, se preferisci dal terminale:

```bash
npm i -g vercel && cd ~/latin-america-mission && vercel --prod
```

Il primo `vercel` chiede il login nel browser e crea il progetto; i successivi deployano e basta.

**Stato: online** su https://latin-america-mission.vercel.app (progetto `latin-america-mission`,
team `ediliziaios-projects`). Ogni push su `main` ridistribuisce da solo.

### Dominio definitivo

`armandorossi.it` **non è ancora registrato** (nessun record NS), quindi `SITE["base_url"]` punta
per ora al dominio Vercel: se puntasse a un dominio inesistente, l'`og:image` non caricherebbe
nelle anteprime social e Google non indicizzerebbe nulla.

Quando `latinamericamission.armandorossi.it` esiste e lo colleghi in *Settings → Domains*,
rimetti quel dominio in `SITE["base_url"]` ([`src/content.py`](src/content.py)) e rilancia la
build: canonical, hreflang, `og:image`, `sitemap.xml` e `llms.txt` si riallineano da soli.

## Modificare i contenuti

I testi italiani e inglesi stanno in [`src/content.py`](src/content.py), nei dizionari `IT` e
`EN`; il portoghese in [`src/content_pt.py`](src/content_pt.py). Le tre lingue hanno la stessa
struttura: se aggiungi una chiave in una, aggiungila anche nelle altre — il build fallisce
subito se una manca. Poi `python3 src/build.py`.

Dati di sito (email, telefono, date, dominio) nel dizionario `SITE` in cima allo stesso file.

## Zone immagine

Il sito ha **24 slot immagine**, tutti pieni. Finché un file non esiste, al suo posto compare
un segnaposto che dice cosa mettere, in che misura e con che nome salvarlo. Non serve toccare
il codice: basta copiare l'immagine in `assets/img/` con il nome indicato e rilanciare la build.

| Slot | File | Dove compare |
|---|---|---|
| `hero` | `hero-ceara.jpg` | sfondo del hero (skyline di Fortaleza al tramonto, foto Unsplash, licenza libera anche commerciale, `unsplash.com/photos/lWMkpyKglbs`) |
| `mission_band` | `mission-band.webp` | fascia larga sotto "La missione" — waterfront di Fortaleza |
| `ceara_porto` | `ceara-porto-pecem.webp` | coppia in "Perché il Ceará" — banchine di Pecém |
| `ceara_industria` | `ceara-industria.webp` | coppia in "Perché il Ceará" — visita tecnica a Pecém |
| `rinascimento` | `rinascimento-district.webp` | render del distretto |
| `rinascimento_logo` | `rinascimento-logo.webp` | marchio del distretto, sopra il titolo di sezione |
| `gallery_1…13` | `gallery-1.webp` … `gallery-13.webp` | sezione "Il Ceará in immagini" |
| `promoter` | `promoter.webp` | blocco "Chi guida la missione" |
| `dato_*` | `dato-*.webp` | quattro schede dati in "Perché il Ceará" — **solo pagina IT** |

`python3 src/build.py` stampa a fine build l'elenco degli slot con lo stato (`ok` / `DA FORNIRE`).

La **galleria è a mosaico**: ogni foto tiene il suo rapporto d'immagine, quindi non serve
ritagliare tutto a 4:3. Basta dichiarare in `IMAGES` la misura reale del file.

### Schede dati

Le quattro infografiche del Governo del Ceará (hub portuale, energie rinnovabili, hub
tecnologico, crescita del PIL) hanno il testo **impresso nell'immagine, in italiano**: per
questo compaiono solo sulla pagina IT. La lista degli slot e il filtro di lingua sono in
`DATA_CARDS` / `DATA_CARDS_LANGS` in [`src/build.py`](src/build.py): quando arrivano le
versioni EN e PT basta aggiungere i file e allargare il filtro.

## Documenti scaricabili

`assets/docs/economic-report-ceara-2026-07.pdf` è il bollettino economico ufficiale della
Segreteria dello Sviluppo Economico del Ceará (SDE), in inglese. Compare come card di download
in fondo a "Perché il Ceará", in tutte e tre le lingue, ed è linkato in `llms.txt`.

Per sostituirlo o aggiungerne un altro: metti il PDF in `assets/docs/`, aggiorna `DOC_FILE` in
[`src/build.py`](src/build.py) e i testi `doc_*` nei tre file di contenuti. Se il file non
esiste, la card semplicemente non viene generata.

Uno slot può dichiarare `"responsive": [1200, 1600]`: in quel caso `python3 src/make_variants.py`
genera le versioni ridotte e la build emette un `srcset`, così il mobile scarica l'immagine
piccola. È così per il hero: 114 kB su mobile invece di 256.

Le didascalie, i testi alternativi e le descrizioni dei segnaposto stanno nel dizionario
`IMAGES` in [`src/content.py`](src/content.py). Le immagini della galleria sono cliccabili e si
aprono a tutto schermo (lightbox); i segnaposto no.

## Modulo di adesione

Di default il form **non ha un endpoint**: alla conferma apre il client di posta con tutti i
campi precompilati verso `info@studioavvocatorossi.it`.

Per farlo inviare davvero in background, imposta l'endpoint in `SITE["form_endpoint"]`
(`src/content.py`) e rigenera. Il form fa un `POST` JSON con i campi
`company, contact, role, email, phone, country, participants, sector, interest, message,
privacy, page`. Funziona con Formspree, Make, n8n, Zapier o un webhook proprio.
È già presente un honeypot anti-bot (campo `website`).

## Cosa c'è nella pagina

Hero → fascia loghi istituzionali → La missione → Perché il Ceará → Settori → Perché
partecipare / A chi si rivolge → Rinascimento Design District → Programma → Partner locali →
FAQ → Adesioni (modulo) → Il Ceará in immagini → Chi guida la missione → Contatti.

Interazioni: countdown ai giorni alla partenza nel hero, "Aggiungi al calendario" che genera
un `.ics`, barra CTA fissa su mobile (si nasconde quando sei già sul modulo), torna-su su
desktop, lightbox della galleria, scrollspy in navigazione, menu mobile.

## Performance

Il CSS e il JS sono **inlinati** nelle pagine: nessuna richiesta bloccante in render.
Al primo schermo il browser scarica ~336 kB su mobile e ~531 kB su desktop in 7–9 richieste
(la foto del hero pesa da sola più di tutto il resto). Le altre 23 immagini sono tutte in
`loading="lazy"` con `width`/`height` dichiarati — non causano salti di layout e arrivano solo
se l'utente scorre: a pagina interamente scorsa il totale è ~2,0–2,5 MB.

## SEO

- Tre pagine separate per lingua con `hreflang` reciproci e `x-default` sull'italiano
- Canonical, Open Graph, Twitter Card, immagine OG 1200×630 dedicata
- JSON-LD: `Organization`, `BusinessEvent`, `FAQPage`, `WebPage`
- `sitemap.xml` con alternate per lingua, `robots.txt` con crawler AI abilitati, `llms.txt` per GEO/AEO

## Da completare

- [ ] Far confermare allo Studio didascalie e testi alternativi delle foto della missione:
      sono scritti su quello che si vede nell'immagine, senza nomi di persone né sedi non
      identificabili con certezza
- [ ] Versioni EN e PT delle quattro schede dati (oggi solo sulla pagina italiana)
- [ ] Far rileggere il portoghese a un madrelingua brasiliano prima del lancio
- [ ] Endpoint del modulo di adesione (`SITE["form_endpoint"]`)
- [ ] Verificare in FAQ costi, tempi di adesione e servizi inclusi: i testi attuali sono
      formulati in modo prudente e vanno confermati dallo Studio
- [ ] Pagina privacy policy e cookie policy (il form raccoglie dati personali)
- [ ] Collegare il dominio `latinamericamission.armandorossi.it`
