from datetime import date
from src.downloadDadosEXPIMP import loopDownload
from src.downloadEmpresas import loopDownloadEmpresas


# https://www.gov.br/produtividade-e-comercio-exterior/pt-br/assuntos/comercio-exterior/estatisticas/base-de-dados-bruta
# https://www.gov.br/produtividade-e-comercio-exterior/pt-br/assuntos/comercio-exterior/estatisticas/empresas-brasileiras-exportadoras-e-importadoras


# links onde os arquivos estão
BASE_URL_EXP = 'https://balanca.economia.gov.br/balanca/bd/comexstat-bd/ncm/EXP_{}.csv'    
BASE_URL_EXPMUN = 'https://balanca.economia.gov.br/balanca/bd/comexstat-bd/mun/EXP_{}_MUN.csv'
BASE_URL_IMP = 'https://balanca.economia.gov.br/balanca/bd/comexstat-bd/ncmv2/IMP_{}_V2.csv'
BASE_URL_IMPMUN = 'https://balanca.economia.gov.br/balanca/bd/comexstat-bd/mun/IMP_{}_MUN.csv'
BASE_URL_EMPRESAS = 'https://balanca.economia.gov.br/balanca/outras/EMPRESAS_CADASTRO_{}.xlsx'

# período para os downloads
anoIncio = 2021
anoFim = date.today().year +1 # retorna o corrente ano +1

# nome das planilhas nos arquivos excel das empresas
PlanilhaExp = 'EXP_CNPJ14'
PlanilhaImp = 'IMP_CNPJ14'


if __name__ == '__main__':
    print('---INICIANDO DOWNLOAD DOS ARQUIVOS---\n')

    print('1 - Arquivos de Exportação e Importação\n')

    loopDownload(anoIncio, anoFim, 'EXP-GERAL', BASE_URL_EXP, 'EXP_{}_GERAL.csv')
    loopDownload(anoIncio, anoFim, 'EXP-MUNICIPAL', BASE_URL_EXPMUN, 'EXP_{}_MUN.csv')
    loopDownload(anoIncio, anoFim, 'IMP-GERAL', BASE_URL_IMP, 'IMP_{}_GERAL.csv')
    loopDownload(anoIncio, anoFim, 'IMP-MUNICIPAL', BASE_URL_IMPMUN, 'IMP_{}_MUN.csv')

    print('2 - Arquivos de Empresas Exportadoras e Importadoras\n')

    loopDownloadEmpresas(anoIncio, anoFim, 'Empresas-EXP', PlanilhaExp, BASE_URL_EMPRESAS, 'EXP_{}_CNPJ.csv')
    loopDownloadEmpresas(anoIncio, anoFim, 'Empresas-IMP', PlanilhaImp, BASE_URL_EMPRESAS, 'IMP_{}_CNPJ.csv')

    print('MARAVILHA')
    print('\nTodos os arquivos foram baixados com sucesso!\n')