from Entidades.Comando import Comando
from Entidades.Bot import Bot
from typing import List

class BotOtaku(Bot):
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
        return f'Meu nome é {self.__nome}. Não fala mal dos meus animes!'

    def despedida(self):
        return f'--> {self.nome} diz: Até mais. Vai lá assistir animes.'