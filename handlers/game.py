from distutils.dist import command_re


from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton
from aiohttp.web_routedef import options

from config import bot

import random


games = ['⚽', '🎰', '🏀', '🎯', '🎳', '🎲']

async def game(m: types.Message):
    game = random.choice(games)
    await bot.send_dice(emoji=game,chat_id=m.from_user.id)


def register_game(dp: Dispatcher):
    dp.register_message_handler(game, commands=['game'])