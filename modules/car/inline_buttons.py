from aiogram import types


BM = types.InlineKeyboardButton(text='↩️Главное меню', callback_data='menu')
BA = types.InlineKeyboardButton(text='Добавить в бота', callback_data='addToBot')


choose_city_board = types.InlineKeyboardMarkup(row_width=3)
c1 = types.InlineKeyboardButton(text='Никосия', callback_data='city_car_nikosiya')
c2 = types.InlineKeyboardButton(text='Гирне', callback_data='city_car_girne')
c3 = types.InlineKeyboardButton(text='Фамагуста', callback_data='city_car_phamagusta')
c4 = types.InlineKeyboardButton(text='Гюзельюрт', callback_data='city_car_guzel')
c5 = types.InlineKeyboardButton(text='Искеле', callback_data='city_car_iscle')
choose_city_board.add(c1, c2, c3, c4, c5, BM, BA)

car_options_board = types.InlineKeyboardMarkup(row_width=3)
c1 = types.InlineKeyboardButton(text='Аренда авто', callback_data='option_car_rent')
c2 = types.InlineKeyboardButton(text='Продажа авто', callback_data='option_car_sell')
c3 = types.InlineKeyboardButton(text='Автосервисы', callback_data='option_car_service')
c4 = types.InlineKeyboardButton(text='Химчистка', callback_data='option_car_cleaning')
c5 = types.InlineKeyboardButton(text='Автоподбор', callback_data='option_car_choose')
c6 = types.InlineKeyboardButton(text='Автострахование', callback_data='option_car_insurance')
car_options_board.add(c1, c2, c3, c4, c5, c6, BM, BA)
