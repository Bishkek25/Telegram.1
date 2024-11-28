from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import Text
from aiogram.types import ReplyKeyboardRemove

from db import db_main
import buttons
from handlers.fsm_reg import start_fsm
import db.db_main  # Correct import based on your folder structure



class store_fsm(StatesGroup):
    name_product = State()
    product_id = State()
    size = State()
    price = State()
    info_products = State()
    category = State()
    collection = State()
    photo = State()
    submit = State()

async def start_fsm_store(message: types.Message):
    await store_fsm.name_product.set()
    await message.answer(text='Введите название товара:')
                         # reply_markup=buttons.cansel)

async def load_name_product(message: types.Message, state : FSMContext):
     async with state.proxy() as data:
         data['name_product'] = message.text

     await message.answer('введите артикул для товара:')
     await store_fsm.next()


async def load_product_id(message: types.Message, state : FSMContext):
    async with state.proxy() as data:
        data['product_id'] = message.text

    await message.answer('введите размер товара:')
    await store_fsm.next()


async def load_size(message: types.Message, state : FSMContext):
        async with state.proxy() as data:
            data['size'] = message.text

        await message.answer('введите цену товара:')
        await store_fsm.next()


async def load_price(message: types.Message, state : FSMContext):
    async with state.proxy() as data:
        data['price'] = message.text

    await message.answer('отправьте информацию о товаре:')
    await store_fsm.next()

async def load_info_product(message: types.Message, state : FSMContext):
        async with state.proxy() as data:
            data['info_product'] = message.text

        await message.answer('введите категорию товара:')
        await store_fsm.next()

async def load_category(message: types.Message, state : FSMContext):
    async with state.proxy() as data:
        data['category'] = message.text

    await message.answer('отправьте коллекцию товара:')
    await store_fsm.next()

async def load_collection(message: types.Message, state : FSMContext):
    async with state.proxy() as data:
        data['collection'] = message.text

    await message.answer('отправьте фото товара:')
    await store_fsm.next()




async def load_photo(message: types.Message, state : FSMContext):
        async with state.proxy() as data:
            data['photo'] = message.photo[-1].file_id

        await message.answer_photo(photo=data['photo'],
                                   caption=f"заполненный товар:\n"
                                           f"название - {data['name_product']}\n"
                                           f"Артикул - {data['product_id']}\n"
                                           f"Размер - {data['size']}\n"
                                           f"цена - {data['price']}\n"
                                           f"информация о товаре - {data['info_product']}\n"
                                           f"категория товара - {data['category']}\n")

        await message.answer('Верные ли данные?', reply_markup=buttons.submit)
        await store_fsm.next()

async def submit(message: types.Message, state : FSMContext):
    if message.text =='Да':
        kb_remove = ReplyKeyboardRemove()
        await message.answer('Отлично товар в базе!', reply_markup = kb_remove)


        async with state.proxy() as data:
            await db_main.sql_insert_store(
                name_product=data['name_product'],
                product_id=data['product_id'],
                size=data['size'],
                price=data['price'],
                photo=data['photo'],
            )
            await db_main.sql_insert_collection(
                product_id=data['product_id'],
                collection=data['collection'],
            )
            await db_main.sql_insert_store_detail(
                info_product=data['info_product'],
                product_id=data['product_id'],
                category_id=data['category'],
            )
        # await dp_main.
    elif message.text == 'Нет':
        kb_remove = ReplyKeyboardRemove()
        await message.answer('Отменено!', reply_markup = kb_remove)
    else:
        await message.answer('Введите да или нет')

async def cancel_fsm(message: types.Message, state : FSMContext):
    current_state = await state.get_state()

    kb_remove = ReplyKeyboardRemove()

    if current_state is not None:
        await state.finish()
        await message.answer('Отменено!', reply_markup=kb_remove)

def reg_handler_fsm_store(dp: Dispatcher):
    # dp.register_message_handler(start_fsm_store, Text(equals='Отмена!', ignore_case=True),
    #                             state="*")

    dp.register_message_handler(start_fsm_store, commands=['store'])
    dp.register_message_handler(load_name_product, state=store_fsm.name_product)
    dp.register_message_handler(load_product_id, state=store_fsm.product_id)
    dp.register_message_handler(load_size, state=store_fsm.size)
    dp.register_message_handler(load_price, state=store_fsm.price)
    dp.register_message_handler(load_info_product, state=store_fsm.info_products)
    dp.register_message_handler(load_category, state=store_fsm.category)
    dp.register_message_handler(load_collection, state=store_fsm.collection)
    dp.register_message_handler(load_photo, state=store_fsm.photo, content_types=['photo'])
    dp.register_message_handler(submit, state=store_fsm.submit)