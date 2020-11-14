# Autor: Bruno Hiis
# Eesmärk: Mugav tarkvara veebilehe SEO analüüsi saamiseks.
#
# Programmist: 
# * Programm küsib kasutajalt millist veebilehte skännida.
# * Programm saadab mitmeid päringuid antud veebilehele.
# * Programm uurib kas veebileht vastab parimatele SEO nõuetele.
# * Programm esitab kasutajale analüüsi tulemused nii failis kui ka ekraanil.
# 
# Uuritavad SEO nõuded:
# * Sitemap.xml'i olemasolu.
# * Robots.txt'i olemasolu.
# * HTTPS'i olemasolu.
# * Meta kirjelduse olemasolu ja täpsem analüüs.
# * H1 märgiste olemasolu ja täpsem analüüs.
# * ALT tekstide olemasolu ja täpsem analüüs.
# * Title märgiste olemasolu ja täpsem analüüs.

import urllib.request
import modules.html_checkers as check
from modules.check_website import check_website
from modules.check_https import check_https
from modules.print_output import print_output
from modules.write_output import write_output
from bs4 import BeautifulSoup
from datetime import datetime

# Märgistame kasutatava USER_AGENT'i, mida saadame päringutel kaasa.
USER_AGENT = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'

def main():
    # Küsime kasutajalt veebilehe URL'i, mida ta soovib analüüsida.
    website_url = input("Palun sisestage veebilehe URL järgnevas formaadis: (https://domain.tld): ")

    # Esialgsed analüüsid uurivad järgnevaid andmeid veebilehel: Sitemap.xml, HTTPS ja Robots.txt.
    has_sitemap = check_website(website_url + "/sitemap.xml", USER_AGENT)
    has_https = check_https(website_url)
    has_robots = check_website(website_url + "/robots.txt", USER_AGENT)

    # Et saaksime täpsemaid nõudeid analüüsida laeme alla veebilehe HTML'i ning kasutame edasi BeautifulSoup HTML parserit sisu lugemiseks. 
    request = urllib.request.Request(
        website_url, None, {'User-Agent': USER_AGENT, })
    response = urllib.request.urlopen(request)
    html = BeautifulSoup(response.read(), "html.parser")

    # Kasutame eelnevas etapis saadud veebilehe HTML'i, et uurida järgnevaid andmeid veebilehel: Meta kirjeldust, H1 märgiseid, Alt tekste ja Title märgiseid.
    meta_data = check.meta_tags(html)
    h1_data = check.multiple_h1(html)
    alt_texts_data = check.alt_texts(html)
    titles_data = check.check_titles(html)

    # Koostame analüüsi kasutajale näitamiseks.
    outputLines = [
        '\n--------------- OUTPUT ----------------\n',
        f'[{"+" if has_sitemap else "-"}] Sitemap.xml\n'
        f'[{"+" if has_robots else "-"}] Robots.txt\n',
        f'[{"+" if has_https else "-"}] HTTPS\n',
        '\n-------------- META DATA --------------\n',
        f'[{"+" if meta_data["description"] == "Good size meta description." else "-"}] {meta_data["description"]}\n',
        f'[{"+" if meta_data["keywords"] == "Good amount of meta keywords." else "-"}] {meta_data["keywords"]}\n',
        '\n------------- OTHER ISSUES ------------\n',
        f'[{"+" if h1_data == "Has one H1 element." else "-"}] {h1_data}\n',
        f'[{"+" if alt_texts_data == "All images have alt texts." else "-"}] {alt_texts_data}\n',
        f'[{"+" if titles_data == "Perfect title length." else "-"}] {titles_data}'
    ]
    
    # Prindime ekraanile analüüsi.
    print_output(outputLines)
    
    # Salvestame analüüsi ka faili, "output" kausta.
    write_output(website_url, datetime.now().strftime("%Y_%m_%d-%I_%M_%S_%p"), outputLines)
    
if __name__ == "__main__":
    main()
