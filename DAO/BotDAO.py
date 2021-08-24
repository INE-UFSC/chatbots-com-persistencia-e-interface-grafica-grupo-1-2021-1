from DAO.DAO import DAO
from Entidades.Bot import Bot

class BotDAO(DAO):
    def __init__(self):
        super().__init__()

    def add(self, bot: Bot):
        if (bot is not None) and (isinstance(bot.codigo, int)) and (isinstance(bot, Bot)):
            super().add(bot.codigo, bot)

    def get(self, comando: int):
        if isinstance(comando, int):
            return super().get(comando)

    def remove(self, comando: int):
        if isinstance(comando, int):
            return super().remove(comando)