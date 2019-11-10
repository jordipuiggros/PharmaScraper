#Pip3 install Selenium
import csv
import zipfile
import os
from farmacias import Farm
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

url='http://esfarmacia.es/'
Ciutat='Igualada'
#creem un objecte de la classe Farm
farmacies = Farm()

#busquem per la ciutat que volem:
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(url)
time.sleep(5) # Let the user actually see something!
search_box = driver.find_element_by_name('texto')
search_box.send_keys(Ciutat)
search_box.submit()
time.sleep(5) # Let the user actually see something!
ListFarmaLinks = farmacies.obtenirlinksFarmacies(driver.current_url)

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
filePath="./csv/farmaDatasetIgualada.csv"
farmacies.guardarFarmaciesCSV(filePath, farmaList)

driver.quit()



