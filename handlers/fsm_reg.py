from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from config import bot
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton
from aiogram.dispatcher.filters.state import State, StatesGroup

class fsm_store(StatesGroup):
        name = State()
        size = State()
        category = State()
        price = State()
        photo = State()

async def start_fsm(message: types.Message):
    await message.answer('Введите название товара')
    await fsm_store.name.set()

async def process_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    size_keyboard = ReplyKeyboardMarkup().add(
        KeyboardButton(text="S"),
        KeyboardButton(text="M"),
        KeyboardButton(text="L"),
        KeyboardButton(text="XL"),
        KeyboardButton(text="3XL")
    )
    await fsm_store.next()
    await message.answer('Введи свой размер: ',reply_markup=size_keyboard)


async def process_size(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['size'] = message.text
    kb = types.ReplyKeyboardRemove()
    await fsm_store.next()
    await message.answer('category:',reply_markup=kb)


async def load_category(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['category'] = message.text

    await fsm_store.next()
    await message.answer('Отправь цену:')

async def load_price (message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['price'] = message.text

    await fsm_store.next()
    await message.answer('Отправь фото:')

async def load_photo(message: types.Message, state: FSMContext):

    async with state.proxy() as data:
        data['photo'] = message.photo[-1].file_id
    await message.answer_photo(photo=data['photo'],
                               caption=f"название: {data['name']}\n"
                               f"цена: {data['price']}\n"
                               f"категория: {data['category']}\n"
                               f"размер: {data['size']}\n"
                               )
    await state.finish()



def reg_handler_fsm_registration(dp: Dispatcher):
    dp.register_message_handler(start_fsm, commands=['registration'])
    dp.register_message_handler(process_name, state=fsm_store.name)
    dp.register_message_handler(process_size, state=fsm_store.size)
    dp.register_message_handler(load_category, state=fsm_store.category)
    dp.register_message_handler(load_price, state=fsm_store.price)
    dp.register_message_handler(load_photo, state=fsm_store.photo,content_types=['photo'])

