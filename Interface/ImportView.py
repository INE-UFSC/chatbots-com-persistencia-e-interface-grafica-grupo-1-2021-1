import PySimpleGUI as sg

class ImportView:
    def __init__(self):
        self.__container = []
        self.__largura_resposta = 40
        self.__window = sg.Window('Importação bots', self.__container, font=('Helvetica', 14))

    def tela_cosulta(self):
        self.__container = [[sg.In(key="caminho_import"), sg.FileBrowse(file_types=(("*.json"),))],
                            [sg.Button("importar")]]

        self.__window = sg.Window('Exportação de bots', self.__container, font=('Helvetica',14))

    def le_eventos(self):
        return self.__window.read()

    def fim(self):
        self.__window.close()