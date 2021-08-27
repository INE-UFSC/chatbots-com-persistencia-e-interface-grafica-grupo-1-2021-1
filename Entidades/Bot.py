import random as r
from Entidades.Comando import Comando

class Bot():
    def __init__(self, nome, comandos: Comando, id):
        self.__nome = nome
        self.comandos = comandos
        self.id = id

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    def mostra_comandos(self):
        print()
        for comandos in self.comandos:
            print(comandos)

    def executa_comando(self,id):
        for comando in self.comandos:
            if comando.id == id:
                return (f'--> {self.nome} diz: {comando.getRandomResposta()}')
    
    def apresentacao(self, mensagem):
        return f'Meu nome é {self.__nome}. {mensagem}'

    def despedida(self, mensagem):
        return f'--> {self.__nome} {mensagem}'