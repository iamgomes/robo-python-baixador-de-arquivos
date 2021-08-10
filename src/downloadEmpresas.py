import os
import pandas as pd

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