# PharmaScraper
Scraper que descarrega totes les direccions i telèfons de farmacies del Estat i que estiguin continguts en el següent lloc web: http://esfarmacia.es/

Pel correcte funcionament d'aquest scraper s'empraran dos fitxers de codi:

El primer main.py hi haurà el fil principal d'execució del codi. Des d'aquí crearem un objecte de la classe Farmacia i utilitzarem els mètodes que aquest objecte té definits a la seva classe.

El segon fitxer, farmacias.py conté la classe farmacia amb tots els seus mètodes i propietats.

Per executar l'script caldrà crear una carpeta en el directori d'execució amb el següent nom: ./csv/
També caldrà instal.lar les següents llibreries:

    pip3  install python-whois
    pip3 install requests
    pip3 install beautifulsoup4
