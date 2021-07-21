from urllib.request import urlretrieve

def download(url, nome_arquivo):
    print('Baixando arquivo {}'.format(nome_arquivo))
    urlretrieve(url, nome_arquivo)
    print('Donwload finalizado!')

if __name__ == '__main__':
    BASE_URL_EXP = 'https://balanca.economia.gov.br/balanca/bd/comexstat-bd/ncm/EXP_{}.csv'    
    BASE_URL_EXPMUN = 'https://balanca.economia.gov.br/balanca/bd/comexstat-bd/mun/EXP_{}_MUN.csv'
    BASE_URL_IMP = 'https://balanca.economia.gov.br/balanca/bd/comexstat-bd/ncmv2/IMP_{}_V2.csv'
    BASE_URL_IMPMUN = 'https://balanca.economia.gov.br/balanca/bd/comexstat-bd/mun/IMP_{}_MUN.csv'

    AnoIncio = 2015
    AnoFim = 2022

    for i in range(AnoIncio, AnoFim):
        novo_nome_arquivo = 'EXP_{}_GERAL.csv'.format(i)
        download(BASE_URL_EXP.format(i), novo_nome_arquivo)

    for i in range(AnoIncio, AnoFim):
        novo_nome_arquivo = 'EXP_{}_MUN.csv'.format(i)
        download(BASE_URL_EXPMUN.format(i), novo_nome_arquivo)

    for i in range(AnoIncio, AnoFim):
        novo_nome_arquivo = 'IMP_{}_GERAL.csv'.format(i)
        download(BASE_URL_IMP.format(i), novo_nome_arquivo)

    for i in range(AnoIncio, AnoFim):
        novo_nome_arquivo = 'IMP_{}_MUN.csv'.format(i)
        download(BASE_URL_IMPMUN.format(i), novo_nome_arquivo)
