import os
import requests


def download(url, endereco):
    resposta = requests.get(url, verify=False)
    if resposta.status_code == requests.codes.OK:
        with open(endereco, 'wb') as novo_arquivo:
                novo_arquivo.write(resposta.content)
        print("Download finalizado. Arquivo salvo em: {}".format(endereco))
    else:
        resposta.raise_for_status()


def loopDownload(AnoIncio, AnoFim, OutputDir, url, NomeArquivo):
    for i in range(AnoIncio, AnoFim):
        if not os.path.isdir(OutputDir):
            os.makedirs(OutputDir)
        nome_arquivo = os.path.join(OutputDir, NomeArquivo.format(i))
        download(url.format(i), nome_arquivo)