import requests
from bs4 import BeautifulSoup

URL_BASE = "https://dadosabertos.ans.gov.br/FTP/PDA/demonstracoes_contabeis"
PATH_DOWNLOADS = 'IntuitiveCare/banco_dados_ans/arquivos/demonstrativos/'

def downloadArquivos(fileName , url):
    """
    Faz o download dos anexos e grava

    :param fileName: nome do arquvi anexo que será gravado
    :param url: endereço do arquivo na web
    """
    
    file = requests.get(url)
    with open(PATH_DOWNLOADS+fileName, 'wb') as f:
        f.write(file.content) 

page = requests.get(URL_BASE).text
soup = BeautifulSoup(page, 'html.parser')

anos = [URL_BASE + '/' + node.get('href') for node in soup.find_all('a') if node.get('href').startswith('20')]

for ano in anos:
    ano_page = requests.get(ano).text
    ano_soup = BeautifulSoup(ano_page, 'html.parser')

    arquivos = [ano + '/' + node.get('href') for node in ano_soup.find_all('a') if node.get('href').endswith('.zip')]

    for arquivo in arquivos:
        fileName = arquivo.split('/')[-1]
        downloadArquivos(fileName, arquivo)