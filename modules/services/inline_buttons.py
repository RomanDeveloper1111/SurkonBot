from aiogram import types


BM = types.InlineKeyboardButton(text='↩️Главное меню', callback_data='menu')
BA = types.InlineKeyboardButton(text='Добавить в бота', callback_data='addToBot')


city_board = types.InlineKeyboardMarkup(row_width=3)
c1 = types.InlineKeyboardButton(text='Никосия', callback_data='city_service_nikosiya')
c2 = types.InlineKeyboardButton(text='Гирне', callback_data='city_service_girne')
c3 = types.InlineKeyboardButton(text='Фамагуста', callback_data='city_service_phamagusta')
c4 = types.InlineKeyboardButton(text='Гюзельюрт', callback_data='city_service_guzel')
c5 = types.InlineKeyboardButton(text='Искеле', callback_data='city_service_iscle')
city_board.add(c1, c2, c3, c4, c5, BM, BA)


b1 = types.InlineKeyboardButton(text='SMM/WEB', callback_data='opt_service_SMM')
b2 = types.InlineKeyboardButton(text='Аптеки', callback_data='opt_service_pharmacy')
b3 = types.InlineKeyboardButton(text='Ателье', callback_data='opt_service_studio')
b4 = types.InlineKeyboardButton(text='Бани/Хамам', callback_data='opt_service_bathhouse')
b5 = types.InlineKeyboardButton(text='Больницы', callback_data='opt_service_hospital')
b6 = types.InlineKeyboardButton(text='Вейпы', callback_data='opt_service_veyp')
b7 = types.InlineKeyboardButton(text='ВетКлиники', callback_data='opt_service_pethospital')
b8 = types.InlineKeyboardButton(text='Вода/Газ', callback_data='opt_service_water')
b9 = types.InlineKeyboardButton(text='Грузоперевозки', callback_data='opt_service_supplying')
b10 = types.InlineKeyboardButton(text='Детские сады', callback_data='opt_service_child')
b11 = types.InlineKeyboardButton(text='Дизайн', callback_data='opt_service_design')
b12 = types.InlineKeyboardButton(text='Еда на заказ', callback_data='opt_service_orderfood')
b13 = types.InlineKeyboardButton(text='Интернет Кафе', callback_data='opt_service_netcafe')
b14 = types.InlineKeyboardButton(text='Казино', callback_data='opt_service_casino')
b15 = types.InlineKeyboardButton(text='Кальянные', callback_data='opt_service_smoking')
b16 = types.InlineKeyboardButton(text='Караоке', callback_data='opt_service_karaoke')
b17 = types.InlineKeyboardButton(text='Кафе/Бары', callback_data='opt_service_cafebars')
b18 = types.InlineKeyboardButton(text='Клининг', callback_data='opt_service_cleaning')
b19 = types.InlineKeyboardButton(text='Компьютерная помощь', callback_data='opt_service_pchelp')
b20 = types.InlineKeyboardButton(text='Копи центр', callback_data='opt_service_copycentre')
b21 = types.InlineKeyboardButton(text='Красота', callback_data='opt_service_spa')
b22 = types.InlineKeyboardButton(text='Массаж', callback_data='opt_service_massage')
b23 = types.InlineKeyboardButton(text='Няни', callback_data='opt_service_nanny')
b24 = types.InlineKeyboardButton(text='Парикмахерские', callback_data='opt_service_barbershop')
b25 = types.InlineKeyboardButton(text='Пляжи', callback_data='opt_service_beach')
b26 = types.InlineKeyboardButton(text='Прачечные', callback_data='opt_service_laundry')
b27 = types.InlineKeyboardButton(text='Развлечения', callback_data='opt_service_entertainment')
b28 = types.InlineKeyboardButton(text='Ремонт', callback_data='opt_service_repair')
b29 = types.InlineKeyboardButton(text='Рестораны', callback_data='opt_service_restaurant')
b30 = types.InlineKeyboardButton(text='Рынки', callback_data='opt_service_market')
b31 = types.InlineKeyboardButton(text='Салон связи', callback_data='opt_service_serviceline')
b32 = types.InlineKeyboardButton(text='Саморазвитие', callback_data='opt_service_selfdev')
b33 = types.InlineKeyboardButton(text='Спорт', callback_data='opt_service_sport')
b34 = types.InlineKeyboardButton(text='Страхование', callback_data='opt_service_insurance')
b35 = types.InlineKeyboardButton(text='Супермаркеты', callback_data='opt_service_supermarkets')
b36 = types.InlineKeyboardButton(text='ТВ-Интернет', callback_data='opt_service_TV')
b37 = types.InlineKeyboardButton(text='ТЦ', callback_data='opt_service_mall')
b38 = types.InlineKeyboardButton(text='Фото/Видео', callback_data='opt_service_photo')
b39 = types.InlineKeyboardButton(text='Цветы', callback_data='opt_service_flowers')
b40 = types.InlineKeyboardButton(text='Школы', callback_data='opt_service_schools')
b41 = types.InlineKeyboardButton(text='Тату', callback_data='opt_service_tattoo')
b42 = types.InlineKeyboardButton(text='Москитные сетки', callback_data='opt_service_masknet')
b43 = types.InlineKeyboardButton(text='Музыкальное искусство', callback_data='opt_service_music')



