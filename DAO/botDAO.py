from DAO import DAO
from Bot import Bot

class BotDAO(DAO):
    def add(self, bot: Bot):
        if (bot is not None) and (isinstance(bot.codigo, int)) and (isinstance(bot, Bot)):
            super().add(bot.codigo, bot)

    def get(self, comando: int):
        if isinstance(comando, int):
            return super().get(comando)

    def remove(self, comando: int):
        if isinstance(comando, int):
            return super().remove(comando)