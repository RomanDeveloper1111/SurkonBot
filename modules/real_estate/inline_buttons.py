from aiogram import types

selection_board = types.InlineKeyboardMarkup()
selection_board.add(types.InlineKeyboardButton(text='Получить подборку',
                                               url='https://b24-3ooe85.bitrix24.site/crm_form_mk6lt/'))

cities_board = types.InlineKeyboardMarkup(row_width=3)
c1 = types.InlineKeyboardButton(text='Никосия', callback_data='city_real_nikosiya')
c2 = types.InlineKeyboardButton(text='Гирне', callback_data='city_real_girne')
c3 = types.InlineKeyboardButton(text='Фамагуста', callback_data='city_real_phamagusta')
c4 = types.InlineKeyboardButton(text='Гюзельюрт', callback_data='city_real_guzel')
c5 = types.InlineKeyboardButton(text='Искеле', callback_data='city_real_iscle')
c6 = types.InlineKeyboardButton(text='↩️Главное меню', callback_data='menu')
cities_board.add(c1, c2, c3, c4, c5, c6)

rent_or_buy_board = types.InlineKeyboardMarkup(row_width=2)
b1 = types.InlineKeyboardButton(text='Аренда', callback_data='rent_estate')
b2 = types.InlineKeyboardButton(text='Покупка', callback_data='buy_estate')
b3 = types.InlineKeyboardButton(text='↩️Главное меню', callback_data='menu')
rent_or_buy_board.add(b1, b2, b3)

rent_board = types.InlineKeyboardMarkup(row_width=1)
r1 = types.InlineKeyboardButton(text='Чат аренды недвижимости', url='https://t.me/severkipr')
r2 = types.InlineKeyboardButton(text='Добавить в бота', callback_data='addToBot')
r3 = types.InlineKeyboardButton(text='↩️Главное меню', callback_data='menu')
rent_board.add(r1, r2, r3)

add_to_bot_and_main_menu = types.InlineKeyboardMarkup(row_width=1)
b1 = types.InlineKeyboardButton(text='Добавить в бота', callback_data='addToBot')
b2 = types.InlineKeyboardButton(text='↩️Главное меню', callback_data='menu')
add_to_bot_and_main_menu.add(b1, b2)
