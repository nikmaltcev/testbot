import telebot

from telebot import types


# Создаем объект бота и передаем ему токен

bot = telebot.TeleBot("6507610313:AAF-hsgN_ds5G3Us7aCMo_3bhw06ufYMW4Q")


# Состояния для конечного автомата

MENU, ORDER, PRICE, PAYMENT, TIMELINE, WORKTIME, NAME, EMAIL, RECIPIENT_NAME, OCCASION, MESSAGE = range(11)


# Список вариантов для выбора события или повода

OCCASION_OPTIONS = [

    "Свадьба",

    "День рождения",

    "Приглашение на свидание",

    "Признание в любви",

    "Попросить прощения, извиниться",

    "Пожелать доброго утра",

    "Пожелать спокойной ночи",

    "Сказать, что соскучился/ась",

    "Пожелать удачи",

    "Сделать комплимент",

    "Смотивировать ребенка на учебу",

    "Поддержать",

    "Свой вариант"

]


# Обработчик команды /start

@bot.message_handler(commands=['start'])

def start(message):

    user = message.from_user

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    markup.add(types.KeyboardButton('Хочу разобраться'))

    bot.send_message(message.chat.id,

                     f"Привет, {user.first_name}! Я БИМ чат-бот, ваш помощник в оформлении заказа на видеопослание от ведущих БИМ-радио. "

                     "Чтобы вы смогли легко во всем разобраться - жмите на кнопку: 'Хочу разобраться'",

                     reply_markup=markup)

    bot.register_next_step_handler(message, show_menu)


