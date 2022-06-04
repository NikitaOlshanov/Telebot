# t.me/Olshanov_Nikita_1MD4_bot

#Final versionn

import telebot
from telebot import types
import requests
import bs4
from datetime import datetime
from pycbrf import ExchangeRates
import SECRET
from menuBot import Menu
import menuBot
from BotGames import Dice
import random
from BotGames import GameRPS
from BotGames import stopGame
import DZ
# ----------------------------------------------------------------------------------------------------------------------
bot = telebot.TeleBot(SECRET.TOKEN)

@bot.message_handler(commands=["start"])
def command(message):
    chat_id = message.chat.id
    bot.send_sticker(chat_id, "CAACAgIAAxkBAAEEomVic_KNNDHWj8UfQU3SuimB_tLNOQACug4AAh0riUs8l5PXehBSVSQE")
    txt_message = f"Здравствуй, {message.from_user.first_name}! Я Бот Выдрочка!\nТы можешь написать мне что-либо, или использовать уже готовые команды.)"
    bot.send_message(chat_id, text=txt_message, reply_markup=Menu.getMenu("Главное меню").markup)




@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    chat_id = message.chat.id
    ms_text = message.text

    cur_user = menuBot.Users.getUser(chat_id)
    if cur_user is None:
        cur_user = menuBot.Users(chat_id, message.json["from"])

    result = goto_menu(chat_id,ms_text)
    if result == True:
        return

    if Menu.cur_menu != None and ms_text in Menu.cur_menu.buttons:



        if ms_text == "Помощь":
            send_help(chat_id)



        elif ms_text == "Курсы валют":
            bot.send_message(chat_id, text='Выбери валюту')



        elif ms_text =='USD':
                message_norm = ms_text.strip().lower()
                if message_norm in ['usd', 'eur']:
                    rates = ExchangeRates(datetime.now())
                    bot.send_message(chat_id, text=f"Курс {message_norm.upper()} на\n{datetime.now().strftime('%d.%m.%Y %H:%M')}\n{float(rates[message_norm.upper()].rate)} мать его рублей!",
                                     parse_mode="html")

        elif ms_text == 'EUR':
                message_norm = ms_text.strip().lower()
                if message_norm in ['usd', 'eur']:
                    rates = ExchangeRates(datetime.now())
                    bot.send_message(chat_id,
                                     text=f"Курс {message_norm.upper()} на\n{datetime.now().strftime('%d.%m.%Y %H:%M')}\n{float(rates[message_norm.upper()].rate)} мать его рублей!",
                                     parse_mode="html")



        elif ms_text == "Рассказать анекдот":
            bot.send_message(chat_id, text=get_anekdot())



        elif ms_text == "Показать собачку":
            bot.send_message(chat_id, text=f"{get_dog()}\nВот твоя собака <3")



        elif ms_text == "Показать лисичку":
            bot.send_message(chat_id, text=f"{get_fox()}\nВот твоя лисичка <3")



        elif ms_text == "Показать уточку":
            bot.send_message(chat_id, text=f"{get_duck()}\nВот твоя уточка <3")



        elif ms_text == "Вебка":
            video = open("чипсы.mp4", "rb")
            bot.send_video(chat_id, video)



        elif ms_text == 'Угадай число':
            digitgames(message)



        elif ms_text == "Бросить кость":
            dc = Dice()
            text_game = dc.playerChoice()
            bot.send_message(chat_id, text=text_game)


        elif ms_text in GameRPS.values:
            GRPS = GameRPS()
            text_game = GRPS.playerChoice(ms_text)
            bot.send_message(chat_id, text=text_game)


        elif ms_text == "BTC":
            req = requests.get("https://yobit.net/api/3/ticker/btc_usd")
            response = req.json()
            sell_price = response["btc_usd"]["sell"]
            bot.send_message(chat_id, text=f"Цена BTC на\n{datetime.now().strftime('%d.%m.%Y %H:%M')}\n{sell_price} $")



        elif ms_text == "Фильм":
            send_film(bot, chat_id)



        elif ms_text == "Стоп!" or ms_text == "Выйти":
                stopGame(chat_id)
                goto_menu(chat_id, "Выход")
                return


        elif ms_text == "ДЗ №1":
            DZ.dz1(bot, chat_id)

        elif ms_text == "ДЗ №2":
            DZ.dz2(bot, chat_id)

        elif ms_text == "ДЗ №3":
            DZ.dz3(bot, chat_id)

        elif ms_text == "ДЗ №4":
            DZ.dz4(bot, chat_id)

        elif ms_text == "ДЗ №5":
            DZ.dz5(bot, chat_id)

        elif ms_text == "ДЗ №6":
            DZ.dz7(bot, chat_id)

        elif ms_text == "ДЗ №7":
            DZ.dz8(bot, chat_id)

        elif ms_text == "ДЗ №8":
            DZ.dz10(bot, chat_id)


        else:
            bot.send_message(chat_id, text="К сожалению, я не распознал твою команду: " + ms_text)
            goto_menu(chat_id, "Главное меню")
