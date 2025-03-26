import requests
from pathlib import Path

def downloadAnexos(url):
    file = requests.get(url)
    path = Path("./downloads/anexo1.pdf")
    with open(path.name, 'wb') as f:
        f.write(file.content) 

if __name__=="__main__":
    down = downloadAnexos("https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos/Anexo_I_Rol_2021RN_465.2021_RN627L.2024.pdf")
    print(down)