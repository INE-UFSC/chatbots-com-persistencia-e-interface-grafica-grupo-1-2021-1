##implemente as seguintes classes

from abc import ABC, abstractmethod
import random as r
from Entidades.Comando import Comando

class Bot(ABC):
    @abstractmethod
    def __init__(self, nome, comandos: Comando, id):
        self.nome = nome
        self.comandos = comandos
        self.id = id

    @abstractmethod
    def nome(self):
        pass

    @abstractmethod
    def nome(nome):
        pass

    def mostra_comandos(self):
        print()
        for comandos in self.comandos:
            print(comandos)

    def executa_comando(self,id):
        respondeu = False
        for comando in self.comandos:
            if comando.id == id:
                print(f'--> {self.nome} diz: {comando.getRandomResposta()}')
                respondeu = True
                break
        if not respondeu:
            raise KeyError
    
    @abstractmethod
    def despedida():
        pass