iscele_board_1 = types.InlineKeyboardMarkup(row_width=3)
iscele_board_1.add(b17, b13, b12, b21, b5, b7, b8, b11, b3, b9, b6, b18, b10, b2, b15, b22, b16, b26, b42, b14, b23, b19)

iscele_board_2 = types.InlineKeyboardMarkup(row_width=3)
iscele_board_2.add(b29, b35, b30, b40, b27, b37, b32, b33, b28, b36, b34, b38, b20, b31, b1, BM, BA)


guzel_board_1 = types.InlineKeyboardMarkup(row_width=3)
guzel_board_1.add(b13, b17, b4, b12, b25, b21, b5, b7, b9, b18, b6, b10, b11, b2, b19, b3, b24)

guzel_board_2 = types.InlineKeyboardMarkup(row_width=3)
guzel_board_2.add(b29, b35, b40, b27, b37, b32, b33, b28, b36, b34, b38, b20, b31, b1, BM, BA)


phamagusta_board_1 = types.InlineKeyboardMarkup(row_width=3)
phamagusta_board_1.add(b17, b13, b12, b25, b6, b21, b5, b7, b2, b24, b8, b9, b10, b18, b11, b14, b22, b23, b4, b15, b3,
                       b16, b19, b26)

phamagusta_board_2 = types.InlineKeyboardMarkup(row_width=3)
phamagusta_board_2.add(b29, b35, b30, b40, b27, b37, b32, b33, b39, b28, b36, b34, b38, b20, b31, b1, BM, BA)


girne_board_1 = types.InlineKeyboardMarkup(row_width=3)
girne_board_1.add(b17, b12, b13, b21, b25, b8, b24, b5, b7, b2, b9, b4, b10, b6, b11, b14, b18, b19, b22, b23, b43, b3, b26)

girne_board_2 = types.InlineKeyboardMarkup(row_width=3)
girne_board_2.add(b29, b35, b30, b40, b27, b37, b32, b33, b28, b36, b34, b38, b20, b31, b1, BM, BA)



nicosia_board_1 = types.InlineKeyboardMarkup(row_width=3)
nicosia_board_1.add(b17, b24, b12, b13, b5, b7, b9, b6, b10, b8, b21, b11, b18, b14, b4, b2, b22, b26, b3, b19)

nicosia_board_2 = types.InlineKeyboardMarkup(row_width=3)
nicosia_board_2.add(b29, b35, b30, b40, b27, b37, b32, b33, b28, b36, b34, b38, b20, b31, b1, BM, BA)







