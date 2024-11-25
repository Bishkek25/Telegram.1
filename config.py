from Tools.scripts.objgraph import store
from aiogram import Bot, Dispatcher
from decouple import config
from aiogram.contrib.fsm_storage.memory import MemoryStorage

token = config('TOKEN')
bot = Bot(token=token)
Storage = MemoryStorage()
dp = Dispatcher(bot, storage=Storage)
