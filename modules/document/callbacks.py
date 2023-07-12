from settings.config import dp
from aiogram import types
from aiogram.dispatcher import filters, FSMContext
from .inline_buttons import choose_city_board
from .constants import TYPE_OF_DOCUMENTS
import pandas as pd


@dp.callback_query_handler(filters.Text(contains='document'))
async def choose_option(callback: types.CallbackQuery):
    await callback.message.answer(text='📁')
    await callback.message.answer(text='Раздел - «Документы/Помощь»🤝\nВыберите услугу:',
                                  reply_markup=choose_city_board)


@dp.callback_query_handler(filters.Text(contains='doc_'))
async def option_info(callback: types.CallbackQuery):
    excel_sheet = 'Документы'
    column = TYPE_OF_DOCUMENTS[callback.data]

    s_data = pd.read_excel('SurkonBot.xlsx', sheet_name=excel_sheet, usecols=[column, ], index_col=column)

    for el in s_data.iterrows():
        if type(el[0]) is not float:
            await callback.message.answer(text=str(el))