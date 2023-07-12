from aiogram import types
from aiogram.utils.exceptions import WrongFileIdentifier

from settings.config import dp
from aiogram.dispatcher import filters
from .constants import CITIES_VALUES
from .inline_buttons import choose_city_board, navigation_board
import pandas as pd


@dp.callback_query_handler(filters.Text(contains='taxi'))
async def choose_city(callback: types.CallbackQuery):
    await callback.message.answer(text='🚕')
    await callback.message.answer(text='Раздел - Такси 🚖🚕\nВыберите город: 🌇',
                                  reply_markup=choose_city_board)


@dp.callback_query_handler(filters.Text(contains='city_tax'))
async def get_info(callback: types.CallbackQuery):
    excel_sheet = 'Такси'
    column1 = f'{CITIES_VALUES[callback.data]} текст'
    column2 = f'{CITIES_VALUES[callback.data]} изображение'

    s_data = pd.read_excel('SurkonBot.xlsx', sheet_name=excel_sheet, usecols=[column1, column2], index_col=column1)

    for content, pic in s_data.iterrows():
        if type(content) is not float:
            await callback.message.answer(text=str(content))
            if type(pic.values[0]) is not float:
                try:
                    await callback.message.answer_photo(photo=pic.values[0])
                except WrongFileIdentifier:
                    pass
    await callback.message.answer(text='Навигация:', reply_markup=navigation_board)
