from Entidades.Comando import Comando
from Entidades.Bot import Bot
from typing import List

class BotStreamer(Bot):
    def __init__(self,nome, comandos: List[Comando], id):
        super().__init__(nome, comandos, id)
        self.__nome = nome
        self.id = id

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self,nome):
        self.__nome = nome

    def apresentacao(self):
        return f'Salve, sou o {self.__nome}'

    def despedida(self):
        return f'---> {self.__nome} diz: Falou, vai ter live amanha em'