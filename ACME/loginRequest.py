# Realiza login com request
from bs4 import BeautifulSoup
import requests

from ACME.downWorkItem import funDownWorkItem


def funLoginRequest(var_strUsuario, var_strSenha, var_strUrlAcme, var_strWorkItems, funIterarLista):

    try:
        with requests.Session() as session:
            print("Realizando login via Request")
            # Login com request
            acme = session.get(var_strUrlAcme)
            acme_html = BeautifulSoup(acme.content, 'html.parser')
            # print(acme_html)
            var_strToken = acme_html.find(
                'input', {'name': '_token'})['value']
            var_strLogin = {'email': var_strUsuario,
                            'password': var_strSenha, '_token': var_strToken}
            # print(var_strLogin)
            session.post(var_strUrlAcme, var_strLogin)
            print("Login realizado com sucesso.")

            # Chama Função para fazer o download do work item
            funDownWorkItem(session, var_strWorkItems, funIterarLista)
    except:
        print('Erro ao fazer login via request')
