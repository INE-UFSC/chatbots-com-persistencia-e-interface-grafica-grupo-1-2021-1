import PySimpleGUI as sg
from DAO.BotDAO import BotDAO
from Entidades.Bot import Bot

class BotView():
    def __init__(self):
        self.__container = []
        self.__window = sg.Window("ChatBot", self.__container, font=("Helvetica", 14))
        self.__botDAO = BotDAO()

    def tela_consulta(self):
        self.__container = [
            [sg.Text('Escolha com qual bot você deseja conversar'), sg.Button('Importar')],     
        ]
        self.__window = sg.Window('Chat bot', self.__container ,font=('Helvetica', 14))

    def listar(self):
        bots = [str(i) for i in self.__botDAO.get_all()]
        return '\n'.join(bots)

    def le_eventos(self):
        return self.__window.read()

    def fim(self):
        self.__window.close()
    
    def update_tela(self, bot):
        botoes = []
        for comando in bot.comandos:
            botao = sg.Button(comando.msg, key=comando.id)
            botoes.append(botao)
        self.__container = [botoes]
        self.__window = sg.Window('Chat bot', self.__container ,font=('Helvetica', 14))