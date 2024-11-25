from config import bot, dp
from aiogram import executor, types
import logging
from handlers import commands,quiz,game,fsm_reg



commands.register_commands(dp)
quiz.register_handler_quiz(dp)
game.register_game(dp)
fsm_reg.reg_handler_fsm_registration(dp)


if __name__ == '__main__':
     logging.basicConfig(level=logging.INFO)
     executor.start_polling(dp, skip_updates=True)


