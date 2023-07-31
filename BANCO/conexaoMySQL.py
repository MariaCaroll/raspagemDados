import mysql.connector

print("Conectando com MYSql")
try:
    var_strConexao = mysql.connector.connect(host="localhost", user="root",
                                             passwd="Lima", db="db_workItem")
    var_strCursor = var_strConexao.cursor()
except:
    print("Serviço MySQL80 não inicializado")
