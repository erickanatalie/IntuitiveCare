import requests
import os
import zipfile

PATH_DOWNLOADS = "IntuitiveCare/WEBSCRAPING/downloads/"

def downloadAnexos(fileName , url):
    """
    Faz o download dos anexos e grava

    :param fileName: nome do arquvi anexo que será gravado
    :param url: endereço do arquivo na web
    """
    
    file = requests.get(url)
    with open(PATH_DOWNLOADS+fileName, 'wb') as f:
        f.write(file.content) 

def compactar_diretorio(pasta_origem, arquivo_saida):
 
    """
    Compacta todos os arquivos dentro de uma pasta em um arquivo ZIP.

    :param pasta_origem: Caminho da pasta que será compactada
    :param arquivo_saida: Nome do arquivo ZIP de saída (ex: "saida.zip")
    """

    with zipfile.ZipFile(arquivo_saida, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for raiz, _, arquivos in os.walk(pasta_origem):
            for arquivo in arquivos:
                caminho_completo = os.path.join(raiz, arquivo)
                caminho_no_zip = os.path.relpath(caminho_completo, pasta_origem)
                zipf.write(caminho_completo, caminho_no_zip)
    
    print(f"✔ Arquivo ZIP criado: {arquivo_saida}")

if __name__=="__main__":
    anexos = ["anexo1.pdf", "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos/Anexo_I_Rol_2021RN_465.2021_RN627L.2024.pdf",
              "anexo2.pdf", "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos/Anexo_II_DUT_2021_RN_465.2021_RN628.2025_RN629.2025.pdf"]
    
    downloadAnexos(anexos[0], anexos[1])
    downloadAnexos(anexos[2], anexos[3])
    
    compactar_diretorio(PATH_DOWNLOADS, "anexos.zip")