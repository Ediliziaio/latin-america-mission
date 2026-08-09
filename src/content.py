# -*- coding: utf-8 -*-
"""Contenuti bilingui del sito Latin America Mission — Ceará 2026."""

SITE = {
    # Dominio pubblico attuale. Quando latinamericamission.armandorossi.it sara'
    # registrato e collegato in Vercel, rimetti quello qui e rilancia la build:
    # canonical, hreflang, og:image, sitemap e llms.txt si aggiornano da soli.
    "base_url": "https://latin-america-mission.vercel.app",
    "email": "info@studioavvocatorossi.it",
    "phone_display": "+39 338 611 5394",
    "phone_href": "+393386115394",
    "start_date": "2026-11-16",
    "end_date": "2026-11-23",
    "promoter": "Studio Armando Rossi & Partners",
    "city": "Fortaleza",
    "region": "Ceará",
    "country_it": "Brasile",
    "country_en": "Brazil",
    # Lascia vuoto per il fallback via e-mail; inserisci qui l'endpoint
    # (Google Form / Formspree / Make / webhook) per l'invio diretto.
    "form_endpoint": "",
}

LOGOS = [
    {
        "file": "governo-ceara.webp",
        "w": 554, "h": 200,
        "alt_it": "Governo dello Stato del Ceará — Segreteria dello Sviluppo Economico",
        "alt_en": "Government of the State of Ceará — Secretariat of Economic Development",
        "alt_pt": "Governo do Estado do Ceará — Secretaria do Desenvolvimento Econômico",
    },
    {
        "file": "fiec.webp",
        "w": 612, "h": 200,
        "alt_it": "FIEC — Federazione delle Industrie dello Stato del Ceará",
        "alt_en": "FIEC — Federation of Industries of the State of Ceará",
        "alt_pt": "FIEC — Federação das Indústrias do Estado do Ceará",
    },
    {
        "file": "camara-italo-brasileira.webp",
        "w": 214, "h": 200,
        "alt_it": "Camera Italo-Brasiliana di Commercio e Industria di Rio de Janeiro",
        "alt_en": "Italian-Brazilian Chamber of Commerce and Industry of Rio de Janeiro",
        "alt_pt": "Câmara Ítalo-Brasileira de Comércio e Indústria do Rio de Janeiro",
    },
]

# ---------------------------------------------------------------------------
# ZONE IMMAGINE
# ---------------------------------------------------------------------------
# Ogni voce e' uno slot del sito. Se il file esiste in assets/img/ viene usato;
# se manca, al suo posto compare un segnaposto che indica misura e nome file da
# fornire. Basta copiare l'immagine con quel nome ed eseguire python3 src/build.py.
#
# Formato consigliato: JPG (foto) o WebP. Le misure sono in pixel, gia' al
# rapporto giusto: rispettale per evitare tagli.
IMAGES = {
    # sfondo del hero: se manca resta il gradiente blu notte (nessun segnaposto)
    # Foto: Fortaleza al tramonto — Unsplash, licenza libera anche per uso
    # commerciale, attribuzione non obbligatoria. unsplash.com/photos/lWMkpyKglbs
    "hero": {
        "file": "hero-ceara.jpg", "w": 2400, "h": 1350, "silent": True,
        "responsive": [1200, 1600],
        "label_it": "Sfondo hero — vista del Ceará o del Porto di Pecém",
        "label_en": "Hero background — view of Ceará or the Port of Pecém",
        "alt_it": "Skyline di Fortaleza al tramonto, Stato del Ceará, Brasile",
        "alt_en": "Skyline of Fortaleza at sunset, State of Ceará, Brazil",
    },
    "mission_band": {
        "file": "mission-band.jpg", "w": 1920, "h": 760,
        "label_it": "Fascia missione — delegazione, tavolo istituzionale o skyline di Fortaleza",
        "label_en": "Mission band — delegation, institutional meeting or Fortaleza skyline",
        "alt_it": "Delegazione italiana in visita istituzionale nello Stato del Ceará",
        "alt_en": "Italian delegation on an institutional visit in the State of Ceará",
        "cap_it": "La missione riunisce imprese italiane, istituzioni brasiliane e sistema industriale del Ceará.",
        "cap_en": "The mission brings together Italian companies, Brazilian institutions and the industrial system of Ceará.",
    },
    "ceara_porto": {
        "file": "ceara-porto-pecem.jpg", "w": 1200, "h": 900,
        "label_it": "Porto di Pecém — banchine, terminal o vista aerea",
        "label_en": "Port of Pecém — docks, terminal or aerial view",
        "alt_it": "Porto di Pecém, hub logistico e portuale dello Stato del Ceará",
        "alt_en": "Port of Pecém, the logistics and port hub of the State of Ceará",
        "cap_it": "Porto di Pecém e FTZ Ceará",
        "cap_en": "Port of Pecém and FTZ Ceará",
    },
    "ceara_industria": {
        "file": "ceara-industria.jpg", "w": 1200, "h": 900,
        "label_it": "Industria — impianto, cava di pietra naturale o parco eolico",
        "label_en": "Industry — plant, natural stone quarry or wind farm",
        "alt_it": "Impianto industriale nello Stato del Ceará",
        "alt_en": "Industrial plant in the State of Ceará",
        "cap_it": "Manifattura ed energia rinnovabile",
        "cap_en": "Manufacturing and renewable energy",
    },
    "rinascimento": {
        "file": "rinascimento-district.jpg", "w": 1200, "h": 1000,
        "label_it": "Rinascimento Design District — render, masterplan o materiali",
        "label_en": "Rinascimento Design District — render, masterplan or materials",
        "alt_it": "Rinascimento Design District, ecosistema industriale del design nel Ceará",
        "alt_en": "Rinascimento Design District, the design industrial ecosystem in Ceará",
    },
    "gallery_1": {
        "file": "gallery-1.jpg", "w": 1200, "h": 900,
        "label_it": "Fortaleza — skyline o waterfront",
        "label_en": "Fortaleza — skyline or waterfront",
        "alt_it": "Skyline di Fortaleza, capitale dello Stato del Ceará",
        "alt_en": "Skyline of Fortaleza, capital of the State of Ceará",
        "cap_it": "Fortaleza", "cap_en": "Fortaleza",
    },
    "gallery_2": {
        "file": "gallery-2.jpg", "w": 1200, "h": 900,
        "label_it": "Incontri B2B — tavolo di lavoro con imprese",
        "label_en": "B2B meetings — working table with companies",
        "alt_it": "Incontri B2B tra imprese italiane e partner brasiliani",
        "alt_en": "B2B meetings between Italian companies and Brazilian partners",
        "cap_it": "Incontri B2B", "cap_en": "B2B meetings",
    },
    "gallery_3": {
        "file": "gallery-3.jpg", "w": 1200, "h": 900,
        "label_it": "Pietre naturali — cava, blocchi o lastre lavorate",
        "label_en": "Natural stone — quarry, blocks or finished slabs",
        "alt_it": "Lavorazione di pietre naturali nello Stato del Ceará",
        "alt_en": "Natural stone processing in the State of Ceará",
        "cap_it": "Pietre naturali e superfici", "cap_en": "Natural stone and surfaces",
    },
    "gallery_4": {
        "file": "gallery-4.jpg", "w": 1200, "h": 900,
        "label_it": "Energia — parco eolico, solare o idrogeno verde",
        "label_en": "Energy — wind farm, solar or green hydrogen",
        "alt_it": "Parco eolico nello Stato del Ceará",
        "alt_en": "Wind farm in the State of Ceará",
        "cap_it": "Energia e transizione", "cap_en": "Energy and transition",
    },
    "gallery_5": {
        "file": "gallery-5.jpg", "w": 1200, "h": 900,
        "label_it": "Visita istituzionale — firma accordo o incontro con il Governo",
        "label_en": "Institutional visit — agreement signing or meeting with the Government",
        "alt_it": "Incontro istituzionale con il Governo dello Stato del Ceará",
        "alt_en": "Institutional meeting with the Government of the State of Ceará",
        "cap_it": "Tavoli istituzionali", "cap_en": "Institutional roundtables",
    },
    "gallery_6": {
        "file": "gallery-6.jpg", "w": 1200, "h": 900,
        "label_it": "Design e arredamento — showroom, prodotto o materiali",
        "label_en": "Design and furniture — showroom, product or materials",
        "alt_it": "Showroom di design e arredamento",
        "alt_en": "Design and furniture showroom",
        "cap_it": "Design e arredamento", "cap_en": "Design and furniture",
    },
    "promoter": {
        "file": "promoter.jpg", "w": 900, "h": 1100,
        "label_it": "Ritratto — Avv. Armando Rossi o team dello Studio",
        "label_en": "Portrait — Armando Rossi or the firm's team",
        "alt_it": "Avv. Armando Rossi, promotore della Latin America Mission",
        "alt_en": "Armando Rossi, promoter of the Latin America Mission",
    },
}


