import os
from urllib.request import urlretrieve

# https://www.gov.br/produtividade-e-comercio-exterior/pt-br/assuntos/comercio-exterior/estatisticas/base-de-dados-bruta

def download(url, endereco):
    print('Baixando arquivo em: {}'.format(endereco))
    urlretrieve(url, endereco)
    print('Donwload finalizado!')

if __name__ == '__main__':
    BASE_URL_EXP = 'https://balanca.economia.gov.br/balanca/bd/comexstat-bd/ncm/EXP_{}.csv'    
    BASE_URL_EXPMUN = 'https://balanca.economia.gov.br/balanca/bd/comexstat-bd/mun/EXP_{}_MUN.csv'
    BASE_URL_IMP = 'https://balanca.economia.gov.br/balanca/bd/comexstat-bd/ncmv2/IMP_{}_V2.csv'
    BASE_URL_IMPMUN = 'https://balanca.economia.gov.br/balanca/bd/comexstat-bd/mun/IMP_{}_MUN.csv'

    AnoIncio = 2014
    AnoFim = 2022


    for i in range(AnoIncio, AnoFim):
        OUTPUT_DIR = 'EXP-GERAL'
        if not os.path.isdir(OUTPUT_DIR):
            os.makedirs(OUTPUT_DIR)

        nome_arquivo = os.path.join(OUTPUT_DIR,'EXP_{}_GERAL.csv'.format(i))
        download(BASE_URL_EXP.format(i), nome_arquivo)

    for i in range(AnoIncio, AnoFim):
        OUTPUT_DIR = 'EXP-MUNICIPAL'
        if not os.path.isdir(OUTPUT_DIR):
            os.makedirs(OUTPUT_DIR)

        nome_arquivo = os.path.join(OUTPUT_DIR,'EXP_{}_MUN.csv'.format(i))
        download(BASE_URL_EXPMUN.format(i), nome_arquivo)

    for i in range(AnoIncio, AnoFim):
        OUTPUT_DIR = 'IMP-GERAL'
        if not os.path.isdir(OUTPUT_DIR):
            os.makedirs(OUTPUT_DIR)

        nome_arquivo = os.path.join(OUTPUT_DIR,'IMP_{}_GERAL.csv'.format(i))
        download(BASE_URL_IMP.format(i), nome_arquivo)

    for i in range(AnoIncio, AnoFim):
        OUTPUT_DIR = 'IMP-MUNICIPAL'
        if not os.path.isdir(OUTPUT_DIR):
            os.makedirs(OUTPUT_DIR)

        nome_arquivo =  os.path.join(OUTPUT_DIR,'IMP_{}_MUN.csv'.format(i))
        download(BASE_URL_IMPMUN.format(i), nome_arquivo)

    print('\nMARAVILHA')
    print('\nTodos os arquivos foram baixados com sucesso!')