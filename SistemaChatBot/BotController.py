from Interface.BotView import BotView
from Interface.ImportView import ImportView
from Entidades.Bot import Bot
from DAO.BotDAO import BotDAO
from Entidades.Comando import Comando
import PySimpleGUI as sg 

class BotController:
    def __init__(self):
        self.__telaBot = BotView()
        self.__telaImport = ImportView()
        self.__botDAO = BotDAO()

        sg.theme('Reddit')

    def inicia(self):
        self.__telaBot.tela_consulta()
        
        # Loop de eventos
        rodando = True
        import_active = False
        while rodando:
            if import_active:
                import_active = self.handle_import()
            else:
                event, values = self.__telaBot.le_eventos()

                if event == sg.WIN_CLOSED:
                    self.__telaBot.fim()
                    break
                else:
                    if event == 'Importar':
                        import_active = True

    def handle_import(self):
        self.__telaImport.tela_consulta()
        event_exp, values_exp = self.__telaImport.le_eventos()

        import_active = True

        if event_exp == sg.WIN_CLOSED:
            self.__telaImport.fim()
            import_active = False
        elif event_exp == 'importar':
                path = values_exp['caminho_import']
                self.__botDAO.import_source(path)
                self.__telaImport.fim()
                import_active = False
        self.instanciando_bot()
        return import_active

    def instanciando_bot(self):
        comandos = []
        for comando in self.__botDAO.objectCache["comandos"]:
            comandos.append(Comando(comando["id"], comando["msg"], comando["respostas"]))
        self.bot = Bot(self.__botDAO.objectCache["nome"], comandos, self.__botDAO.objectCache["id"])
        self.update_tela()

    def update_tela(self):
        self.__telaBot.update_tela(self.bot)
        