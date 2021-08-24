from typing import List
from Entidades.Bot import Bot

class SistemaChatBot:
    def __init__(self,nomeEmpresa,lista_bots: List[Bot]):
        self.__empresa=nomeEmpresa
        self.__lista_bots=[]
        for bot in lista_bots:
            if isinstance(bot, Bot):
                self.__lista_bots.append(bot)
        self.__bot = None
    
    def boas_vindas(self):
        print(f'Olá, esse é o sistema chat bot da empresa {self.__empresa}\n')

    def mostra_menu(self):
        print("Os chat bots disponiveis no momento são:")

        for bot in self.__lista_bots:
            print(f'Id: {bot.id} - Bot: {bot.nome} - Mensagem de apresentação: {bot.apresentacao()}')
        print()
    
    def escolhe_bot(self):
        id = input("Digite o id do chat bot desejado: ")

        try:
            id = self.__parse_int(id)
        except ValueError:
            print("Id deve ser um inteiro!")
            self.escolhe_bot()

        for bot in self.__lista_bots:
            if bot.id == id:
                self.__bot = bot
        
        while self.__bot == None:
            print("Bot não encontrado")
            self.escolhe_bot()

    def mostra_comandos_bot(self):
        self.__bot.mostra_comandos()

    def le_envia_comando(self):
        comando = input("Digite o comando desejado (ou -1 para sair): ")
        print()

        try:
            comando = self.__parse_int(comando)
        except ValueError as e:
            print("Comando deve ser um inteiro!")
            terminar = self.le_envia_comando()
            return terminar

        if comando == -1:
            print(self.__bot.despedida())
            return False
        try:
            self.__bot.executa_comando(comando)
        except KeyError:
            print('Comando não existente\n')
            terminar = self.le_envia_comando()
            return terminar
        return 

    def inicio(self):
        self.boas_vindas()
        self.mostra_menu()
        self.escolhe_bot()
        while True:
            self.mostra_comandos_bot()
            print()
            retorno = self.le_envia_comando()
            if retorno == False:
                break
    
    def __parse_int(self, valor):
        try:
            return int(valor)
        except ValueError as e:
            print(f'Erro ao parsear inteiro')
            raise e
