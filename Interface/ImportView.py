import PySimpleGUI as sg

class ImportView:
    def __init__(self):
        self.__container = []

    def tela_consulta(self):
        self.__container = [[sg.In(key="caminho_import"), sg.FileBrowse(file_types=(("JSON files", "*.json"),))],
                            [sg.Button("importar")]]

        self.__window = sg.Window('Importação de bots', self.__container, font=('Helvetica',14))

    def le_eventos(self):
        return self.__window.read()

    def fim(self):
        self.__window.close()