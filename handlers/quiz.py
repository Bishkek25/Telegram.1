from distutils.dist import command_re


from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton
from aiohttp.web_routedef import options

from config import bot

async def quiz_1(message: types.Message):
    keyboard = InlineKeyboardMarkup(resize_keyboard=True)
    button = InlineKeyboardButton('Далее', callback_data='quiz_2')
    keyboard.add(button)
    question = "where are you from?"
    options=['Bishkek','Moscow','Tokio','Tashkent']

    await bot.send_poll(
        chat_id=message.from_user.id,
        question=question,
        options=options,
        is_anonymous=False,
        type='quiz',
        correct_option_id=0,
        explanation='local',
        open_period=60,
        reply_markup=keyboard
    )


async def quiz2(call:types.CallbackQuery):
    keyboard = InlineKeyboardMarkup(resize_keybooard=True)
    button = InlineKeyboardButton('следуюшее', callback_data='quiz_2')
    keyboard.add(button)
    question = "выбери страну"
    options = ['kyrgyzstan', 'Russia', 'Usbekistan', 'China', 'Japan', 'USA']

    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=options,
        is_anonymous=True,
        type='quiz',
        correct_option_id=0,
        explanation='Эмигрант',
        open_period=60,
        reply_markup=keyboard
    )



async def quiz3(call:types.CallbackQuery):
    keyboard = InlineKeyboardMarkup(resize_keybooard=True)
    button = InlineKeyboardButton('следуюшее', callback_data='quiz_3')
    keyboard.add(button)
    question = "национальноые блюда"
    options = ['Besh barmak', 'Manty', 'Plow', 'Oromo', 'Boorsok']

    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=options,
        is_anonymous=True,
        type='quiz',
        correct_option_id=0,
        explanation='Паренные,Жаренные,Варенн',
        open_period=60,
        reply_markup=keyboard
    )

def register_handler_quiz(dp: Dispatcher):
        dp.register_message_handler(quiz_1, commands=['quiz'])
        dp.register_callback_query_handler(quiz2, text=['quiz-2'])
        dp.register_callback_query_handler(quiz3, text=['quiz-3'])