# ----------------------------------------------------------------------------------------------------------------------
def goto_menu(chat_id, name_menu):
    if name_menu == "Выход" and Menu.cur_menu != None and Menu.cur_menu.parent != None:
        target_menu = Menu.getMenu(Menu.cur_menu.parent.name)
    else:
        target_menu = Menu.getMenu(name_menu)
    if target_menu != None:
        bot.send_message(chat_id, text=target_menu.name, reply_markup=target_menu.markup)



def get_fox():
    contents = requests.get('https://randomfox.ca/floof/').json()
    urlFOX= contents['image']
    return urlFOX



def get_dog():
    contents = requests.get('https://random.dog/woof.json').json()
    urlDOG = contents['url']
    return urlDOG



def get_duck():
    contents = requests.get('https://random-d.uk/api/random').json()
    urlDUCK = contents['url']
    return urlDUCK


def get_anekdot():
    array_anekdots = []
    req_anek = requests.get('http://anekdotme.ru/random')
    soup = bs4.BeautifulSoup(req_anek.text, "html.parser")
    result_find = soup.select('.anekdot_text')
    for result in result_find:
        array_anekdots.append(result.getText().strip())
    return array_anekdots[0]



def send_help(chat_id):
    global bot
    bot.send_message(chat_id, text="Шо, помощь нужна?")
    key1 = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton(text="Напиши автору пару ласковых", url="https://vk.com/drzvin")
    key1.add(btn1)
    img = open("Фотка.JPG", "rb")
    bot.send_photo(chat_id, img, reply_markup=key1)

    bot.send_message(chat_id, "Активные пользователи бота-выдрочки:")
    for el in menuBot.Users.activeUsers:
        bot.send_message(chat_id, menuBot.Users.activeUsers[el].getUserHTML(), parse_mode='HTML')



def get_data():
    req = requests.get("https://yobit.net/api/3/ticker/btc_usd")
    response = req.json()
    sell_price = response["btc_usd"]["sell"]



def send_film(bot, chat_id):
    film = get_randomFilm()
    info_str = f"<b>{film['Наименование']}</b>\n" \
               f"Год: {film['Год']}\n" \
               f"Страна: {film['Страна']}\n" \
               f"Жанр: {film['Жанр']}\n" \
               f"Продолжительность: {film['Продолжительность']}"
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton(text="Трейлер", url=film["Трейлер_url"])
    btn2 = types.InlineKeyboardButton(text="СМОТРЕТЬ онлайн", url=film["фильм_url"])
    markup.add(btn1, btn2)
    bot.send_photo(chat_id, photo=film['Обложка_url'], caption=info_str, parse_mode='HTML', reply_markup=markup)



