import os
from urllib.request import urlretrieve


def download(url, endereco):
    print('Baixando arquivos em: {}'.format(endereco))
    urlretrieve(url, endereco)
    print('Donwload finalizado!\n')


def loopDownload(AnoIncio, AnoFim, OutputDir, url, NomeArquivo):
    for i in range(AnoIncio, AnoFim):
        if not os.path.isdir(OutputDir):
            os.makedirs(OutputDir)
        nome_arquivo = os.path.join(OutputDir, NomeArquivo.format(i))
        download(url.format(i), nome_arquivo)