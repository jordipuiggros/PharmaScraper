import csv
import requests
from bs4 import BeautifulSoup

class Farm():

    def __init__(self):
        self.ListFarmacia = []

    #Obtenim els enllaços provincials de les farmacies
    def obtenirlinksProvincies(self, url):
        page = requests.get(url)
        html = BeautifulSoup(page.content, features="html.parser")
        ListProvincies=[]
        index = 0
        for link in html.find_all('a'):
            element=link.get('href')
            if element.find("farmacias")==1: #Només volem capturar alguns dels enllaços
                ListProvincies.append(url+element)
            index = index + 1
        return ListProvincies

    #A partir d'un enllaç provincial obtenim els enllaços a la fitxa de la farmacia. Retornem una llista d'enllaços
    def obtenirlinksFarmacies(self,url):
            page = requests.get(url)
            html = BeautifulSoup(page.text, "html.parser")
            ListLinksFarma=[]
            for element in html.find_all('a'):
                if element.text.find("+info")!=-1:
                    if element['href'].find('html')!=-1:
                        ListLinksFarma.append(element['href'])
            return ListLinksFarma

    #Obtenim els camps d'una farmacia a partir d'una url de pàgina donada
    def obtenirFarmacia(self,url):
        page = requests.get(url)
        html = BeautifulSoup(page.content, features="html.parser")
        Farmacia=""
        Titular=""
        Direccio=""
        Municipi=""
        Provincia=""
        Comunitat=""
        Telefon=""
        for strong in html.find_all('strong'):
            li=strong.find_previous()
            if li.text.find("Farmacia:")==0:
                Farmacia = li.text.replace("Farmacia: ","")
            if li.text.find("Titular:")==0:
                Titular = li.text.replace("Titular: ","")
            if li.text.find("Dirección:")==0:
                Direccio = li.text.replace("Dirección: ","")
            if li.text.find("Municipio:")==0:
                Municipi = li.text.replace("Municipio: ","")
            if li.text.find("Provincia:")==0:
                Provincia = li.text.replace("Provincia: ","")
            if li.text.find("Comunidad:")==0:
                Comunitat = li.text.replace("Comunidad: ","")
            if li.text.find("Teléfono:")==0:
                Telefon = li.text.replace("Teléfono: ","")
        return Farmacia, Titular, Direccio, Municipi, Provincia, Comunitat, Telefon

    #Guardem les farmacies a un fitxer CSV
    def guardarFarmaciesCSV(self, filePath, farmaList):
        with open(filePath, 'w', newline='') as csvFile:
            writer = csv.writer(csvFile)
            for farmaElement in farmaList:
                #print(farmaElement)
                writer.writerow(farmaElement)
