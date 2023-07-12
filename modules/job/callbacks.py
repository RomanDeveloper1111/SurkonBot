from aiogram.dispatcher import filters, FSMContext
from settings.config import dp
from aiogram import types
from .inline_buttons import cities_board, vacancy_and_CV, professions_girne_board, professions_guzel_board, \
    professions_nikosiya_board, professions_iscle_board, professions_phamagusta_board, profile_girne_board, \
    profile_guzel_board, profile_nikosiya_board, profile_iscle_board, profile_phamagusta_board
from .constants import CITIES_VALUES, JOB_VALUES
import pandas as pd


@dp.callback_query_handler(filters.Text(equals='job'))
async def choose_city(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.answer(text='🧑‍💻')
    await callback.message.answer(text='Раздел "Работа"\nВыберите город 🏙:', reply_markup=cities_board)


@dp.callback_query_handler(filters.Text(contains='city_job'))
async def choose_options(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.answer(text=f'Работа - {CITIES_VALUES[callback.data]}🏙',
                                  reply_markup=vacancy_and_CV)
    async with state.proxy() as data:
        data['current_city'] = CITIES_VALUES[callback.data]


@dp.callback_query_handler(filters.Text(contains='vacancy'))
async def vacancy(callback: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        city = data['current_city']

        if city == 'Гирне':
            reply_mark = professions_girne_board
        elif city == 'Гюзельюрт':
            reply_mark = professions_guzel_board
        elif city == 'Никосия':
            reply_mark = professions_nikosiya_board
        elif city == 'Искеле':
            reply_mark = professions_iscle_board
        elif city == 'Фамагуста':
            reply_mark = professions_phamagusta_board
    await callback.message.answer(text=f'Работа - {city}', reply_markup=reply_mark)


@dp.callback_query_handler(filters.Text(contains='professions'))
async def choose_profession(callback: types.CallbackQuery):
    city = callback.data.split('_')

    excel_sheet = f"Работа Вакансии {CITIES_VALUES[f'city_job_{city[2]}']}"
    column = JOB_VALUES[city[1]]

    s_data = pd.read_excel('SurkonBot.xlsx', sheet_name=excel_sheet, usecols=[column,], index_col=column)

    for el in s_data.iterrows():
        if type(el[0]) is not float:
            await callback.message.answer(text=str(el))


@dp.callback_query_handler(filters.Text(contains='CV'))
async def cv(callback: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        city = data['current_city']

        if city == 'Гирне':
            reply_mark = profile_girne_board
        elif city == 'Гюзельюрт':
            reply_mark = profile_guzel_board
        elif city == 'Никосия':
            reply_mark = profile_nikosiya_board
        elif city == 'Искеле':
            reply_mark = profile_iscle_board
        elif city == 'Фамагуста':
            reply_mark = profile_phamagusta_board
    await callback.message.answer(text=f'Работа - {city}', reply_markup=reply_mark)


@dp.callback_query_handler(filters.Text(contains='profile'))
async def choose_profession(callback: types.CallbackQuery):
    city = callback.data.split('_')

    excel_sheet = f"Работа Резюме {CITIES_VALUES[f'city_job_{city[2]}']}"
    column = JOB_VALUES[city[1]]

    s_data = pd.read_excel('SurkonBot.xlsx', sheet_name=excel_sheet, usecols=[column,], index_col=column)

    for el in s_data.iterrows():
        if type(el[0]) is not float:
            await callback.message.answer(text=str(el))