IT = {
    "lang": "it",
    "path": "/",
    "other_lang": "en",
    "other_path": "/en/",
    "dir_prefix": "",

    # ---- SEO ----
    "title": "Latin America Mission 2026 | Missione d'impresa in Ceará, Brasile",
    "meta_desc": "Missione imprenditoriale italiana in Ceará, Brasile, dal 16 al 23 novembre 2026: incontri B2B, visite al Porto di Pecém e Rinascimento Design District.",
    "og_title": "Latin America Mission 2026 — Ceará, Brasile | 16–23 novembre",
    "og_desc": "Una settimana di incontri B2B, visite industriali e relazioni istituzionali tra imprese italiane e il sistema produttivo del Ceará. Adesioni aperte.",
    "locale": "it_IT",

    # ---- nav ----
    "nav": [
        ("#missione", "La missione"),
        ("#ceara", "Perché il Ceará"),
        ("#settori", "Settori"),
        ("#rinascimento", "Rinascimento"),
        ("#programma", "Programma"),
        ("#faq", "FAQ"),
    ],
    "nav_extra": [("#adesioni", "Adesioni"), ("#contatti", "Contatti")],
    "nav_aria": "Navigazione principale",
    "nav_cta": "Aderisci",
    "menu_label": "Apri il menu",
    "skip": "Vai al contenuto principale",

    # ---- hero ----
    "hero_flag": "Italia · Brasile — Stato del Ceará",
    "hero_h1_a": "Latin America",
    "hero_h1_b": "Mission",
    "hero_place": "Ceará, Brasile",
    "hero_dates": "16 – 23 novembre 2026",
    "hero_sub": "Otto giorni per aprire una rotta industriale concreta tra l'Europa e l'America Latina: incontri B2B selezionati, visite al Porto di Pecém e alla FTZ, tavoli istituzionali con il Governo dello Stato del Ceará e la FIEC.",
    "hero_cta_1": "Invia la tua adesione",
    "hero_cta_2": "Scopri la missione",
    "hero_meta": [
        ("Formato", "B2B · Visite · Networking"),
        ("Promotore", "Studio Armando Rossi & Partners"),
        ("Adesioni", "Aperte fino a esaurimento posti"),
    ],
    "scroll": "Scorri",

    # ---- supporters ----
    "sup_promoted": "Promossa da",
    "sup_with": "con la partecipazione di Italink",
    "sup_support": "Con il supporto istituzionale di",
    "sup_text_cards": [("Sistema Italia", "Rete istituzionale")],

    # ---- mission ----
    "mission_eyebrow": "La missione",
    "mission_h2": "Un ponte industriale tra Europa e America Latina",
    "mission_p": [
        "Sono aperte le adesioni alla <strong>Latin America Mission</strong>, la missione imprenditoriale promossa dallo Studio Armando Rossi &amp; Partners con la partecipazione di <strong>Italink</strong> e il supporto istituzionale del Governo dello Stato del Ceará, della FIEC – Federazione delle Industrie dello Stato del Ceará, della Camera Italo-Brasiliana di Commercio e Industria e del Sistema Italia.",
        "L'obiettivo è aprire opportunità reali di <strong>internazionalizzazione, export e partnership industriali</strong>. Non una delegazione di rappresentanza: un programma di lavoro con incontri B2B costruiti sul profilo di ogni impresa partecipante, visite tecniche alle infrastrutture strategiche del territorio e tavoli diretti con le istituzioni che quelle infrastrutture le decidono.",
        "Un'attenzione particolare è dedicata alle filiere del <strong>design, arredamento, pietre naturali, superfici, materiali, interni e architettura</strong>, con la presentazione del Rinascimento Design District: il nuovo ecosistema che connette industria, materie prime, innovazione e logistica in un unico hub integrato.",
    ],
    "fact_h3": "In sintesi",
    "facts": [
        ("Destinazione", "Ceará, Brasile"),
        ("Date", "16–23 novembre 2026"),
        ("Promotore", "Studio Armando Rossi &amp; Partners"),
        ("Partecipazione", "Italink"),
        ("Formato", "B2B · Visite · Networking"),
    ],
    "fact_support_k": "Supporto istituzionale",
    "fact_support_v": "Governo dello Stato del Ceará · FIEC – Federazione delle Industrie dello Stato del Ceará · Camera Italo-Brasiliana di Commercio e Industria · Sistema Italia",
    "fact_open_k": "Adesioni",
    "fact_open_v": "Aperte",

    # ---- why ceará ----
    "why_eyebrow": "Perché il Ceará",
    "why_h2": "Uno Stato che tiene insieme tutta la catena del valore",
    "why_lede": "Materie prime, logistica portuale, energia rinnovabile, tecnologia e manifattura in un solo territorio. È questo che rende il Ceará una piattaforma di ingresso ai mercati dell'America Latina, e non semplicemente una destinazione.",
    "why_cells": [
        ("01", "Logistica e Porto di Pecém", "Hub logistico e portuale di livello internazionale, con la FTZ Ceará e un collegamento diretto verso Europa, Stati Uniti e Africa."),
        ("02", "Energia e transizione", "Polo di riferimento per l'idrogeno verde, l'eolico e il solare: energia rinnovabile competitiva, priorità dichiarata dello Stato."),
        ("03", "Materie prime e manifattura", "Pietre naturali, materiali e manifattura avanzata integrata: la base di filiere competitive già strutturate."),
        ("04", "Tecnologia e formazione", "Ricerca, sviluppo tecnologico e formazione professionale con IEL e SENAI Ceará a supporto degli insediamenti."),
    ],
    # Fonte: scheda "PECÉM 2031 — Hub globale di energia e tecnologia" fornita
    # dallo Studio (9/8/2026). NB: nel messaggio erano indicati 571 mld, la scheda
    # riporta R$ 585 bi — qui vale la scheda.
    "pecem_eyebrow": "Pecém 2031 — Hub globale di energia e tecnologia",
    "pecem_h3": "Leadership mondiale nella transizione energetica",
    "pecem_stats": [
        ("11 GW", "idrogeno verde"),
        ("R$ 585 mld", "investimenti"),
        ("42.000", "nuovi posti di lavoro"),
    ],
    "pecem_p": "Uno studio con la partecipazione di Harvard e del MIT proietta Pecém come riferimento mondiale per energia pulita e innovazione. L'allineamento tra politiche pubbliche e infrastruttura logistica sta attirando investimenti di giganti come TikTok e Casa dos Ventos.",
    "pecem_pillars_lbl": "I pilastri della trasformazione",
    "pecem_pillars": [
        ("Data center su larga scala", "Infrastruttura per l'economia digitale globale."),
        ("Industria ad alta tecnologia", "Attrazione di aziende ad alto consumo elettrico."),
        ("FTZ Ceará", "Incentivi fiscali e sicurezza giuridica per l'esportazione."),
    ],

    # ---- sectors ----
    "sect_eyebrow": "Settori della missione",
    "sect_h2": "Una missione ampia e multisettoriale",
    "sect_lede": "La missione resta aperta e trasversale: accanto al focus su design e materiali, il Ceará offre oggi opportunità concrete a logistica, energia, macchinari, tecnologia, agroalimentare e manifattura avanzata.",
    "sectors": [
        ("↗", "Energia e transizione energetica", "Generazione, rinnovabili e nuove filiere dell'energia pulita."),
        ("⚓", "Logistica e infrastrutture", "Porto di Pecém, FTZ e reti logistiche integrate."),
        ("⚙", "Macchinari e impiantistica", "Meccanica, automazione ed equipaggiamenti industriali."),
        ("❋", "Agroalimentare", "Filiere agroindustriali e trasformazione alimentare."),
        ("◈", "Tecnologie digitali", "Innovazione digitale e trasformazione tecnologica."),
    ],
    "sect_callout": "<strong>Focus speciale.</strong> Una corsia dedicata alle filiere del <strong>design, arredamento, pietre naturali, superfici, materiali, interni e architettura</strong>, presentate attraverso il Rinascimento Design District.",

    # ---- value / audience ----
    "val_eyebrow": "Perché partecipare",
    "val_h2": "Cosa porta a casa un'impresa che parte con noi",
    "val_lede": "Una missione ha senso solo se produce relazioni utilizzabili al ritorno. Il programma è costruito su questo principio.",
    "values": [
        ("1", "Un'agenda B2B costruita su misura", "Gli incontri vengono definiti a partire dal profilo dell'impresa, in raccordo con i sindacati industriali della FIEC: si parla con controparti pertinenti, non con una platea generica."),
        ("2", "Accesso diretto alle istituzioni", "Governo dello Stato, FIEC, Camera Italo-Brasiliana e Sistema Italia partecipano alla missione: interlocutori decisionali, nella stessa stanza."),
        ("3", "Visite tecniche", "Porto di Pecém, FTZ Ceará e infrastrutture industriali si visitano per valutare costi, tempi e fattibilità di un insediamento o di una fornitura."),
        ("4", "Una piattaforma già mappata", "Il Rinascimento Design District offre un percorso di ingresso già strutturato per chi valuta produzione, showroom o distribuzione in Brasile."),
    ],
    "aud_eyebrow": "A chi si rivolge",
    "aud_h3": "La missione è pensata per",
    "audience": [
        "Imprese manifatturiere che valutano una piattaforma produttiva competitiva fuori dall'Europa",
        "Aziende export-oriented che vogliono aprire i mercati dell'America Latina",
        "Produttori di pietre naturali, ceramica, superfici, arredo e serramenti",
        "Fornitori di macchinari, impiantistica e automazione industriale",
        "Studi di design, architettura e ingegneria con progetti internazionali",
        "Operatori dell'energia, della logistica e delle infrastrutture",
    ],

    # ---- rinascimento ----
    "rin_badge": "Progetto di punta",
    "rin_h2_a": "Rinascimento",
    "rin_h2_b": "Design District",
    "rin_p": [
        "Tra le opportunità presentate nel corso della missione, il Rinascimento Design District è un <strong>ecosistema industriale integrato</strong> del design, dei materiali, degli interni e della manifattura avanzata.",
        "Un unico distretto produttivo che connette imprese, fornitori, showroom, logistica, servizi, innovazione e internazionalizzazione: il punto di riferimento naturale per chi entra in Brasile con un progetto industriale, non solo commerciale.",
    ],
    "rin_cta": "Partecipa alla presentazione",
    "rin_visual_small": "Design · Materiali · Manifattura",
    "why_now_eyebrow": "Perché ora",
    "why_now_h3": "Una piattaforma complementare, non un trasloco",
    "why_now_p": "Per alcuni settori industriali energivori l'Europa è diventata più complessa e più costosa. Il Rinascimento offre alle imprese italiane una piattaforma complementare di espansione produttiva in Brasile, con energia rinnovabile competitiva, infrastrutture industriali pronte e accesso ai mercati delle Americhe.",
    "narrative": "La logica non è «delocalizzare dall'Italia», ma:",
    "narrative_list": [
        "Design, tecnologia e know-how italiani.",
        "Produzione competitiva e sostenibile in Brasile.",
        "Accesso diretto ai mercati latinoamericani e internazionali.",
    ],
    "narrative_note": "Un argomento commerciale particolarmente forte per ceramica, superfici, vetro, pietre naturali e per tutti i settori a forte consumo energetico.",
    "seg_eyebrow": "I segmenti di riferimento",
    "segments": [
        ("Arredamento e interior design", "Residenziale, contract, hospitality, uffici, retail, cucine, outdoor e falegnameria industriale."),
        ("Pietre naturali, ceramica e superfici", "Marmo, granito, quarzite, gres porcellanato, superfici sinterizzate e ultracompatte, rivestimenti e piani cucina."),
        ("Materiali per architettura e costruzioni", "Pannelli, laminati, pavimenti, facciate, sistemi costruttivi industrializzati e materiali avanzati e sostenibili."),
        ("Legno, vetro, alluminio e serramenti", "Pannelli e derivati del legno, porte, serramenti, vetro architettonico, facciate continue e sistemi di schermatura."),
        ("Illuminazione, automazione e smart building", "Illuminazione tecnica e decorativa, domotica, building automation e tecnologie per edifici intelligenti."),
        ("Interior, bagno e complementi", "Tessuti, tende, tappeti, carte da parati, imbottiti, rubinetteria, sanitari, docce e complementi d'arredo."),
        ("Design, architettura e innovazione", "Studi di design e architettura, interior e product design, prototipazione, modellazione digitale, biomateriali e nuove tecnologie."),
    ],
    "fair_lbl": "Prossimo appuntamento",
    "fair_ttl": "Fiera del Rinascimento — Fortaleza",
    "fair_p": "È in programma l'organizzazione di una Fiera del Rinascimento nei pressi di Fortaleza, dedicata alle filiere del design, dei materiali e della manifattura avanzata.",

    # ---- programme ----
    "prog_eyebrow": "Programma indicativo",
    "prog_h2": "Come sono organizzati gli otto giorni",
    "prog_lede": "Una settimana di incontri, visite e relazioni istituzionali costruita per produrre risultati verificabili al rientro.",
    "programme": [
        ("01", "Incontri B2B", "Con imprese, associazioni industriali e partner locali dei settori focus della missione, selezionati sul profilo di ciascun partecipante."),
        ("02", "Visite istituzionali e tecniche", "Al Porto di Pecém, alla FTZ Ceará e alle principali infrastrutture logistiche e industriali del territorio."),
        ("03", "Presentazione del Rinascimento", "Il Rinascimento Design District, il suo modello di sviluppo e le opportunità di collaborazione, internazionalizzazione e insediamento produttivo."),
        ("04", "Networking istituzionale", "Momenti di relazione tra imprenditori italiani, istituzioni brasiliane e stakeholder locali."),
    ],
    "prog_note": "Il programma definitivo, con orari e sedi, viene condiviso con le imprese confermate prima della partenza.",

    # ---- partners ----
    "part_eyebrow": "Partner locali",
    "part_h2": "Un ecosistema industriale già coinvolto",
    "part_lede": "In vista dell'Accordo di Cooperazione con il Governo del Ceará, la missione coinvolge i principali sindacati industriali della FIEC collegati ai settori focus, insieme agli enti per l'innovazione e la formazione.",
    "part_col1_h3": "Sindacati industriali FIEC",
    "part_col1_sub": "Federazione delle Industrie dello Stato del Ceará",
    "unions": [
        ("SindMóveis", "Mobile, cucine, arredamento contract e interior design."),
        ("SIMAGRAN", "Pietre naturali, marmi, graniti e quarziti."),
        ("SindCerâmica", "Ceramica, porcellanato, superfici, vetro e materiali per l'architettura."),
        ("Sinduscon-CE", "Costruzioni e sistemi costruttivi."),
        ("SindSerrarias", "Legno, pannelli, falegnameria industriale e prodotti derivati."),
        ("SIMEC", "Metallurgia, meccanica, alluminio, serramenti, automazione ed equipaggiamenti industriali."),
    ],
    "part_col2_h3": "Innovazione e formazione",
    "part_col2_sub": "Enti di ricerca, sviluppo e formazione professionale",
    "bodies": [
        ("IEL Ceará", "Innovazione, ricerca e sviluppo tecnologico."),
        ("SENAI Ceará", "Formazione professionale, laboratori e prototipazione."),
    ],
    "inst_eyebrow": "Supporto istituzionale",
    "inst_p": "Governo dello Stato del Ceará · FIEC · Camera Italo-Brasiliana di Commercio e Industria · Sistema Italia",

    # ---- faq ----
    "faq_eyebrow": "Domande frequenti",
    "faq_h2": "Tutto quello che serve sapere prima di aderire",
    "faq": [
        ("Chi può partecipare alla Latin America Mission?",
         "La missione è aperta a imprese, studi professionali e operatori economici italiani ed europei interessati a export, partnership industriali o insediamento produttivo in Brasile. Non è richiesta una dimensione aziendale minima: contano la pertinenza settoriale e la concretezza dell'obiettivo."),
        ("Quali sono le date e la durata?",
         "La missione si svolge dal 16 al 23 novembre 2026 nello Stato del Ceará, in Brasile, con base a Fortaleza. Il programma copre otto giorni tra incontri B2B, visite tecniche e appuntamenti istituzionali."),
        ("Quanto costa la partecipazione?",
         "I costi di partecipazione, comprensivi dei servizi organizzativi previsti, vengono comunicati insieme al programma dettagliato a seguito della manifestazione di interesse. Viaggio e soggiorno sono indicati separatamente nella proposta."),
        ("La missione è riservata al settore design e arredamento?",
         "No. Il design, l'arredamento e i materiali hanno una corsia dedicata attraverso il Rinascimento Design District, ma la missione è multisettoriale e include energia, logistica e infrastrutture, macchinari e impiantistica, tecnologie digitali, agroalimentare e manifattura avanzata."),
        ("Che tipo di incontri B2B sono previsti?",
         "Incontri con imprese, sindacati industriali della FIEC, partner locali e istituzioni, selezionati sul profilo di ciascuna azienda partecipante. Per questo l'agenda si costruisce nelle settimane precedenti alla partenza: aderire con anticipo aumenta la qualità degli abbinamenti."),
        ("Che ruolo hanno le istituzioni brasiliane?",
         "La missione si svolge con il supporto istituzionale del Governo dello Stato del Ceará, della FIEC, della Camera Italo-Brasiliana di Commercio e Industria e del Sistema Italia, in vista dell'Accordo di Cooperazione con il Governo del Ceará."),
        ("Cos'è il Rinascimento Design District?",
         "È un ecosistema industriale integrato dedicato a design, materiali, interni e manifattura avanzata: un distretto produttivo che collega imprese, fornitori, showroom, logistica, servizi e innovazione. Viene presentato nel corso della missione ed è aperto a progetti di collaborazione, internazionalizzazione e insediamento."),
        ("Come si aderisce e con quali tempi?",
         "Si compila il modulo di adesione in questa pagina. Il team dello Studio Armando Rossi &amp; Partners ricontatta l'impresa con programma dettagliato, costi e passi successivi. Le adesioni restano aperte fino a esaurimento dei posti disponibili."),
    ],

    # ---- form ----
    "form_eyebrow": "Adesioni aperte",
    "form_h2": "Partecipa alla Latin America Mission",
    "form_p": "Compila il modulo per manifestare il tuo interesse. Il team dello Studio Armando Rossi &amp; Partners ti ricontatta con il programma dettagliato, i costi di partecipazione e i prossimi passi. Nessun impegno in questa fase.",
    "form_perks": [
        "Agenda personalizzata di incontri B2B con imprese e partner locali",
        "Accesso alle visite istituzionali e tecniche (Porto di Pecém, FTZ Ceará)",
        "Presentazione del Rinascimento Design District",
        "Networking con istituzioni e stakeholder brasiliani",
    ],
    "form_h3": "Modulo di adesione",
    "form_sub": 'I campi contrassegnati con <span class="req">*</span> sono obbligatori.',
    "f_company": "Ragione sociale",
    "f_contact": "Referente",
    "f_role": "Ruolo",
    "f_email": "Email",
    "f_phone": "Telefono",
    "f_country": "Paese",
    "f_participants": "N° partecipanti",
    "f_sector": "Settore di attività",
    "f_sector_placeholder": "Seleziona un settore…",
    "f_sectors": [
        "Arredamento e interior design",
        "Pietre naturali, ceramica e superfici",
        "Materiali per architettura e costruzioni",
        "Legno, vetro, alluminio e serramenti",
        "Illuminazione, automazione e smart building",
        "Interior, bagno e complementi",
        "Design, architettura e innovazione",
        "Energia e transizione energetica",
        "Logistica e infrastrutture",
        "Macchinari e impiantistica",
        "Agroalimentare",
        "Tecnologie digitali e manifattura avanzata",
        "Altro",
    ],
    "f_interest": "Interesse principale",
    "f_interests": [
        "Incontri B2B", "Visite istituzionali e tecniche", "Rinascimento Design District",
        "Networking", "Insediamento produttivo", "Export",
    ],
    "f_message": "Note o messaggio",
    "f_message_ph": "Raccontaci in due righe cosa cerchi in Brasile: ci serve per costruire la tua agenda.",
    "f_privacy": 'Acconsento al trattamento dei dati personali ai sensi del Reg. UE 2016/679 (GDPR) per le finalità connesse alla partecipazione alla missione. <span class="req">*</span>',
    "f_submit": "Invia la tua adesione",
    "f_sending": "Invio in corso…",
    "f_error": "Invio non riuscito. Scrivici direttamente a {email}.",
    "f_note": "Oppure scrivici a",
    "f_success_h3": "Adesione ricevuta. Grazie.",
    "f_success_p": "Il team dello Studio Armando Rossi &amp; Partners ti ricontatta a breve con il programma dettagliato e i prossimi passi.",
    "f_mail_subject": "Adesione — Latin America Mission 2026",

    # ---- galleria ----
    "gal_eyebrow": "Il Ceará in immagini",
    "gal_h2": "Il territorio, le filiere, gli incontri",
    "gal_lede": "Le infrastrutture, le filiere industriali e i momenti di lavoro che compongono la missione.",

    # ---- promotore ----
    "prom_eyebrow": "Chi guida la missione",
    "prom_h2": "Studio Armando Rossi & Partners",
    "prom_role": "Promotore della Latin America Mission",
    "prom_p": [
        "Lo Studio Armando Rossi &amp; Partners promuove la Latin America Mission e cura i rapporti con le istituzioni brasiliane, la selezione delle controparti e l'assistenza alle imprese partecipanti prima, durante e dopo la missione.",
        "Per informazioni sul programma, sui costi e sui requisiti di partecipazione, la segreteria risponde direttamente ai contatti in fondo alla pagina.",
    ],
    "prom_cta": "Parla con la segreteria",

    # ---- micro-interazioni ----
    "countdown_label": "Alla partenza",
    "countdown_unit": "giorni",
    "countdown_today": "La missione è in corso",
    "ics_label": "Aggiungi al calendario",
    "sticky_cta": "Aderisci alla missione",
    "sticky_dates": "16–23 nov 2026 · posti limitati",
    "top_label": "Torna su",
    "close_label": "Chiudi",
    "zoom_label": "Ingrandisci l'immagine",

    # ---- contacts ----
    "ct_eyebrow": "Contatti",
    "ct_h2": "Informazioni e partecipazione",
    "ct_lede": "Per qualsiasi chiarimento sul programma, sui costi o sui requisiti di partecipazione, la segreteria della missione risponde direttamente.",
    "ct_email": "Email",
    "ct_phone": "Telefono",
    "ct_promoter": "Promotore",

    # ---- footer ----
    "foot_sub": "Ceará · Brasile — 16–23 novembre 2026",
    "foot_p": "Missione imprenditoriale per l'internazionalizzazione, l'export e le partnership industriali tra Europa e America Latina.",
    "foot_nav_h": "Navigazione",
    "foot_ct_h": "Contatti",
    "foot_copy": "© 2026 Studio Armando Rossi &amp; Partners",
    "foot_note": "Con il supporto del Governo dello Stato del Ceará, della FIEC, della Camera Italo-Brasiliana di Commercio e Industria e del Sistema Italia.",
    "lang_label": "Lingua",
}

