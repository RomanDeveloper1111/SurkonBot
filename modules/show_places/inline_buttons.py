from aiogram import types

cities_board = types.InlineKeyboardMarkup(row_width=3)
c1 = types.InlineKeyboardButton(text='Никосия', callback_data='city_place_nikosiya')
c2 = types.InlineKeyboardButton(text='Гирне', callback_data='city_place_girne')
c3 = types.InlineKeyboardButton(text='Фамагуста', callback_data='city_place_phamagusta')
c4 = types.InlineKeyboardButton(text='Гюзельюрт', callback_data='city_place_guzel')
c5 = types.InlineKeyboardButton(text='Искеле', callback_data='city_place_iscle')
c6 = types.InlineKeyboardButton(text='↩️Главное меню', callback_data='menu')
cities_board.add(c1, c2, c3, c4, c5, c6)
