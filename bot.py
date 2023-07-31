"""
WARNING:

Please make sure you install the bot with `pip install -e .` in order to get all the dependencies
on your Python environment.

Also, if you are using PyCharm or another IDE, make sure that you use the SAME Python interpreter
as your IDE.

If you get an error like:
```
ModuleNotFoundError: No module named 'botcity'
```

This means that you are likely using a different Python interpreter than the one used to install the bot.
To fix this, you can either:
- Use the same interpreter as your IDE and install your bot with `pip install --upgrade -r requirements.txt`
- Use the same interpreter as the one used to install the bot (`pip install --upgrade -r requirements.txt`)

Please refer to the documentation for more information at https://documentation.botcity.dev/
"""


# Import for the Web Bot
from botcity.web import WebBot, Browser, By

# Import for integration with BotCity Maestro SDK
from botcity.maestro import *

# For Chrome
#from botcity.web.browsers.chrome import default_options

from configuracao import var_strUsuario as usuario, var_strSenhaAcme as senha, var_strSenhaGmail, var_strUrlAcme, drive_item, var_strWorkItems
from BANCO.comandosMySQL import funAddBanco, funSelecionarDados
from ACME.loginRequest import funLoginRequest
from EMAIL.sendEmail import funConectatEmail


# Disable errors if we are not connected to Maestro
BotMaestroSDK.RAISE_NOT_CONNECTED = False


def main():
    # Runner passes the server url, the id of the task being executed,
    # the access token and the parameters that this task receives (when applicable).
    maestro = BotMaestroSDK.from_sys_args()
    # Fetch the BotExecution with details from the task, including parameters
    execution = maestro.get_execution()

    print(f"Task ID is: {execution.task_id}")
    print(f"Task Parameters are: {execution.parameters}")

    bot = WebBot()

    # Configure whether or not to run on headless mode
    bot.headless = False

    bot.browser = Browser.CHROME

    # Uncomment to set the WebDriver path
    bot.driver_path = drive_item

    # Implement here your logic...
    # Página Acme System
    funLoginRequest(usuario, senha, var_strUrlAcme,
                    var_strWorkItems, funIterarLista)

    # E-amil de finalização
    funConectatEmail(usuario, var_strSenhaGmail)

    # Wait 3 seconds before closing
    # bot.wait(3000)

    # Finish and clean up the Web Browser
    # You MUST invoke the stop_browser to avoid
    # leaving instances of the webdriver open
    # bot.stop_browser()

    # Uncomment to mark this task as finished on BotMaestro
    # maestro.finish_task(
    #     task_id=execution.task_id,
    #     status=AutomationTaskFinishStatus.SUCCESS,
    #     message="Task Finished OK."
    # )

# Função para iterar a lista de work itens e adicionar no banco


def funIterarLista(lista):
    for item in lista:
        result = funSelecionarDados(str(item[1]))
        if result == 0:
            funAddBanco(str(item[1]), str(item[2]), str(
                item[3]), str(item[4]), str(item[5]))
        else:
            print(f'O Wiid: {str(item[1])}, já existe no banco')


def not_found(label):
    print(f"Element not found: {label}")


if __name__ == '__main__':
    main()
