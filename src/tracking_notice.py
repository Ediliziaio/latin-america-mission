"""Technical cookie/statistics notice; no change to participation form handling."""
from html import escape
from pathlib import Path

COPY = {
 'it': ('cookie-statistiche', 'Cookie e statistiche', 'Questa pagina descrive gli strumenti di misurazione del sito Latin America Mission.',
  [('Preferenze del browser', 'La scelta sui cookie facoltativi viene salvata nel browser. Serve a ricordare se hai accettato o rifiutato le statistiche.'),
   ('Google Analytics e Google Tag Manager', 'Se il servizio di misurazione è attivato, Google Analytics viene caricato tramite Google Tag Manager soltanto dopo il consenso alle statistiche. Il rifiuto permette di continuare a consultare il sito.'),
   ('Informazioni misurate', 'La misurazione riguarda le pagine pubbliche visitate e l’utilizzo del sito. I campi del modulo di adesione non vengono inviati agli strumenti di analisi da questa integrazione. I parametri di ricerca e i frammenti dell’indirizzo non vengono aggiunti ai dati di pagina della configurazione.'),
   ('Cambiare la scelta', 'Puoi riaprire “Preferenze cookie” dal pulsante presente sul sito e modificare il consenso. La revoca interrompe la misurazione, elimina i cookie analitici accessibili al sito e può ricaricare la pagina.'),
   ('Marketing', 'Questa integrazione non aggiunge pixel pubblicitari o strumenti di remarketing.')],
  'Informazioni sui dati trattati da Google', 'Richieste relative al sito', 'Torna al sito'),
 'en': ('cookies-statistics', 'Cookies and statistics', 'This page describes the measurement tools used by the Latin America Mission website.',
  [('Browser preferences', 'Your choice about optional cookies is saved in your browser. It is used to remember whether you accepted or refused statistics.'),
   ('Google Analytics and Google Tag Manager', 'When measurement is enabled, Google Analytics is loaded through Google Tag Manager only after you consent to statistics. You can continue browsing if you refuse.'),
   ('Information measured', 'Measurement concerns visits to public pages and use of the website. This integration does not send participation form fields to analytics tools. Search parameters and URL fragments are not included in the configured page information.'),
   ('Changing your choice', 'Use the “Cookie preferences” button on the website to change your consent. Withdrawal stops measurement, removes analytics cookies accessible to the website and may reload the page.'),
   ('Marketing', 'This integration does not add advertising pixels or remarketing tools.')],
  'How Google uses data', 'Website enquiries', 'Back to the website'),
 'pt': ('cookies-estatisticas', 'Cookies e estatísticas', 'Esta página descreve as ferramentas de medição do site Latin America Mission.',
  [('Preferências do navegador', 'A escolha sobre cookies opcionais é salva no navegador para lembrar se você aceitou ou recusou as estatísticas.'),
   ('Google Analytics e Google Tag Manager', 'Quando a medição está ativada, o Google Analytics é carregado pelo Google Tag Manager somente após o consentimento para estatísticas. Você pode continuar navegando se recusar.'),
   ('Informações medidas', 'A medição considera visitas às páginas públicas e o uso do site. Esta integração não envia os campos do formulário de participação às ferramentas de análise. Parâmetros de pesquisa e fragmentos do endereço não são incluídos nas informações de página configuradas.'),
   ('Alterar a escolha', 'Use o botão “Preferências de cookies” no site para alterar o consentimento. A retirada interrompe a medição, remove cookies analíticos acessíveis ao site e pode recarregar a página.'),
   ('Marketing', 'Esta integração não adiciona pixels publicitários ou ferramentas de remarketing.')],
  'Como o Google usa os dados', 'Contato sobre o site', 'Voltar ao site')
}

def write_notices(root, site):
    root = Path(root)
    for lang, values in COPY.items():
        slug, title, intro, sections, google_label, contact_label, back = values
        prefix = '' if lang == 'it' else lang + '/'
        folder = root / prefix / slug
        folder.mkdir(parents=True, exist_ok=True)
        body = ''.join('<h2>'+escape(h)+'</h2><p>'+escape(p)+'</p>' for h,p in sections)
        scripts = ''.join('<script defer src="/assets/js/'+name+'"></script>' for name in ['analytics-config.js','analytics-loader.js','analytics-consent.js'])
        page = '<!doctype html><html lang="'+lang+'"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="noindex,follow"><title>'+escape(title)+' — Latin America Mission</title>'+scripts+'<style>body{font:17px/1.65 system-ui,sans-serif;color:#10283a;background:#fafbfc;margin:0}main{max-width:780px;margin:48px auto;padding:24px}h1{line-height:1.15}h2{font-size:23px;margin-top:32px}a{color:#145d8a}button{font:inherit;padding:10px 15px;background:#fff;border:1px solid #10283a;border-radius:6px}</style></head><body><main><a href="/'+prefix+'">'+escape(back)+'</a><h1>'+escape(title)+'</h1><p>'+escape(intro)+'</p>'+body+'<p><button type="button" onclick="window.dispatchEvent(new Event(\'eic:open-cookie-preferences\'))">'+('Cookie preferences' if lang=='en' else 'Preferências de cookies' if lang=='pt' else 'Preferenze cookie')+'</button></p><p><a href="https://policies.google.com/technologies/partner-sites" target="_blank" rel="noopener noreferrer">'+escape(google_label)+'</a></p><h2>'+escape(contact_label)+'</h2><p>'+escape(site['promoter'])+' · <a href="mailto:'+escape(site['email'],quote=True)+'">'+escape(site['email'])+'</a></p></main></body></html>'
        (folder/'index.html').write_text(page, encoding='utf-8')
