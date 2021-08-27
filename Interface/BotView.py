import PySimpleGUI as sg
from DAO.BotDAO import BotDAO
from Entidades.Bot import Bot

class BotView():
    def __init__(self):
        self.__container = []
        self.__window = sg.Window("ChatBot", self.__container, font=("Helvetica", 14), size=(450,300))
        self.__botDAO = BotDAO()

    def tela_consulta(self):
        self.__container = [
            [sg.Text('Escolha com qual bot você deseja conversar'), sg.Button('Importar')],     
        ]
        self.__window = sg.Window('Chat bot', self.__container ,font=('Helvetica', 14))

    def le_eventos(self):
        return self.__window.read()

    def fim(self):
        self.__window.close()
    
    def update_tela(self, bot):
        self.fim()
        botoes = []
        container_botoes = []
        a = 0
        for comando in bot.comandos:
            botao = sg.Button(comando.msg, key=comando.id)
            botoes.append(botao)
            if a == 2:
                container_botoes.append(botoes)
                botoes = []
                a = 0
            a += 1
        container_botoes.append(botoes)
        self.__container = [ [sg.Text(f'Você está falando com {bot.nome}')],
                             [sg.Text('Trocar bot'), sg.Button('Importar')],
                             container_botoes,
                             [sg.Text('',key='resposta', size=(0,1))] ]
        self.__window = sg.Window(bot.nome, self.__container ,font=('Helvetica', 14), size=(700,300))

    def update_resposta(self, resposta):
        self.__window.Element('resposta').set_size((len(resposta),1))
        self.__window.Element('resposta').Update(resposta)