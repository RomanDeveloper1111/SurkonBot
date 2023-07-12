from settings.config import dp
from aiogram import types
from aiogram.dispatcher import filters
import emoji
from .inline_buttons import selection_board, cities_board, rent_or_buy_board, rent_board, add_to_bot_and_main_menu
from .constants import CITIES_VALUES


@dp.callback_query_handler(filters.Text(contains='real_estate'))
async def show_places(callback_query: types.CallbackQuery):
    await callback_query.message.answer(text=emoji.emojize(":house:"))
    await callback_query.message.answer(
        text='Заполните короткую форму и получите бесплатно подборку в один клик по вашему запросу',
        reply_markup=selection_board
    )
    await callback_query.message.answer(text='Раздел - \"Недвижимость\"\nВыберите город 🌇:',
                                        reply_markup=cities_board)


@dp.callback_query_handler(filters.Text(contains='city_real'))
async def get_city(callback: types.callback_query):
    usr_msg = CITIES_VALUES[callback.data] + '🌇'
    await callback.message.answer(text=f'{usr_msg}\nВыберите категорию:', reply_markup=rent_or_buy_board)


@dp.callback_query_handler(filters.Text(contains='rent_estate'))
async def rent_info(callback: types.callback_query):
    await callback.message.answer(text="Аренду проверенных объектов на Северном Кипре вы можете посмотреть в"
                                       " чате наших партнеров https://t.me/severkipr\nСкажите, что вы от Surkon bot"
                                       + emoji.emojize(":winking_face:"),
                                  reply_markup=rent_board
                                  )


@dp.callback_query_handler(filters.Text(contains='buy_estate'))
async def rent_info(callback: types.callback_query):
    await callback.message.answer(text=emoji.emojize(":house:"))
    await callback.message.answer(text='Заполните короткую форму и получите бесплатно подборку '
                                       'в один клик по вашему запросу',
                                  reply_markup=types.InlineKeyboardMarkup().
                                  add(types.InlineKeyboardButton(text='Получить подборку',
                                                                 url='https://b24-3ooe85.bitrix24.site/crm_form_mk6lt/'))
                                  )
    await callback.message.answer(text="Данный раздел еще не заполнен, но в скором времени он будет доступен. "
                                       "Сюда вы можете разместить свое объявление - нажмите добавиться в бота.",
                                  reply_markup=add_to_bot_and_main_menu
                                  )
