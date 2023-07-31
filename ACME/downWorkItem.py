# Faz o download do workItem
from bs4 import BeautifulSoup
import pandas as pd
import re


# Função para iterar a lista de work itens e adicionar no banco
def funDownWorkItem(session, var_strWorkItems, funIterarLista):
    var_intPage = 1
    var_strUrl = session.get(var_strWorkItems)
    var_strUrlHtml = BeautifulSoup(var_strUrl.content, 'html.parser')
    var_listWokItem = []

    # página next
    var_srtNextHref = var_strUrlHtml.select_one('[rel=''next'']')['href']
    # print(var_srtNextHref)
    try:
        while var_srtNextHref != 'ultima':
            if var_intPage == 1:
                # pega a primeria página do work itens
                # salva a tabela na variavel lista
                print('primeira página')
                var_dttabela = var_strUrlHtml.find(class_='table')
                var_strTabela = str(var_dttabela)
                var_listWokItem = pd.read_html(var_strTabela)[
                    0].values.tolist()
                # Chama função para iterar a lista work Itens
                #print(var_strUrl)
                funIterarLista(var_listWokItem)

            # Demais páginas
            #print(var_strWorkItems)
            var_intPage = var_intPage + 1
            var_strUrl = var_strWorkItems + '?page=' + str(var_intPage)
            var_strUrl = session.get(var_strUrl)
            #print(var_strUrl)
            var_strUrlHtml = BeautifulSoup(var_strUrl.content, 'html.parser')
            var_dttabela = var_strUrlHtml.find(class_='table')
            var_strTabela = str(var_dttabela)
            var_listWokItem = pd.read_html(var_strTabela, header=None)[
                0].values.tolist()
                      
            # Chama função para iterar a lista work Itens
            funIterarLista(var_listWokItem)

            #verificar ultima página
            var_strRegex = re.compile(r'rel\W+next')
            var_strResultado = var_strRegex.findall(str(var_strUrlHtml.find(class_='page-numbers')))
            if len(var_strResultado) == 0:
                var_srtNextHref = 'ultima'
          
        print("Fim do download do work item")
    except:
        print('Erro ao extrair dados do SITE')
