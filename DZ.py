def dz1(bot, chat_id):
    bot.send_message(chat_id, text=f"Меня зовут Никита")

def dz2(bot, chat_id):
    bot.send_message(chat_id, text=f"Мне 19 лет")

def dz3(bot, chat_id):
    bot.send_message(chat_id, text=f"Никита " * 5)

def dz4(bot, chat_id):
    dz4_ResponseHandler = lambda message: bot.send_message(chat_id, f"Добро пожаловать {message.text}! У тебя красивое имя, в нём {len(message.text)} букв!")
    my_input(bot, chat_id, "Как тебя зовут?", dz4_ResponseHandler)

def dz5(bot, chat_id):
    my_inputInt(bot, chat_id, "Сколько тебе лет?", dz5_ResponseHandler)

def dz5_ResponseHandler(bot, chat_id, age_int):
    bot.send_message(chat_id, text=f"О! тебе уже {age_int}! \nА через год будет уже {age_int+1}!!!")
    if int(age_int) > 50 and int(age_int) < 150:
        bot.send_message(chat_id, text=f'Слушай, да ты уже дедушка, да еще и живой, раз тебе {age_int+1}!')
    if int(age_int) > 1 and int(age_int) < 50:
        bot.send_message(chat_id, text=f'Получается, мой ровестник, да?)')


def dz8(bot, chat_id):
    qwerty = lambda message: bot.send_message(chat_id, "{}\n{}\n{}\n{}".format(message.text.upper(), message.text.lower(),
                                                                               message.text.capitalize(),
                                                                               message.text[0].lower() + message.text[1:].upper()))
    my_input(bot, chat_id, "Как тебя зовут?", qwerty)


def dz7(bot, chat_id):
    mult = lambda x: int(x[0]*int(x[1]))
    addit = lambda x: int(x[0])+int(x[1])
    age_ans = lambda message: bot.send_message(chat_id, "Произведение цифр твоего возраста: {}\nСумма цифр твоего возраста: {}".format(mult(message.text),addit(message.text)))
    my_input(bot, chat_id, "Сколько тебе лет?", age_ans)


def my_input(bot, chat_id, txt, ResponseHandler):
    message = bot.send_message(chat_id, text=txt)
    bot.register_next_step_handler(message, ResponseHandler)

def my_inputInt(bot, chat_id, txt, ResponseHandler):
    message = bot.send_message(chat_id, text=txt)
    bot.register_next_step_handler(message, my_inputInt_SecondPart, botQuestion=bot, txtQuestion=txt, ResponseHandler=ResponseHandler)

def my_inputInt_SecondPart(message, botQuestion, txtQuestion, ResponseHandler):
    chat_id = message.chat.id
    try:
        if message.content_type != "text":
            raise ValueError
        var_int = int(message.text)
        ResponseHandler(botQuestion, chat_id, var_int)
    except ValueError:
        botQuestion.send_message(chat_id,
                         text="Можно вводить ТОЛЬКО целое число в десятичной системе исчисления (символами от 0 до 9)!\nПопробуйте еще раз...")
        my_inputInt(botQuestion, chat_id, txtQuestion, ResponseHandler)


def dz10(bot, chat_id):
    my_inputInt(bot, chat_id, "Сколько будет 2+2*2?", dz10_ResponseHandler)

def dz10_ResponseHandler(bot, chat_id,num_int):
    if num_int == int("6"):
        bot.send_sticker(chat_id, "CAACAgIAAxkBAAEE5btimROuB5eos0VdeyZn2J5RXUg_WAAC-AsAAqydAAFIkwFAkULAXYYkBA")
        bot.send_message(chat_id, text=f"Молодец!\nДействительно, правильный ответ {num_int}!")
    else:
        bot.send_message(chat_id, text=f"Неправильно, ответ не {num_int}!")