def get_randomFilm():
    url = 'https://randomfilm.ru/'
    infoFilm = {}
    req_film = requests.get(url)
    soup = bs4.BeautifulSoup(req_film.text, "html.parser")
    result_find = soup.find('div', align="center", style="width: 100%")
    infoFilm["Наименование"] = result_find.find("h2").getText()
    names = infoFilm["Наименование"].split(" / ")
    infoFilm["Наименование_rus"] = names[0].strip()
    if len(names) > 1:
        infoFilm["Наименование_eng"] = names[1].strip()

    images = []
    for img in result_find.findAll('img'):
        images.append(url + img.get('src'))
    infoFilm["Обложка_url"] = images[0]

    details = result_find.findAll('td')
    infoFilm["Год"] = details[0].contents[1].strip()
    infoFilm["Страна"] = details[1].contents[1].strip()
    infoFilm["Жанр"] = details[2].contents[1].strip()
    infoFilm["Продолжительность"] = details[3].contents[1].strip()
    infoFilm["Режиссёр"] = details[4].contents[1].strip()
    infoFilm["Актёры"] = details[5].contents[1].strip()
    infoFilm["Трейлер_url"] = url + details[6].contents[0]["href"]
    infoFilm["фильм_url"] = url + details[7].contents[0]["href"]

    return infoFilm



storage = dict()

def init_storage(user_id):
    storage[user_id] = dict(attempt=None, random_digit=None)

def set_data_storage(user_id, key, value):
    storage[user_id][key] = value

def get_data_storage(user_id):
    return storage[user_id]


def digitgames(message):
    init_storage(message.chat.id)

    attempt = 5
    set_data_storage(message.chat.id, "attempt", attempt)

    bot.send_message(message.chat.id, f'Игра "угадай число"!\nКоличество попыток: {attempt}')

    random_digit = random.randint(1, 10)

    set_data_storage(message.chat.id, "random_digit", random_digit)

    bot.send_message(message.chat.id, 'Готово! Загадано число от 1 до 10!')
    bot.send_message(message.chat.id, 'Ну давай, введи число, попробуй угадай;)')
    bot.register_next_step_handler(message, process_digit_step)


def process_digit_step(message):
    chat_id = message.chat.id
    user_digit = message.text

    if not user_digit.isdigit():
        msg = bot.reply_to(message, 'Ты ввел не цифры. Вводи только цифры!')
        bot.register_next_step_handler(msg, process_digit_step)
        return

    attempt = get_data_storage(chat_id)["attempt"]
    random_digit = get_data_storage(chat_id)["random_digit"]

    if int(user_digit) == random_digit:
        bot.send_sticker(chat_id, "CAACAgIAAxkBAAEE5btimROuB5eos0VdeyZn2J5RXUg_WAAC-AsAAqydAAFIkwFAkULAXYYkBA")
        bot.send_message(chat_id, f'Ура! Ты угадал число! Это была цифра {random_digit}')
        init_storage(chat_id)
        return
    elif attempt > 1:
        attempt -= 1
        set_data_storage(chat_id, "attempt", attempt)
        bot.send_message(chat_id, f'Неверно, осталось попыток: {attempt}')
        bot.register_next_step_handler(message, process_digit_step)
    else:
        bot.send_message(chat_id, 'Твои попытки закончились, ты проиграл!')
        init_storage(chat_id)
        return
# ----------------------------------------------------------------------------------------------------------------------
bot.polling(none_stop=True, interval=0)



# choice = random.choice(['Камень', 'Ножницы', 'Бумага'])
# if ms_text == choice:
#     bot.send_message(chat_id, 'Ничья, у меня тоже', {choice})
# else:
#     if ms_text == 'Камень':
#         if choice == 'Ножницы':
#             bot.send_message(chat_id, 'Ты победил, у меня ', {choise})
#         else:
#             bot.send_message(chat_id, 'Ты проиграл, у меня ', {choise})
#     elif ms_text == 'Ножницы':
#         if choice == 'Бумага':
#             bot.send_message(chat_id, 'Ты победил, у меня ', {choise})
#         else:
#             bot.send_message(chat_id, 'Ты проиграл, у меня ', {choise})
#     elif ms_text == 'Бумага':
#         if choice == 'Камень':
#             bot.send_message(chat_id, 'Ты победил, у меня ', {choise})
#         else:
#             bot.send_message(chat_id, 'Ты проиграл, у меня ', {choise})