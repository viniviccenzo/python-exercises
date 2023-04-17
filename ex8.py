import requests
from bs4 import BeautifulSoup

url = 'https://www.nytimes.com/'
response = requests.get(url)

if response.status_code == 200:
    html = response.content

    soup = BeautifulSoup(html, 'html.parser')

    titulos = soup.find_all('h2')

    print("Títulos de artigos do New York Times:")
    for titulo in titulos:
        print(titulo.text.strip())
else:
    print("Falha na requisição. Código de status:", response.status_code)
