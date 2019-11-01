#Llibreries instal.lades:
    #pip3  install python-whois
    #pip3 install requests
    #pip3 install beautifulsoup4

#ROBOTS.txt: http://esfarmacia.es/robots.txt
#sitemap: http://esfarmacia.es/sitemap.xml

#Importem la classe Farm que em construït
from farmacias import Farm
import csv
import time

#creem un objecte de la classe Farm
farmacies = Farm()

#Url a scrapejar
url='http://esfarmacia.es/'

#Obtenim els enllaços de les pàgines de farmacies per Provincia
ListProvincies=[]
ListProvincies=farmacies.obtenirlinksProvincies(url)

#Obtenim el llistat d'enllaços de totes les farmacies d'una provincia
ListFarmaLinks = []
for linkProvincia in ListProvincies:
    print(linkProvincia)
    for i in range(1,120):
        print(linkProvincia + '/'+ str(i))
        aux1 = farmacies.obtenirlinksFarmacies(linkProvincia + '/'+str(i))
        ListFarmaLinks= ListFarmaLinks + aux1
        print(aux1)

#Preparem capçalera del fitxer
farmaList=[]
headerList=["Farmacia","Titular","Dirección","Municipio","Provincia","Comunidad","Teléfono"]
farmaList.append(headerList)

#Obtenim dades d'una farmacia
for linkFarma in ListFarmaLinks:
    aux2 = farmacies.obtenirFarmacia(url + linkFarma)
    farmaList.append(aux2)
    print(aux2)

#guardem les dades en un fitxer CSV per importar a una eina de visualització
filePath="./csv/farmaDataset.csv"
farmacies.guardarFarmaciesCSV(filePath, farmaList)
