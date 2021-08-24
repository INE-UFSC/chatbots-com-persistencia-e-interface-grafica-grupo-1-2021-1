#encoding: utf-8
from SistemaChatBot import SistemaChatBot as scb
from Entidades.BotOtaku import BotOtaku
from Entidades.BotStreamer import BotStreamer
from Entidades.BotZangado import BotZangado
from Entidades.Comando import Comando

###construa a lista de bots disponíveis aqui
lista_comando_zangado = [Comando(1, 'Boas vindas', ['Não', 'Sai']),
                Comando(2, 'Xingamento', ['Seu bobo', 'Seu chato', 'Seu sem graça'])]

lista_comando_otaku = [Comando(1, 'Boas vindas', ['Só vou aceitar boas vindas se você gosta de algum anime', 'Youkoso!']),
                        Comando(2, 'Recomendações', ['School Days', 'Death Note', 'Demon Slayer', 'Attack on titan', 'One punch man'])]

lista_comando_streamer = [Comando(1, 'Boas vindas', ['Opaaa, fala delee', 'Como voce vai?', 'Tudo certo?']),
                          Comando(2, 'Horario live', ['Live amanha, hoje to cansado', 'Tá em live mula', 'Hoje é rerun']),
                          Comando(3, 'Prime', ['Escorrega o prime marreco', 'Passem as coroas']),
                          Comando(4, 'Agradecimento Sub', ['GOD GOD, VALEU, TAMO JUNTO', 'Obrigado'])
]

lista_bots = [BotZangado("Yoda", lista_comando_zangado, 1), BotStreamer("Redy", lista_comando_streamer, 2), BotOtaku('Sasuke XD', lista_comando_otaku, 3)]

sys = scb.SistemaChatBot("CrazyBots",lista_bots)
sys.inicio()
