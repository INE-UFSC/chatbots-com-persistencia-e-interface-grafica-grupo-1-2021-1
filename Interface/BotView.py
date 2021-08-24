import PySimpleGUI as sg
from botDAO import BotDAO
from Bot import Bot

class BotView():
    def __init__(self):
        self.__container = []
        self.__window = sg.Window("ChatBot", self.__container, fon=("Helvetica", 14))
        self.__botDAO = BotDAO

    def tela_bot(self):
        self.__container = [
                            [sg.Text('Escolha com qual bot você deseja conversar')],
                            
        ]


    def listar(self):
        bots = [str(i) for i in self.__botDAO.get_all()]
        return '\n'.join(bots)

    def le_eventos(self):
        return self.__window.read()

    def fim(self):
        self.__window.close()