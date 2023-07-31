# Responsavel por enviar e-mail de finalização

# For e-mail
from botcity.plugins.email import BotEmailPlugin
from configuracao import var_strDestinatario


def funEnviarEmail(email):
    print("Criando corpo do e-mail.")
    # Definindo os atributos que comporão a mensagem
    para = [var_strDestinatario]
    assunto = "Robô finalizado"
    corpo_email = "<h1>Olá, tudo bem?</h1> O robô de download de WorkItems foi finalizado com sucesso."

    # Enviando a mensagem de e -mail
    try:
        email.send_message(assunto, corpo_email, para,
                           attachments=False, use_html=True)
        print("E-mail enviado com sucesso!")
    except:
        print(f"Erro ao enviar e-mail para {var_strDestinatario}")

    # Feche a conexão com os servidores IMAP e SMTP
    email.disconnect()


def funConectatEmail(usuario, senha):

    # Instantiate the plugin
    var_strEmail = BotEmailPlugin()

    # Configure SMTP with the gmail server
    var_strEmail.configure_smtp("smtp.gmail.com", 587)
    print(var_strEmail)

    # Login with a valid email account
    var_strEmail.login(usuario, senha)

    print("Enviando e-mail de finalização...")
    funEnviarEmail(var_strEmail)
