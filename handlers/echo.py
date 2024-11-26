
from aiogram import types, Dispatcher


async def echo_handler(message: types.Message):
    if message.text.isnumeric():
        await message.answer(int(message.text)**2)
        return
    await message.answer(message.text)

def register_echo(dp: Dispatcher):
    dp.register_message_handler(echo_handler)

