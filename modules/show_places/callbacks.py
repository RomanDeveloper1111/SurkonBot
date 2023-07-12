from aiogram import types
from aiogram.dispatcher import filters
from settings.config import dp
from .inline_buttons import cities_board
from .constants import CITIES_VALUES
import pandas as pd
from aiogram.utils.exceptions import WrongFileIdentifier


@dp.callback_query_handler(filters.Text(contains='showPlaces'))
async def real_estate(callback: types.CallbackQuery):
    await callback.message.answer(text='🗿')
    await callback.message.answer(text='Раздел - «Достопримечательности» 📸\nВыберите город: 🌇',
                                  reply_markup=cities_board)


@dp.callback_query_handler(filters.Text(contains='city_place'))
async def city_place(callback: types.CallbackQuery):
    s_data = pd.read_excel('SurkonBot.xlsx', sheet_name='Достопримечательности',
                           usecols=['Текст ' + CITIES_VALUES[callback.data],
                                    'Картинка ' + CITIES_VALUES[callback.data]],
                           index_col='Текст ' + CITIES_VALUES[callback.data],
                           )

    for content, pic in s_data.iterrows():
        if type(pic.values[0]) is not float:
            try:
                await callback.message.answer_photo(pic.values[0])
                await callback.message.answer(text=str(content))
            except WrongFileIdentifier:
                pass


