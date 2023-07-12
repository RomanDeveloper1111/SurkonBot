from aiogram import types

BM = types.InlineKeyboardButton(text='↩️Главное меню', callback_data='menu')
BA = types.InlineKeyboardButton(text='Добавить в бота', callback_data='addToBot')

choose_city_board = types.InlineKeyboardMarkup(row_width=2)
c1 = types.InlineKeyboardButton(text='👩‍🎓Поступление в университет', callback_data='doc_uni')
c2 = types.InlineKeyboardButton(text='🇨🇾Гражданство', callback_data='doc_citizenship')
c3 = types.InlineKeyboardButton(text='🇺🇳Бизнес-виза', callback_data='doc_businessvisa')
c4 = types.InlineKeyboardButton(text='🚘Легелизация авто', callback_data='doc_auto')
c5 = types.InlineKeyboardButton(text='💼Открытие фирмы', callback_data='doc_openfirm')
c6 = types.InlineKeyboardButton(text='📝Получение ВНЖ', callback_data='doc_getVNZ')
c7 = types.InlineKeyboardButton(text='📃Доверенность', callback_data='doc_proxy')
c8 = types.InlineKeyboardButton(text='📑Загранпаспорт', callback_data='doc_passport')
c9 = types.InlineKeyboardButton(text='🇭🇺Шенген Виза', callback_data='doc_shengenvisa')
c10 = types.InlineKeyboardButton(text='📱Разблокирование телефона', callback_data='doc_unlockphone')
choose_city_board.add(c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, BM, BA)