EN = {
    "lang": "en",
    "path": "/en/",
    "other_lang": "it",
    "other_path": "/",
    "dir_prefix": "",

    "title": "Latin America Mission 2026 | Business mission to Ceará, Brazil",
    "meta_desc": "Italian business mission to Ceará, Brazil, 16–23 November 2026: B2B meetings, visits to the Port of Pecém and the Rinascimento Design District.",
    "og_title": "Latin America Mission 2026 — Ceará, Brazil | 16–23 November",
    "og_desc": "A week of B2B meetings, industrial visits and institutional relations between Italian companies and the productive system of Ceará. Applications open.",
    "locale": "en_GB",

    "nav": [
        ("#missione", "The mission"),
        ("#ceara", "Why Ceará"),
        ("#settori", "Sectors"),
        ("#rinascimento", "Rinascimento"),
        ("#programma", "Programme"),
        ("#faq", "FAQ"),
    ],
    "nav_extra": [("#adesioni", "Apply"), ("#contatti", "Contacts")],
    "nav_aria": "Main navigation",
    "nav_cta": "Apply",
    "menu_label": "Open menu",
    "skip": "Skip to main content",

    "hero_flag": "Italy · Brazil — State of Ceará",
    "hero_h1_a": "Latin America",
    "hero_h1_b": "Mission",
    "hero_place": "Ceará, Brazil",
    "hero_dates": "16 – 23 November 2026",
    "hero_sub": "Eight days to open a concrete industrial route between Europe and Latin America: selected B2B meetings, visits to the Port of Pecém and the FTZ, institutional roundtables with the Government of the State of Ceará and FIEC.",
    "hero_cta_1": "Submit your application",
    "hero_cta_2": "Discover the mission",
    "hero_meta": [
        ("Format", "B2B · Visits · Networking"),
        ("Promoter", "Studio Armando Rossi & Partners"),
        ("Applications", "Open while places last"),
    ],
    "scroll": "Scroll",

    "sup_promoted": "Promoted by",
    "sup_with": "with the participation of Italink",
    "sup_support": "With the institutional support of",
    "sup_text_cards": [("Sistema Italia", "Institutional network")],

    "mission_eyebrow": "The mission",
    "mission_h2": "An industrial bridge between Europe and Latin America",
    "mission_p": [
        "Applications are open for the <strong>Latin America Mission</strong>, the business mission promoted by Studio Armando Rossi &amp; Partners with the participation of <strong>Italink</strong> and the institutional support of the Government of the State of Ceará, FIEC – the Federation of Industries of the State of Ceará, the Italian-Brazilian Chamber of Commerce and Industry and Sistema Italia.",
        "The aim is to open real opportunities for <strong>internationalisation, export and industrial partnerships</strong>. This is not a ceremonial delegation: it is a working programme, with B2B meetings built around each participating company's profile, technical visits to the region's strategic infrastructure and direct roundtables with the institutions that decide on it.",
        "Particular attention is devoted to the supply chains of <strong>design, furniture, natural stone, surfaces, materials, interiors and architecture</strong>, with the presentation of the Rinascimento Design District: the new ecosystem connecting industry, raw materials, innovation and logistics in a single integrated hub.",
    ],
    "fact_h3": "At a glance",
    "facts": [
        ("Destination", "Ceará, Brazil"),
        ("Dates", "16–23 November 2026"),
        ("Promoter", "Studio Armando Rossi &amp; Partners"),
        ("Participation", "Italink"),
        ("Format", "B2B · Visits · Networking"),
    ],
    "fact_support_k": "Institutional support",
    "fact_support_v": "Government of the State of Ceará · FIEC – Federation of Industries of the State of Ceará · Italian-Brazilian Chamber of Commerce and Industry · Sistema Italia",
    "fact_open_k": "Applications",
    "fact_open_v": "Open",

    "why_eyebrow": "Why Ceará",
    "why_h2": "A state that holds the entire value chain together",
    "why_lede": "Raw materials, port logistics, renewable energy, technology and manufacturing in a single territory. That is what makes Ceará a gateway platform to the Latin American markets, rather than simply a destination.",
    "why_cells": [
        ("01", "Logistics and the Port of Pecém", "A world-class logistics and port hub, with the FTZ Ceará and direct connections to Europe, the United States and Africa."),
        ("02", "Energy and transition", "A reference hub for green hydrogen, wind and solar: competitive renewable energy, a declared priority of the state."),
        ("03", "Raw materials and manufacturing", "Natural stone, materials and integrated advanced manufacturing: the basis of already structured, competitive supply chains."),
        ("04", "Technology and training", "Research, technological development and vocational training, with IEL and SENAI Ceará supporting new industrial settlements."),
    ],
    "pecem_eyebrow": "Pecém 2031 — Global energy and technology hub",
    "pecem_h3": "World leadership in the energy transition",
    "pecem_stats": [
        ("11 GW", "green hydrogen"),
        ("R$ 585 bn", "investment"),
        ("42,000", "new jobs"),
    ],
    "pecem_p": "A study involving Harvard and MIT projects Pecém as a global reference for clean energy and innovation. The alignment between public policy and logistics infrastructure is attracting investment from majors such as TikTok and Casa dos Ventos.",
    "pecem_pillars_lbl": "The pillars of the transformation",
    "pecem_pillars": [
        ("Large-scale data centres", "Infrastructure for the global digital economy."),
        ("High-tech industry", "Attracting energy-intensive companies."),
        ("FTZ Ceará", "Tax incentives and legal certainty for exports."),
    ],

    "sect_eyebrow": "Mission sectors",
    "sect_h2": "A broad, multi-sector mission",
    "sect_lede": "The mission stays open and cross-sectoral: alongside the focus on design and materials, Ceará today offers concrete opportunities in logistics, energy, machinery, technology, agri-food and advanced manufacturing.",
    "sectors": [
        ("↗", "Energy and energy transition", "Generation, renewables and new clean-energy supply chains."),
        ("⚓", "Logistics and infrastructure", "Port of Pecém, FTZ and integrated logistics networks."),
        ("⚙", "Machinery and plant engineering", "Mechanics, automation and industrial equipment."),
        ("❋", "Agri-food", "Agro-industrial chains and food processing."),
        ("◈", "Digital technologies", "Digital innovation and technological transformation."),
    ],
    "sect_callout": "<strong>Special focus.</strong> A dedicated track for the supply chains of <strong>design, furniture, natural stone, surfaces, materials, interiors and architecture</strong>, presented through the Rinascimento Design District.",

    "val_eyebrow": "Why take part",
    "val_h2": "What a participating company takes home",
    "val_lede": "A mission is only worth it if it produces relationships you can actually use once you are back. The programme is built on that principle.",
    "values": [
        ("1", "A tailor-made B2B agenda", "Meetings are defined from your company profile, in coordination with FIEC's industrial unions: you talk to relevant counterparts, not to a generic audience."),
        ("2", "Direct access to institutions", "The State Government, FIEC, the Italian-Brazilian Chamber and Sistema Italia take part in the mission: decision-makers, in the same room."),
        ("3", "Technical visits", "The Port of Pecém, the FTZ Ceará and industrial infrastructure are visited to assess the cost, timing and feasibility of a settlement or supply agreement."),
        ("4", "A platform already mapped out", "The Rinascimento Design District offers a structured entry route for companies evaluating production, showrooms or distribution in Brazil."),
    ],
    "aud_eyebrow": "Who it is for",
    "aud_h3": "The mission is designed for",
    "audience": [
        "Manufacturers assessing a competitive production platform outside Europe",
        "Export-oriented companies looking to open Latin American markets",
        "Producers of natural stone, ceramics, surfaces, furniture and frames",
        "Suppliers of machinery, plant engineering and industrial automation",
        "Design, architecture and engineering studios with international projects",
        "Operators in energy, logistics and infrastructure",
    ],

    "rin_badge": "Flagship project",
    "rin_h2_a": "Rinascimento",
    "rin_h2_b": "Design District",
    "rin_p": [
        "Among the opportunities presented during the mission, the Rinascimento Design District is an <strong>integrated industrial ecosystem</strong> for design, materials, interiors and advanced manufacturing.",
        "A single productive district connecting companies, suppliers, showrooms, logistics, services, innovation and internationalisation: the natural reference point for those entering Brazil with an industrial project, not merely a commercial one.",
    ],
    "rin_cta": "Attend the presentation",
    "rin_visual_small": "Design · Materials · Manufacturing",
    "why_now_eyebrow": "Why now",
    "why_now_h3": "A complementary platform, not a relocation",
    "why_now_p": "For some energy-intensive industrial sectors, Europe has become more complex and more expensive. Rinascimento offers Italian companies a complementary platform for productive expansion in Brazil, with competitive renewable energy, ready industrial infrastructure and access to the markets of the Americas.",
    "narrative": "The logic is not “offshoring from Italy”, but:",
    "narrative_list": [
        "Italian design, technology and know-how.",
        "Competitive and sustainable production in Brazil.",
        "Direct access to Latin American and international markets.",
    ],
    "narrative_note": "A particularly strong commercial case for ceramics, surfaces, glass, natural stone and every energy-intensive sector.",
    "seg_eyebrow": "The reference segments",
    "segments": [
        ("Furniture and interior design", "Residential, contract, hospitality, office, retail, kitchens, outdoor and industrial joinery."),
        ("Natural stone, ceramics and surfaces", "Marble, granite, quartzite, porcelain stoneware, sintered and ultra-compact surfaces, claddings and countertops."),
        ("Materials for architecture and construction", "Panels, laminates, floors, façades, industrialised building systems and advanced, sustainable materials."),
        ("Wood, glass, aluminium and frames", "Wood panels and derivatives, doors, frames, architectural glass, curtain walls and shading systems."),
        ("Lighting, automation and smart building", "Technical and decorative lighting, home automation, building automation and smart-building technologies."),
        ("Interior, bathroom and accessories", "Fabrics, curtains, rugs, wallpapers, upholstery, taps, sanitaryware, showers and furnishing accessories."),
        ("Design, architecture and innovation", "Design and architecture studios, interior and product design, prototyping, digital modelling, biomaterials and new technologies."),
    ],
    "fair_lbl": "Coming up",
    "fair_ttl": "Rinascimento Fair — Fortaleza",
    "fair_p": "A Rinascimento Fair is being planned near Fortaleza, dedicated to the design, materials and advanced manufacturing supply chains.",

    "prog_eyebrow": "Indicative programme",
    "prog_h2": "How the eight days are organised",
    "prog_lede": "A week of meetings, visits and institutional relations designed to produce results you can verify on your return.",
    "programme": [
        ("01", "B2B meetings", "With companies, industrial associations and local partners in the mission's focus sectors, selected on each participant's profile."),
        ("02", "Institutional and technical visits", "To the Port of Pecém, the FTZ Ceará and the region's main logistics and industrial infrastructure."),
        ("03", "Rinascimento presentation", "The Rinascimento Design District, its development model and the opportunities for collaboration, internationalisation and productive settlement."),
        ("04", "Institutional networking", "Moments of relationship-building between Italian entrepreneurs, Brazilian institutions and local stakeholders."),
    ],
    "prog_note": "The final programme, with times and venues, is shared with confirmed companies before departure.",

    "part_eyebrow": "Local partners",
    "part_h2": "An industrial ecosystem already engaged",
    "part_lede": "Ahead of the Cooperation Agreement with the Government of Ceará, the mission engages FIEC's leading industrial unions linked to the focus sectors, together with the bodies for innovation and training.",
    "part_col1_h3": "FIEC industrial unions",
    "part_col1_sub": "Federation of Industries of the State of Ceará",
    "unions": [
        ("SindMóveis", "Furniture, kitchens, contract furnishing and interior design."),
        ("SIMAGRAN", "Natural stone, marble, granite and quartzite."),
        ("SindCerâmica", "Ceramics, porcelain, surfaces, glass and materials for architecture."),
        ("Sinduscon-CE", "Construction and building systems."),
        ("SindSerrarias", "Wood, panels, industrial joinery and derived products."),
        ("SIMEC", "Metallurgy, mechanics, aluminium, frames, automation and industrial equipment."),
    ],
    "part_col2_h3": "Innovation and training",
    "part_col2_sub": "Research, development and vocational training bodies",
    "bodies": [
        ("IEL Ceará", "Innovation, research and technological development."),
        ("SENAI Ceará", "Vocational training, laboratories and prototyping."),
    ],
    "inst_eyebrow": "Institutional support",
    "inst_p": "Government of the State of Ceará · FIEC · Italian-Brazilian Chamber of Commerce and Industry · Sistema Italia",

    "faq_eyebrow": "Frequently asked questions",
    "faq_h2": "Everything you need to know before applying",
    "faq": [
        ("Who can take part in the Latin America Mission?",
         "The mission is open to Italian and European companies, professional firms and economic operators interested in export, industrial partnerships or productive settlement in Brazil. There is no minimum company size: what counts is sector relevance and a concrete objective."),
        ("What are the dates and duration?",
         "The mission runs from 16 to 23 November 2026 in the State of Ceará, Brazil, based in Fortaleza. The programme covers eight days of B2B meetings, technical visits and institutional appointments."),
        ("How much does participation cost?",
         "Participation costs, including the organisational services provided, are communicated together with the detailed programme following your expression of interest. Travel and accommodation are indicated separately in the proposal."),
        ("Is the mission reserved for design and furniture?",
         "No. Design, furniture and materials have a dedicated track through the Rinascimento Design District, but the mission is multi-sector and includes energy, logistics and infrastructure, machinery and plant engineering, digital technologies, agri-food and advanced manufacturing."),
        ("What kind of B2B meetings are planned?",
         "Meetings with companies, FIEC industrial unions, local partners and institutions, selected on each participating company's profile. That is why the agenda is built in the weeks before departure: applying early improves the quality of the matches."),
        ("What role do the Brazilian institutions play?",
         "The mission takes place with the institutional support of the Government of the State of Ceará, FIEC, the Italian-Brazilian Chamber of Commerce and Industry and Sistema Italia, ahead of the Cooperation Agreement with the Government of Ceará."),
        ("What is the Rinascimento Design District?",
         "It is an integrated industrial ecosystem dedicated to design, materials, interiors and advanced manufacturing: a productive district connecting companies, suppliers, showrooms, logistics, services and innovation. It is presented during the mission and is open to collaboration, internationalisation and settlement projects."),
        ("How do I apply and by when?",
         "Fill in the application form on this page. The Studio Armando Rossi &amp; Partners team will contact you with the detailed programme, costs and next steps. Applications remain open while places last."),
    ],

    "form_eyebrow": "Applications open",
    "form_h2": "Join the Latin America Mission",
    "form_p": "Fill in the form to express your interest. The Studio Armando Rossi &amp; Partners team will get back to you with the detailed programme, participation costs and next steps. No commitment at this stage.",
    "form_perks": [
        "A tailored B2B meeting agenda with local companies and partners",
        "Access to institutional and technical visits (Port of Pecém, FTZ Ceará)",
        "Presentation of the Rinascimento Design District",
        "Networking with Brazilian institutions and stakeholders",
    ],
    "form_h3": "Application form",
    "form_sub": 'Fields marked with <span class="req">*</span> are required.',
    "f_company": "Company name",
    "f_contact": "Contact person",
    "f_role": "Role",
    "f_email": "Email",
    "f_phone": "Phone",
    "f_country": "Country",
    "f_participants": "No. of participants",
    "f_sector": "Business sector",
    "f_sector_placeholder": "Select a sector…",
    "f_sectors": [
        "Furniture and interior design",
        "Natural stone, ceramics and surfaces",
        "Materials for architecture and construction",
        "Wood, glass, aluminium and frames",
        "Lighting, automation and smart building",
        "Interior, bathroom and accessories",
        "Design, architecture and innovation",
        "Energy and energy transition",
        "Logistics and infrastructure",
        "Machinery and plant engineering",
        "Agri-food",
        "Digital technologies and advanced manufacturing",
        "Other",
    ],
    "f_interest": "Main interest",
    "f_interests": [
        "B2B meetings", "Institutional and technical visits", "Rinascimento Design District",
        "Networking", "Productive settlement", "Export",
    ],
    "f_message": "Notes or message",
    "f_message_ph": "Tell us in two lines what you are looking for in Brazil: we use it to build your agenda.",
    "f_privacy": 'I consent to the processing of my personal data pursuant to EU Reg. 2016/679 (GDPR) for purposes related to participation in the mission. <span class="req">*</span>',
    "f_submit": "Submit your application",
    "f_sending": "Sending…",
    "f_error": "Sending failed. Please write to us at {email}.",
    "f_note": "Or write to us at",
    "f_success_h3": "Application received. Thank you.",
    "f_success_p": "The Studio Armando Rossi &amp; Partners team will contact you shortly with the detailed programme and next steps.",
    "f_mail_subject": "Application — Latin America Mission 2026",

    # ---- gallery ----
    "gal_eyebrow": "Ceará in pictures",
    "gal_h2": "The territory, the supply chains, the meetings",
    "gal_lede": "The infrastructure, the industrial supply chains and the working moments that make up the mission.",

    # ---- promoter ----
    "prom_eyebrow": "Who leads the mission",
    "prom_h2": "Studio Armando Rossi & Partners",
    "prom_role": "Promoter of the Latin America Mission",
    "prom_p": [
        "Studio Armando Rossi &amp; Partners promotes the Latin America Mission and manages relations with the Brazilian institutions, the selection of counterparts and support to participating companies before, during and after the mission.",
        "For information on the programme, costs and participation requirements, the secretariat replies directly at the contacts at the bottom of this page.",
    ],
    "prom_cta": "Talk to the secretariat",

    # ---- micro-interactions ----
    "countdown_label": "To departure",
    "countdown_unit": "days",
    "countdown_today": "The mission is under way",
    "ics_label": "Add to calendar",
    "sticky_cta": "Apply to the mission",
    "sticky_dates": "16–23 Nov 2026 · limited places",
    "top_label": "Back to top",
    "close_label": "Close",
    "zoom_label": "Enlarge image",

    "ct_eyebrow": "Contacts",
    "ct_h2": "Information and participation",
    "ct_lede": "For any clarification on the programme, costs or participation requirements, the mission secretariat replies directly.",
    "ct_email": "Email",
    "ct_phone": "Phone",
    "ct_promoter": "Promoter",

    "foot_sub": "Ceará · Brazil — 16–23 November 2026",
    "foot_p": "Business mission for internationalisation, export and industrial partnerships between Europe and Latin America.",
    "foot_nav_h": "Navigation",
    "foot_ct_h": "Contacts",
    "foot_copy": "© 2026 Studio Armando Rossi &amp; Partners",
    "foot_note": "With the support of the Government of the State of Ceará, FIEC, the Italian-Brazilian Chamber of Commerce and Industry and Sistema Italia.",
    "lang_label": "Language",
}

from content_pt import PT, IMAGES_PT  # noqa: E402

for _slot, _extra in IMAGES_PT.items():
    IMAGES[_slot].update(_extra)

LANGS = [IT, EN, PT]
