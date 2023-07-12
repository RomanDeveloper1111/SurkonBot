from settings.config import dp
from aiogram import types
from aiogram.dispatcher import filters, FSMContext
from .inline_buttons import city_board, iscele_board_1, iscele_board_2, guzel_board_1, guzel_board_2,\
    phamagusta_board_1, phamagusta_board_2, girne_board_1, girne_board_2, nicosia_board_1, nicosia_board_2
from .constants import CITIES_VALUES, SERVICE_OPTIONS
import pandas as pd


@dp.callback_query_handler(filters.Text(contains='services'))
async def choose_city(callback: types.CallbackQuery):
    await callback.message.answer(text='Раздел - Услуги/Места\nВыберите город: 🌇', reply_markup=city_board)


@dp.callback_query_handler((filters.Text(contains='city_service')))
async def show_services(callback: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['current_city'] = CITIES_VALUES[callback.data]
        city = data['current_city']

    if city == 'Никосия':
        markup1 = nicosia_board_1
        markup2 = nicosia_board_2
    elif city == 'Гирне':
        markup1 = girne_board_1
        markup2 = girne_board_2
    elif city == 'Фамагуста':
        markup1 = phamagusta_board_1
        markup2 = phamagusta_board_2
    elif city == 'Гюзельюрт':
        markup1 = guzel_board_1
        markup2 = guzel_board_2
    elif city == 'Искеле':
        markup1 = iscele_board_1
        markup2 = iscele_board_2

    await callback.message.answer(text='Услуги/Места - Искеле 🌇  Выберите категорию:', reply_markup=markup1)
    await callback.message.answer(text='▫▫▫▫▫▫▫▫▫▫▫▫▫▫▫', reply_markup=markup2)


@dp.callback_query_handler(filters.Text(contains='opt_service_'))
async def show_option_info(callback: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        city = data['current_city']

    excel_sheet = f'Услуги {city}'
    column = SERVICE_OPTIONS[callback.data]

    s_data = pd.read_excel('SurkonBot.xlsx', sheet_name=excel_sheet, usecols=[column, ], index_col=column)

    for el in s_data.iterrows():
        if type(el[0]) is not float:
            await callback.message.answer(text=str(el))