def show_menu(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    markup.add(types.KeyboardButton('Заказать услугу'), types.KeyboardButton('Цена'))

    markup.add(types.KeyboardButton('Как оплатить'), types.KeyboardButton('Сроки изготовления заказа'))

    markup.add(types.KeyboardButton('Время приема заказов'))

    bot.send_message(message.chat.id, "Выберите действие из меню:", reply_markup=markup)

    bot.register_next_step_handler(message, process_menu_choice)


def process_menu_choice(message):

    if message.text == 'Заказать услугу':

        user_id = message.from_user.id

        save_data = {"user_id": user_id, "option": "Заказать услугу"}

        save_to_airtable(save_data)

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

        markup.add(types.KeyboardButton('Ясно, продолжим!'), types.KeyboardButton('Вернуться в главное меню'))

        bot.send_message(message.chat.id,

                         "Видеопослание от ведущих БИМ-радио - это качественная и неповторимая импровизация. "

                         "Заполните форму заказа, и получите 100% креативный уникальный продукт! Оплата совершается по QR-коду или ссылке, высланной Вам нашим оператором. "

                         "Готовность заказа - через 24 ч. с момента подтверждения оплаты. В выходные и праздничные дни заказы не принимаются. "

                         "Режим работы оператора: пн-пт с 9.00 до 18.00",

                         reply_markup=markup)

        bot.register_next_step_handler(message, process_name_input)

    elif message.text == 'Цена':

        user_id = message.from_user.id

        save_data = {"user_id": user_id, "option": "Цена"}

        save_to_airtable(save_data)

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

        markup.add(types.KeyboardButton('Вернуться в гл. меню'), types.KeyboardButton('Заказать услугу'))

        bot.send_message(message.chat.id, "Стоимость видеопослания: 2900 руб. Вы можете вернуться в главное меню или перейти к оформлению заказа.",

                         reply_markup=markup)

    elif message.text == 'Как оплатить':

        user_id = message.from_user.id

        save_data = {"user_id": user_id, "option": "Как оплатить"}

        save_to_airtable(save_data)

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

        markup.add(types.KeyboardButton('Вернуться в гл. меню'), types.KeyboardButton('Заказать услугу'))

        bot.send_message(message.chat.id,

                         "С Вами свяжется наш оператор, который вышлет  QR-код или ссылку на оплату на Ваш мессенджер. После получения оплаты - он подтвердит прием заказа в работу.",

                         reply_markup=markup)

    elif message.text == 'Сроки изготовления заказа':

        user_id = message.from_user.id

        save_data = {"user_id": user_id, "option": "Сроки изготовления заказа"}

        save_to_airtable(save_data)

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

        markup.add(types.KeyboardButton('Вернуться в гл. меню'), types.KeyboardButton('Заказать услугу'))

        bot.send_message(message.chat.id,

                         "Заказ будет готов в течение 24 часов с момента подтверждения оплаты. В выходные и праздничные дни заказы не принимаются. Если заказ совершается в пятницу или перед/во время выходных, то видеопослание будет готово вечером следующего рабочего дня.",

                         reply_markup=markup)

    elif message.text == 'Время приема заказов':

        user_id = message.from_user.id

        save_data = {"user_id": user_id, "option": "Время приема заказов"}

        save_to_airtable(save_data)

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

        markup.add(types.KeyboardButton('Вернуться в гл. меню'), types.KeyboardButton('Заказать услугу'))

        bot.send_message(message.chat.id,

                         "Режим работы оператора, который подтвердит прием заказа в работу: с понедельника по пятницу с 9.00 до 17.00, кроме праздничных дней.",

                         reply_markup=markup)

    else:

        show_menu(message)


def process_name_input(message):

    user_id = message.from_user.id

    save_data = {"user_id": user_id, "option": "Name", "value": message.text}

    save_to_airtable(save_data)

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    markup.add(types.KeyboardButton('Продолжить'), types.KeyboardButton('Вернуться на предыдущий шаг'))

    bot.send_message(message.chat.id, "Напишите свой е-мейл, если хотите получить видеопослание в HD качестве:",

                     reply_markup=markup)

    bot.register_next_step_handler(message, process_email_input)


def process_email_input(message):

    user_id = message.from_user.id

    save_data = {"user_id": user_id, "option": "Email", "value": message.text}

    save_to_airtable(save_data)

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    markup.add(types.KeyboardButton('Продолжить'), types.KeyboardButton('Пропустить'), types.KeyboardButton('Вернуться на предыдущий шаг'))

    bot.send_message(message.chat.id, "Напишите имя получателя видеопривета (именно так оно прозвучит в видеопослании):",

                     reply_markup=markup)

    bot.register_next_step_handler(message, process_recipient_name_input)


def process_recipient_name_input(message):

    user_id = message.from_user.id

    save_data = {"user_id": user_id, "option": "Recipient Name", "value": message.text}

    save_to_airtable(save_data)

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    markup.add(types.KeyboardButton('Продолжить'), types.KeyboardButton('Вернуться на предыдущий шаг'))

    bot.send_message(message.chat.id,

                     "Опишите событие или повод, который должен быть обыгран ведущими (поставьте галочку напротив нужного варианта):")

    for option in OCCASION_OPTIONS:

        markup.add(types.KeyboardButton(option))

    bot.register_next_step_handler(message, process_occasion_input)


def process_occasion_input(message):

    user_id = message.from_user.id

    selected_occasions = []

    for option in OCCASION_OPTIONS:

        if option in message.text:

            selected_occasions.append(option)

    save_data = {"user_id": user_id, "option": "Occasion", "value": ", ".join(selected_occasions)}

    save_to_airtable(save_data)

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    markup.add(types.KeyboardButton('Продолжить'), types.KeyboardButton('Вернуться на предыдущий шаг'))

    bot.send_message(message.chat.id, "Напишите текст:",

                     reply_markup=markup)

    bot.register_next_step_handler(message, process_message_input)


def process_message_input(message):

    user_id = message.from_user.id

    save_data = {"user_id": user_id, "option": "Message", "value": message.text}

    save_to_airtable(save_data)

    bot.send_message(message.chat.id, "Спасибо! Ваш заказ принят.")

    show_menu(message)


# Обработчик для сохранения ответов в Airtable

def save_to_airtable(data):

    # Здесь реализация сохранения в Airtable, как в предыдущем коде

    pass


if __name__ == '__main__':

    bot.polling(none_stop=True)

