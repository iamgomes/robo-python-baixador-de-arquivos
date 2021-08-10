import os
from datetime import date
from urllib.request import urlretrieve
import pandas as pd

# https://www.gov.br/produtividade-e-comercio-exterior/pt-br/assuntos/comercio-exterior/estatisticas/base-de-dados-bruta
#https://www.gov.br/produtividade-e-comercio-exterior/pt-br/assuntos/comercio-exterior/estatisticas/empresas-brasileiras-exportadoras-e-importadoras

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


def transformaArquivo(url, nome_planilha, ano, endereco):
    print('Lendo url e planilha {} - {}'.format(nome_planilha, ano))
    df = pd.read_excel(url, nome_planilha, header=7)

    print('Inserindo coluna ano {}'.format(ano))
    # criando coluna ano e atribuindo o ano do arquivo
    df['ANO'] = ano
    #setando a coluna cnpj como index
    df.set_index('CNPJ', inplace=True) 
    try:
        # exluindo linha com o valor 99999997999999
        df = df.drop(99999997999999) 
    except:
        print('Nenhuma linha indesejada encontrada')
    else:
        print('Exluindo linhas indesejadas')
    print('Baixando arquivos em: {}'.format(endereco))
    # gerando o csv com o pandas
    df.to_csv(endereco, sep=';', encoding='utf16 ')
    print('Donwload finalizado!\n')


def loopDownloadEmpresas(AnoIncio, AnoFim, OutputDir, nome_planilha, url, NomeArquivo):
    for i in range(AnoIncio, AnoFim):
        if not os.path.isdir(OutputDir):
            os.makedirs(OutputDir)
        nome_arquivo = os.path.join(OutputDir, NomeArquivo.format(i))
        transformaArquivo(url.format(i), nome_planilha, i, nome_arquivo)


# links onde os arquivos estão
BASE_URL_EXP = 'https://balanca.economia.gov.br/balanca/bd/comexstat-bd/ncm/EXP_{}.csv'    
BASE_URL_EXPMUN = 'https://balanca.economia.gov.br/balanca/bd/comexstat-bd/mun/EXP_{}_MUN.csv'
BASE_URL_IMP = 'https://balanca.economia.gov.br/balanca/bd/comexstat-bd/ncmv2/IMP_{}_V2.csv'
BASE_URL_IMPMUN = 'https://balanca.economia.gov.br/balanca/bd/comexstat-bd/mun/IMP_{}_MUN.csv'
BASE_URL_EMPRESAS = 'https://balanca.economia.gov.br/balanca/outras/EMPRESAS_CADASTRO_{}.xlsx'

# período para os downloads
anoIncio = 1997
anoFim = date.today().year +1 # retorna o corrente ano +1

# nome das planilhas nos arquivos excel das empresas
PlanilhaExp = 'EXP_CNPJ14'
PlanilhaImp = 'IMP_CNPJ14'


if __name__ == '__main__':
    print('---INICIANDO DOWNLOAD DOS ARQUIVOS---\n')

    loopDownload(anoIncio, anoFim, 'EXP-GERAL', BASE_URL_EXP, 'EXP_{}_GERAL.csv')
    loopDownload(anoIncio, anoFim, 'EXP-MUNICIPAL', BASE_URL_EXP, 'EXP_{}_MUN.csv')
    loopDownload(anoIncio, anoFim, 'IMP-GERAL', BASE_URL_EXP, 'IMP_{}_GERAL.csv')
    loopDownload(anoIncio, anoFim, 'IMP-MUNICIPAL', BASE_URL_EXP, 'IMP_{}_MUN.csv')
    loopDownloadEmpresas(anoIncio, anoFim, 'Empresas-EXP', PlanilhaExp, BASE_URL_EMPRESAS, 'EXP_{}_CNPJ.csv')
    loopDownloadEmpresas(anoIncio, anoFim, 'Empresas-IMP', PlanilhaImp, BASE_URL_EMPRESAS, 'IMP_{}_CNPJ.csv')

    print('\nMARAVILHA')
    print('\nTodos os arquivos foram baixados com sucesso!\n')