import os
from datetime import date
from urllib.request import urlretrieve

# https://www.gov.br/produtividade-e-comercio-exterior/pt-br/assuntos/comercio-exterior/estatisticas/base-de-dados-bruta

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


# links onde os arquivos estão
BASE_URL_EXP = 'https://balanca.economia.gov.br/balanca/bd/comexstat-bd/ncm/EXP_{}.csv'    
BASE_URL_EXPMUN = 'https://balanca.economia.gov.br/balanca/bd/comexstat-bd/mun/EXP_{}_MUN.csv'
BASE_URL_IMP = 'https://balanca.economia.gov.br/balanca/bd/comexstat-bd/ncmv2/IMP_{}_V2.csv'
BASE_URL_IMPMUN = 'https://balanca.economia.gov.br/balanca/bd/comexstat-bd/mun/IMP_{}_MUN.csv'


# período para os downloads
AnoIncio = 2021
AnoFim = date.today().year +1 # retorna o corrente ano +1


if __name__ == '__main__':
    print('---INICIANDO DOWNLOAD DOS ARQUIVOS---\n')

    loopDownload(AnoIncio, AnoFim, 'EXP-GERAL', BASE_URL_EXP, 'EXP_{}_GERAL.csv')
    loopDownload(AnoIncio, AnoFim, 'EXP-MUNICIPAL', BASE_URL_EXP, 'EXP_{}_MUN.csv')
    loopDownload(AnoIncio, AnoFim, 'IMP-GERAL', BASE_URL_EXP, 'IMP_{}_GERAL.csv')
    loopDownload(AnoIncio, AnoFim, 'IMP-MUNICIPAL', BASE_URL_EXP, 'IMP_{}_MUN.csv')

    print('\nMARAVILHA')
    print('\nTodos os arquivos foram baixados com sucesso!\n')