import telebot

from telebot import types


# Создаем объект бота и передаем ему токен

bot = telebot.TeleBot("6507610313:AAF-hsgN_ds5G3Us7aCMo_3bhw06ufYMW4Q")


# Состояния для конечного автомата

MENU, ORDER, PRICE, PAYMENT, TIMELINE, WORKTIME, NAME, EMAIL = range(8)


# Обработчик команды /start

@bot.message_handler(commands=['start'])

def start(message):

    user = message.from_user

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    markup.add(types.KeyboardButton('Хочу разобраться'))

    bot.send_message(message.chat.id,

                     f"Привет, {user.first_name}! Я БИМ чат-бот, Ваш помощник в оформлении заказа на видеопослание от ведущих БИМ-радио. "

                     "Чтобы Вы смогли легко во всем разобраться - жмите на кнопку: 'Хочу разобраться'",

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

    user_choice = message.text

    if user_choice == 'Заказать услугу':

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

        markup.add(types.KeyboardButton('Ясно, продолжим!'), types.KeyboardButton('Вернуться в гл. меню'))

        bot.send_message(message.chat.id,

                         "Видеопослание от ведущих БИМ-радио - это качественная и неповторимая импровизация. Заполните форму заказа, и получите 100% креативный уникальный продукт! Оплата совершается по QR-коду или ссылке, высланной Вам нашим оператором. Готовность заказа - через 24 ч. с момента подтверждения оплаты. В выходные и праздничные дни заказы не принимаются. Режим работы оператора: пн-пт с 9.00 до 18.00",

                         reply_markup=markup)

        bot.register_next_step_handler(message, process_order_choice)

    elif user_choice == 'Цена':

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

        markup.add(types.KeyboardButton('Вернуться в гл. меню'), types.KeyboardButton('Заказать услугу'))

        bot.send_message(message.chat.id, "Стоимость видеопослания: 2900 руб.", reply_markup=markup)

    elif user_choice == 'Как оплатить':

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

        markup.add(types.KeyboardButton('Вернуться в гл. меню'), types.KeyboardButton('Заказать услугу'))

        bot.send_message(message.chat.id,

                         "С Вами свяжется наш оператор, который вышлет  QR-код или ссылку на оплату на Ваш мессенджер. После получения оплаты - он подтвердит прием заказа в работу.",

                         reply_markup=markup)

    elif user_choice == 'Сроки изготовления заказа':

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

        markup.add(types.KeyboardButton('Вернуться в гл. меню'), types.KeyboardButton('Заказать услугу'))

        bot.send_message(message.chat.id,

                         "Заказ будет готов в течение 24 часов с момента подтверждения оплаты. В выходные и праздничные дни заказы не принимаются. Если заказ совершается в пятницу или перед/во время выходных, то видеопослание будет готово вечером следующего рабочего дня.",

                         reply_markup=markup)

    elif user_choice == 'Время приема заказов':

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

        markup.add(types.KeyboardButton('Вернуться в гл. меню'), types.KeyboardButton('Заказать услугу'))

        bot.send_message(message.chat.id,

                         "Режим работы оператора, который подтвердит прием заказа в работу: с понедельника по пятницу с 9.00 до 17.00, кроме праздничных дней.",

                         reply_markup=markup)


def process_order_choice(message):

    user_choice = message.text

    if user_choice == 'Ясно, продолжим!':

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

        markup.add(types.KeyboardButton('Продолжить'), types.KeyboardButton('Вернуться на предыдущий шаг'))

        bot.send_message(message.chat.id,

                         "Напишите Ваше имя (именно так оно прозвучит в видеопослании, если не хотите раскрывать свое имя - назовитесь анонимом/незнакомцем/незнакомкой/и т.п.)",

                         reply_markup=markup)

        bot.register_next_step_handler(message, process_name_input)

    elif user_choice == 'Вернуться в гл. меню':

        show_menu(message)

        

def process_name_input(message):

    user_choice = message.text

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    markup.add(types.KeyboardButton('Продолжить'), types.KeyboardButton('Вернуться на предыдущий шаг'), types.KeyboardButton('Пропустить'))

    bot.send_message(message.chat.id, "Напишите свой е-мейл, если хотите получить видеопослание в HD качестве:",

                     reply_markup=markup)

    bot.register_next_step_handler(message, process_email_input)


def process_email_input(message):

    user_choice = message.text

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    markup.add(types.KeyboardButton('Продолжить'), types.KeyboardButton('Вернуться на предыдущий шаг'))

    bot.send_message(message.chat.id,

                     f"Напишите свой е-мейл, если хотите получить видеопослание в HD качестве: {user_choice}",

                     reply_markup=markup)

    bot.register_next_step_handler(message, process_email_input)

    

if __name__ == '__main__':

    bot.polling(none_stop=True)

