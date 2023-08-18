import telebot

import requests

from telebot import types

from datetime import datetime


# Создаем объект бота и передаем ему токен

bot = telebot.TeleBot("6621567054:AAGI9I4yS36Ma1vMCe-YjUmJda701HiD10c")


# Airtable API ключ и ID таблицы

AIRTABLE_API_KEY = "YOUR_AIRTABLE_API_KEY"

AIRTABLE_BASE_ID = "YOUR_AIRTABLE_BASE_ID"

AIRTABLE_TABLE_NAME = "YOUR_AIRTABLE_TABLE_NAME"


# Состояния для конечного автомата

MENU, ORDER, NAME, EMAIL, RECIPIENT_NAME, OCCASION, MESSAGE, MOOD, STYLE, THANKS = range(10)


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

        save_data = {"user_id": user_id, "option": "Заказать услугу", "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

        save_to_airtable(save_data)

        bot.send_message(message.chat.id,

                         "Видеопослание от ведущих БИМ-радио - это качественная и неповторимая импровизация. "

                         "Заполните форму заказа, и получите 100% креативный уникальный продукт! Оплата совершается по QR-коду или ссылке, высланной Вам нашим оператором. "

                         "Готовность заказа - через 24 ч. с момента подтверждения оплаты. В выходные и праздничные дни заказы не принимаются. "

                         "Режим работы оператора: пн-пт с 9.00 до 18.00\n\n"

                         "Напишите Ваше имя (именно так оно прозвучит в видеопослании, если не хотите раскрывать свое имя - назовитесь анонимом/незнакомцем/незнакомкой/и т.п.)")

        bot.register_next_step_handler(message, process_name_input)

    elif message.text == 'Цена':

        user_id = message.from_user.id

        save_data = {"user_id": user_id, "option": "Цена", "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

        save_to_airtable(save_data)

        bot.send_message(message.chat.id, "Стоимость видеопослания: 2900 руб. Вы можете вернуться в главное меню или перейти к оформлению заказа.",

                         reply_markup=types.ReplyKeyboardMarkup(resize_keyboard=True).add(types.KeyboardButton('Вернуться в гл. меню'), types.KeyboardButton('Заказать услугу')))

    # Добавьте обработку остальных вариантов


def process_name_input(message):

    user_id = message.from_user.id

    save_data = {"user_id": user_id, "option": "Name", "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "value": message.text}

    save_to_airtable(save_data)

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    markup.add(types.KeyboardButton('Продолжить'), types.KeyboardButton('Вернуться на предыдущий шаг'))

    bot.send_message(message.chat.id, "Напишите свой е-мейл, если хотите получить видеопослание в HD качестве:", reply_markup=markup)

    bot.register_next_step_handler(message, process_email_input)


def process_email_input(message):

    user_id = message.from_user.id

    save_data = {"user_id": user_id, "option": "Email", "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "value": message.text}

    save_to_airtable(save_data)

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    markup.add(types.KeyboardButton('Продолжить'), types.KeyboardButton('Пропустить'), types.KeyboardButton('Вернуться на предыдущий шаг'))

    bot.send_message(message.chat.id, "Напишите имя получателя видеопривета (именно так оно прозвучит в видеопослании):", reply_markup=markup)

    bot.register_next_step_handler(message, process_recipient_name_input)


def process_recipient_name_input(message):

    user_id = message.from_user.id

    save_data = {"user_id": user_id, "option": "Recipient Name", "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "value": message.text}

    save_to_airtable(save_data)

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    markup.add(types.KeyboardButton('Продолжить'), types.KeyboardButton('Вернуться на предыдущий шаг'))

    bot.send_message(message.chat.id,

                     "Опишите событие или повод, который должен быть обыгран ведущими:\n"

                     "⦁ Свадьба\n⦁ День рождения\n⦁ Приглашение на свидание\n⦁ Признание в любви\n⦁ Попросить прощения, извиниться\n"

                     "⦁ Пожелать доброго утра\n⦁ Пожелать спокойной ночи\n⦁ Сказать, что соскучился/ась\n⦁ Пожелать удачи\n"

                     "⦁ Сделать комплимент\n⦁ Смотивировать ребенка на учебу\n⦁ Поддержать\n⦁ Свой вариант", reply_markup=markup)

    bot.register_next_step_handler(message, process_occasion_input)


# Добавьте обработчики для остальных шагов (Описание, Настроение, Стили, Благодарность)


# Обработчик для сохранения ответов в Airtable

def save_to_airtable(data):

    headers = {

        "Authorization": f"Bearer {AIRTABLE_API_KEY}",

        "Content-Type": "application/json"

    }

    url = f"https://api.airtable.com/v0/{AIRTABLE_BASE_ID}/{AIRTABLE_TABLE_NAME}"

    payload = {

        "fields": {

            "User ID": data["user_id"],

            "Option Selected": data["option"],

            "Timestamp": data["timestamp"],

            "Value": data.get("value", "")

        }

    }

    response = requests.post(url, headers=headers, json=payload)

    if response.status_code == 200:

        print("Data saved to Airtable successfully")

    else:

        print("Failed to save data to Airtable")


if __name__ == '__main__':

    bot.polling(none_stop=True)

