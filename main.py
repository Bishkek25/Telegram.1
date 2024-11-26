from config import bot, dp, Admins
from aiogram import executor, types
import logging
from handlers import commands,quiz,game,fsm_reg, echo
from handlers.commands import register_commands



async def on_startup(_):
      for admins in Admins:
       await bot.send_message(chat_id=admins,text='бот включон!')

async def on_shutdown(_):
    for admins in Admins:
        await bot.send_message(chat_id=admins, text='бот выключен!')


commands.register_commands(dp)
quiz.register_handler_quiz(dp)
game.register_game(dp)
fsm_reg.reg_handler_fsm_registration(dp)

echo.register_echo(dp)

if __name__ == '__main__':
     logging.basicConfig(level=logging.INFO)
     executor.start_polling(dp, skip_updates=True, on_startup=on_startup, on_shutdown=on_shutdown, allowed_updates=['callback'])


