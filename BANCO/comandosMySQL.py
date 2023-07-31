# funções para manipular dados no banco
from BANCO.conexaoMySQL import var_strCursor, var_strConexao


def funSelecionarDados(var_strWiid):
    result = 0
    try:
        var_strComando = f'SELECT wiid_workItem FROM tb_workitem WHERE wiid_workItem LIKE "{var_strWiid}"'
        var_strCursor.execute(var_strComando)
        retorno = var_strCursor.fetchall()
        result = len(retorno)
        return result
        # print(result)
    except:
        print('Erro ao selecionar dados')


def funAddBanco(var_strWiid, var_strDescription, var_strType, var_strStatus, var_strDate):
    try:
        var_strComando = f'INSERT INTO tb_workitem (wiid_workItem, description_workItem, type_workItem,status_workItem,date_workItem) VALUES ("{var_strWiid}", "{var_strDescription}","{var_strType}","{var_strStatus}","{var_strDate}")'
        var_strCursor.execute(var_strComando)
        var_strConexao.commit()
        print(f'Adicionando {var_strWiid} no banco')
    except:
        print(f'Erro ao adicionar dados no banco. WIID: {var_strWiid}')
