from aiogram import Dispatcher, Bot, executor, types
import logging
import random

import parsers

point = 0

BOT_TOKEN = '1439523746:AAEIIQyQr-dKzxD13nW836nWiGM42_fIwR8'

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

logging.basicConfig(level=logging.INFO)

keyboard = types.ReplyKeyboardMarkup(
    resize_keyboard=True, one_time_keyboard=True)
genre_button = types.KeyboardButton('Топ фильмов по жанру')
selections_button = types.KeyboardButton('Получить подборку')
random_film_button = types.KeyboardButton('Случайный фильм')
game_film_button = types.KeyboardButton('Угадай фильм')

keyboard.add(genre_button, selections_button, random_film_button, game_film_button)

keyboard_game = types.ReplyKeyboardMarkup(
    resize_keyboard=True, one_time_keyboard=False)
stat_game_button = types.KeyboardButton('Статистика')
back_game_button = types.KeyboardButton('Назад')

keyboard_game.add(stat_game_button, back_game_button)


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await bot.send_message(message.chat.id,
                           'Привет! Выбери нужную опцию на клавиатуре, чтобы получить кино на твой вкус.',
                           reply_markup=keyboard)


@dp.message_handler(text=["Угадай фильм"])
async def game1(message):
    inlinekeyboard = types.InlineKeyboardMarkup()
    black_btn = types.InlineKeyboardButton(text='Чёрная пантера')
    Dad_btn = types.InlineKeyboardButton(text='Здравствуй, папа, Новый год! 2')
    two_btn = types.InlineKeyboardButton(text='Мстители')
    DAd_btn = types.InlineKeyboardButton(text='Отцы и деды')
    inlinekeyboard.add(black_btn, Dad_btn,
                       two_btn, DAd_btn)
    await bot.send_message(message.chat.id, 'Откуда цитата "Плох тот отец, что не подготовил детей к своему уходу."?', reply_markup=inlinekeyboard)



@dp.message_handler(text=['Получить подборку'])
async def send_selections(message: types.Message):
    films = parsers.get_selections()
    key = random.randint(0, 12)
    formatted_reply = '<strong>' + films[key]['films_name'] + '</strong>' + '\n\n' + \
        'Количество фильмов в подборке: ' + \
        films[key]['films_count'] + '\n\n' + films[key]['films_link']
    await bot.send_message(message.chat.id, formatted_reply, parse_mode='HTML', reply_markup=keyboard)


@dp.message_handler(lambda message: "Топ фильмов по жанру" in message.text)
async def search(message: types.Message):
    inlinekeyboard = types.InlineKeyboardMarkup()
    sci_fi_btn = types.InlineKeyboardButton(
        'Научная фантастика', url='https://www.filmpro.ru/movies/top?page=1&year_from=&year_to=&genres[]=17')
    drama_btn = types.InlineKeyboardButton(
        'Драма', url='https://www.filmpro.ru/movies/top?page=1&year_from=&year_to=&genres[]=6')
    boevik_btn = types.InlineKeyboardButton(
        'Боевик', url='https://www.filmpro.ru/movies/top?page=1&year_from=&year_to=&genres[]=22')
    anime_btn = types.InlineKeyboardButton(
        'Аниме', url='https://www.filmpro.ru/movies/top?page=1&year_from=&year_to=&genres[]=31')
    multfilm_btn = types.InlineKeyboardButton(
        'Мультфильм', url='https://www.filmpro.ru/movies/top?page=1&year_from=&year_to=&genres[]=21')
    comedy_btn = types.InlineKeyboardButton(
        'Комедия', url='https://www.filmpro.ru/movies/top?page=1&year_from=&year_to=&genres[]=3')
    voen_films_btn = types.InlineKeyboardButton(
        'Военные фильмы', url='https://www.filmpro.ru/movies/top?page=1&year_from=&year_to=&genres[]=8')
    documentary_films_btn = types.InlineKeyboardButton(
        'Документальные фильмы', url='https://www.filmpro.ru/movies/top?page=1&year_from=&year_to=&genres[]=1')
    history_films_btn = types.InlineKeyboardButton(
        'Исторические фильмы', url='https://www.filmpro.ru/movies/top?page=1&year_from=&year_to=&genres[]=24')
    criminal_btn = types.InlineKeyboardButton(
        'Криминал', url='https://www.filmpro.ru/movies/top?page=1&year_from=&year_to=&genres[]=10')
    mistik_btn = types.InlineKeyboardButton(
        'Мистика', url='https://www.filmpro.ru/movies/top?page=1&year_from=&year_to=&genres[]=23')
    vestern_btn = types.InlineKeyboardButton(
        'Вестерн', url='https://www.filmpro.ru/movies/top?page=1&year_from=&year_to=&genres[]=26')

    inlinekeyboard.add(sci_fi_btn, drama_btn, boevik_btn,
                       anime_btn, multfilm_btn, comedy_btn,
                       vestern_btn, voen_films_btn, documentary_films_btn,
                       history_films_btn, criminal_btn, mistik_btn)
    await bot.send_message(message.chat.id, 'Выберите жанр', reply_markup=inlinekeyboard)


@dp.message_handler(text=['Случайный фильм'])
async def random_film(message: types.Message):
    await bot.send_message(message.chat.id, 'Немного подождите, выбираем фильм...')
    random_genre_id = [22, 21, 6, 31, 17, 3, 8, 1, 24, 10, 23, 26]
    films = parsers.get_genre(random.choice(random_genre_id))
    films_key = random.randint(0, 60)
    formatted_message = '<strong>' + films[films_key]['film_name'] + '</strong>' + '\n\n' + \
        'Жанр: ' + films[films_key]['film_genre'] + '\n\n' + \
        films[films_key]['film_link']
    await bot.send_message(message.chat.id, formatted_message,
                           parse_mode='HTML', reply_markup=keyboard)

#@dp.message_handler(text=['Угадай фильм'])
#async def games_start(message: types.Message):
#    await bot.send_message(message.chat.id,
#                            'Гейммастер: Игра работает так. \n Я предоставляю вам картинку, а вы угадываете по ней фильм. \n Правил нет. \n Удачной игры',
#                        reply_markup=keyboard_game)

@dp.message_handler(text=['Назад'])
async def games_start(message: types.Message):
    await bot.send_message(message.chat.id,
                           '...', reply_markup=keyboard)

######################################################################################################################
#   GAME
######################################################################################################################

if point <= 15:
    otpoint = 1
elif point <= 30:
    otpoint = 2
else:
    otpoint = 3

executor.start_polling(dp, skip_updates=True)
