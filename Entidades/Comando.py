import random

class Comando:
    # recebe o id (inteiro), a mensagem e as respostas (opcional)
    def __init__(self, id, msg, respostas = []):
        self.id = id
        self.__msg = msg
        self.__respostas = respostas

    # get id
    def id(self):
        return self.id

    @property
    def msg(self):
        return self.__msg

    def __str__(self):
        return f'{self.id} - {self.__msg}'

    # retorna uma resposta aleatória
    def getRandomResposta(self):
        return self.__respostas[random.randint(0,len(self.__respostas) - 1)]

    # adiciona resposta
    def addResposta(self, resposta):
        self.__respostas.append(resposta)
    
    # remove resposta (opcional)
    def delResposta(self, resposta):
        if resposta in self.__respostas:
            self.__respostas.remove(resposta)
        else:
            print("Resposta não existente nesse comando")