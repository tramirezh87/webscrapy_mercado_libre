from bs4 import BeautifulSoup
from datetime import datetime
import requests 

# pip install beautifulsoup4

url="https://listado.mercadolibre.com.pe/camionetas#D[A:camionetas]"


print("[INFO] {0}: Inicio del proceso".format(datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
page = requests.get(url)
soup = BeautifulSoup(page.content,'html.parser')

lista_autos=[] 
for x in soup.find_all(class_='ui-search-item__title ui-search-item__group__element'):
    anuncio={}
    anuncio['titulo']=x.get_text()
    lista_autos.append(anuncio)

print(lista_autos)

print("[INFO] {0}: Fin del proceso".format(datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
