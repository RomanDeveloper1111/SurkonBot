from aiogram import types

BM = types.InlineKeyboardButton(text='↩️Главное меню', callback_data='menu')
BA = types.InlineKeyboardButton(text='Добавить в бота', callback_data='addToBot')


choose_city_board = types.InlineKeyboardMarkup(row_width=3)
c1 = types. InlineKeyboardButton(text='Никосия', callback_data='city_eat_nikosiya')
c2 = types. InlineKeyboardButton(text='Гирне', callback_data='city_eat_girne')
c3 = types. InlineKeyboardButton(text='Фамагуста', callback_data='city_eat_phamagusta')
c4 = types. InlineKeyboardButton(text='Гюзельюрт', callback_data='city_eat_guzel')
c5 = types. InlineKeyboardButton(text='Искеле', callback_data='city_eat_iscle')
choose_city_board.add(c1, c2, c3, c4, c5, BM, BA)
