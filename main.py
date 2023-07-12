from modules.real_estate.callbacks import *
from modules.show_places.callbacks import *
from modules.job.callbacks import *
from modules.food.callbacks import *
from modules.car.callbacks import *
from modules.document.callbacks import *
from modules.taxi.callbacks import *
from modules.services.callbacks import *
import pandas as pd
from aiogram.utils.exceptions import BadRequest
from settings.config import dp, bot
from aiogram import types
from aiogram import executor
from aiogram.dispatcher import filters
from constants import ABOUT, ADD_TO_BOT


MAIN_MENU_BOARD = types.InlineKeyboardMarkup().\
    add(types.InlineKeyboardButton(text='↩️Главное меню', callback_data='menu'))

kb = types.InlineKeyboardMarkup(row_width=2)
b1 = types.InlineKeyboardButton(text='🗿 До...ьности', callback_data='showPlaces')
b2 = types.InlineKeyboardButton(text='🏨Нед...мость', callback_data='real_estate')
b3 = types.InlineKeyboardButton(text='🎙 Общий чат', url='https://t.me/surkoncyprus')
b4 = types.InlineKeyboardButton(text='🤵‍♂ Работа', callback_data='job')
b5 = types.InlineKeyboardButton(text='🍣🍿...ка еды', callback_data='food')
b6 = types.InlineKeyboardButton(text='🚗 Авто', callback_data='auto')
b7 = types.InlineKeyboardButton(text='📑Док...помощь', callback_data='document')
b8 = types.InlineKeyboardButton(text='📍 Усл.../Места', callback_data='services')
b9 = types.InlineKeyboardButton(text='🚕 Такси', callback_data='taxi')
b10 = types.InlineKeyboardButton(text='➕ Добавить в бота', callback_data='addToBot')

kb.add(b1, b2, b3, b4, b5, b6, b7, b8, b9, b10)


@dp.message_handler(commands=['menu', 'start'])
async def send_welcome(message: types.Message):
    await message.answer(text='Главное меню, выберите раздел:', reply_markup=kb)


@dp.callback_query_handler(filters.Text(contains='menu'))
async def send_welcome(callback: types.CallbackQuery):
    await callback.message.answer(text='Главное меню, выберите раздел', reply_markup=kb)


@dp.message_handler(commands=['about', 'help'])
async def show_menu_callback(message: types.Message):
    await message.answer(text=ABOUT,
                         reply_markup=MAIN_MENU_BOARD)


@dp.message_handler(filters.Text(contains='afisha'))
async def show_menu_callback(message: types.Message):
    s_data = pd.read_excel('SurkonBot.xlsx', sheet_name='Афиша',
                           usecols=['Текст объявления', 'Ссылка на изображение'],
                           index_col='Текст объявления',
                           )
    for content, pic in s_data.iterrows():
        try:
            await message.answer_photo(photo=pic.values[0])
            await message.answer(text=str(content))
        except BadRequest:
            pass
    await message.answer(text='Скажите, что вы от Surkon bot😉', reply_markup=MAIN_MENU_BOARD)


@dp.callback_query_handler(filters.Text(contains='addToBot'))
async def add_to_bot(callback: types.CallbackQuery):
    await callback.message.answer(text=ADD_TO_BOT, reply_markup=MAIN_MENU_BOARD)


@dp.message_handler(commands=['add_to_bot'])
async def add_to_bot(message: types.Message):
    await message.answer(text=ADD_TO_BOT, reply_markup=MAIN_MENU_BOARD)


async def setup_bot_commands(req):
    bot_commands = [
        types.BotCommand(command="/menu", description="🗂Главное меню"),
        types.BotCommand(command="/afisha", description="⭐Афиша"),
        types.BotCommand(command="/about", description="📢О боте"),
        types.BotCommand(command="/add_to_bot", description="➕Добавить в Бота")
    ]
    await bot.set_my_commands(bot_commands)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=setup_bot_commands)
