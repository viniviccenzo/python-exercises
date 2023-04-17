import requests
from bs4 import BeautifulSoup

url = 'https://www.nytimes.com/'
response = requests.get(url)

if response.status_code == 200:
    html = response.content

    soup = BeautifulSoup(html, 'html.parser')

    titulos = soup.find_all('h2')

    nome_arquivo = 'hard-coded.txt'

    with open(nome_arquivo, 'w') as arquivo:
        arquivo.write("Títulos de artigos do New York Times:\n")
        for titulo in titulos:
            arquivo.write(titulo.text.strip() + '\n')

    print("Os títulos foram escritos no arquivo", nome_arquivo)
else:
    print("Falha na requisição. Código de status:", response.status_code)
