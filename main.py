from config import bot, dp, Admins
from aiogram import executor, types
import logging
from handlers import commands, quiz, game, fsm_reg, echo, fsm_store, send_products, send_and_delete_products

from db import db_main



async def on_startup(_):
    await db_main.sql_create()

async def on_shutdown(_):
    for admins in Admins:
        await bot.send_message(chat_id=admins, text='бот выключен!')


commands.register_commands(dp)
quiz.register_handler_quiz(dp)
game.register_game(dp)
fsm_reg.reg_handler_fsm_registration(dp)
fsm_store.reg_handler_fsm_store(dp)
send_products.register_handlers(dp)
send_and_delete_products.register_handlers(dp)

echo.register_echo(dp)
if __name__ == '__main__':
     logging.basicConfig(level=logging.INFO)

     executor.start_polling(dp, skip_updates=True, on_startup=on_startup, on_shutdown=on_shutdown, allowed_updates=['callback_query'])


