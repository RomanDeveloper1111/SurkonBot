from aiogram.dispatcher import filters, FSMContext
from aiogram.utils.exceptions import WrongFileIdentifier

from settings.config import dp
from aiogram import types
from .inline_buttons import choose_city_board
from .constants import CITIES_VALUES
import pandas as pd


@dp.callback_query_handler(filters.Text(contains='food'))
async def choose_city(callback: types.CallbackQuery):
    text = "Раздел - Доставка еды 🍔🍟🍣\nВыберите город: 🌇"
    await callback.message.answer(text='🍕')
    await callback.message.answer(text=text, reply_markup=choose_city_board)


@dp.callback_query_handler(filters.Text(contains='city_eat'))
async def view_food_by_city(callback: types.CallbackQuery):
    excel_sheet = 'Доставка еды'
    column1 = f'{CITIES_VALUES[callback.data]} текст'
    column2 = f'{CITIES_VALUES[callback.data]} изображение'

    s_data = pd.read_excel('SurkonBot.xlsx', sheet_name=excel_sheet, usecols=[column1, column2], index_col=column1)

    for content, pic in s_data.iterrows():
        if type(pic.values[0]) is not float:
            try:
                # if pic.values[0][:3] == 'http':      Надо решить проблему с картинками в excel - много исключений!
                #     await callback.message.answer_photo(pic.values[0])
                await callback.message.answer(text=str(content))
            except WrongFileIdentifier:
                pass

