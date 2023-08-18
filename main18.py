import telebot

import aiogram

from telebot import types

from aiogram.types.web_app_info import WebAppInfo


# Создаем объект бота и передаем ему токен

bot = telebot.TeleBot("6507610313:AAF-hsgN_ds5G3Us7aCMo_3bhw06ufYMW4Q")


# Состояния для конечного автомата

MENU, ORDER, PRICE, PAYMENT, TIMELINE, WORKTIME = range(6)


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

        markup.add(types.KeyboardButton('аЗполнить форму заказа!', web_app=WebAppInfo(url='https://forms.yandex.ru/u/64d4981deb6146039bd57a2f/')))

        bot.send_message(message.chat.id, "Чтобы оформить заказ, заполните форму по ссылке ниже:", reply_markup=markup)

    elif user_choice == 'Цена':

        bot.send_message(message.chat.id, "Стоимость видеопослания 2900 руб.")

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

        markup.add(types.KeyboardButton('Вернуться в гл. меню'), types.KeyboardButton('Заказать услугу'))

        bot.send_message(message.chat.id, "Выберите действие:", reply_markup=markup)

        bot.register_next_step_handler(message, process_price_choice)

    elif user_choice == 'Как оплатить':

        bot.send_message(message.chat.id,

                         "С Вами свяжется наш оператор, который вышлет  QR-код или ссылку на оплату на Ваш мессенджер. После получения оплаты - он подтвердит прием заказа в работу.")

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

        markup.add(types.KeyboardButton('Вернуться в гл. меню'), types.KeyboardButton('Заказать услугу'))

        bot.send_message(message.chat.id, "Выберите действие:", reply_markup=markup)

        bot.register_next_step_handler(message, process_payment_choice)

    elif user_choice == 'Сроки изготовления заказа':

        bot.send_message(message.chat.id,

                         "Заказ будет готов в течение 24 часов с момента подтверждения оплаты. В выходные и праздничные дни заказы не принимаются. Если заказ совершается в пятницу или перед/во время выходных, то видеопослание будет готово вечером следующего рабочего дня.")

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

        markup.add(types.KeyboardButton('Вернуться в гл. меню'), types.KeyboardButton('Заказать услугу'))

        bot.send_message(message.chat.id, "Выберите действие:", reply_markup=markup)

        bot.register_next_step_handler(message, process_timeline_choice)

    elif user_choice == 'Время приема заказов':

        bot.send_message(message.chat.id,

                         "Режим работы оператора, который подтвердит прием заказа в работу: с понедельника по пятницу с 9.00 до 17.00, кроме праздничных дней.")

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

        markup.add(types.KeyboardButton('Вернуться в гл. меню'), types.KeyboardButton('Заказать услугу'))

        bot.send_message(message.chat.id, "Выберите действие:", reply_markup=markup)

        bot.register_next_step_handler(message, process_worktime_choice)


def process_price_choice(message):

    user_choice = message.text

    if user_choice == 'Вернуться в гл. меню':

        show_menu(message)

    elif user_choice == 'Заказать услугу':

        bot.send_message(message.chat.id, "Вы выбрали: Заказать услугу")

        # Добавьте действия для этого пункта меню


def process_payment_choice(message):

    user_choice = message.text

    if user_choice == 'Вернуться в гл. меню':

        show_menu(message)

    elif user_choice == 'Заказать услугу':

        bot.send_message(message.chat.id, "Вы выбрали: Заказать услугу")

        # Добавьте действия для этого пункта меню


def process_timeline_choice(message):

    user_choice = message.text

    if user_choice == 'Вернуться в гл. меню':

        show_menu(message)

    elif user_choice == 'Заказать услугу':

        bot.send_message(message.chat.id, "Вы выбрали: Заказать услугу")

        # Добавьте действия для этого пункта меню


def process_worktime_choice(message):

    user_choice = message.text

    if user_choice == 'Вернуться в гл. меню':

        show_menu(message)

    elif user_choice == 'Заказать услугу':

        bot.send_message(message.chat.id, "Вы выбрали: Заказать услугу")

        # Добавьте действия для этого пункта меню


if __name__ == '__main__':

    bot.polling(none_stop=True)

