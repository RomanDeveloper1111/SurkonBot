from settings.config import dp
from aiogram import types
from aiogram.dispatcher import filters, FSMContext
from .constants import CITIES_VALUES, CAR_OPTIONS
from .inline_buttons import choose_city_board, car_options_board
import pandas as pd


@dp.callback_query_handler(filters.Text(contains='auto'))
async def choose_city(callback: types.CallbackQuery):
    await callback.message.answer(text='🚗')
    await callback.message.answer(text='Раздел - Авто 🚗🔧\nВыберите город: 🌇', reply_markup=choose_city_board)


@dp.callback_query_handler(filters.Text(contains='city_car'))
async def options(callback: types.CallbackQuery, state: FSMContext):
    city = CITIES_VALUES[callback.data]
    await callback.message.answer(text=f'Раздел Авто - {city} 🚗🔧\nВыберите категорию:',
                                  reply_markup=car_options_board)

    async with state.proxy() as data:
        data['current_city'] = city


@dp.callback_query_handler(filters.Text(contains='option_car'))
async def service(callback: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        city = data['current_city']

    service_name = CAR_OPTIONS[callback.data]
    excel_sheet = f'Авто {city}'
    column = f'{service_name} текст'

    s_data = pd.read_excel('SurkonBot.xlsx', sheet_name=excel_sheet, usecols=[column, ], index_col=column)

    for el in s_data.iterrows():
        if type(el[0]) is not float:
            await callback.message.answer(text=str(el))

