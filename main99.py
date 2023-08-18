from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from aiogram import Bot, Dispatcher, types

from aiogram.types.web_app_info import WebAppInfo

import random

import string


API_TOKEN = "6507610313:AAF-hsgN_ds5G3Us7aCMo_3bhw06ufYMW4Q"


bot = Bot(token=API_TOKEN)

dispatcher = Dispatcher(bot)


intro_text = "Добро пожаловать в БИМ чат-бот!\n\nЯ помогу вам оформить заказ на видеопослание от ведущих Бим-радио. Пожалуйста, нажмите кнопку 'Старт' ниже, чтобы начать."


main_menu = ReplyKeyboardMarkup(resize_keyboard=True).add(

    KeyboardButton("Сроки изготовления заказа"),

    KeyboardButton("Цена"),

    KeyboardButton("Как оплатить"),

    KeyboardButton("Время приема заказа"),

    KeyboardButton("Заказать услугу")

)


other_menu = ReplyKeyboardMarkup(resize_keyboard=True).add(

    KeyboardButton('Заказать услугу'),

    KeyboardButton('Вернуться в гл. меню')

)


@dispatcher.message_handler(commands=['start'])

async def start(message: types.Message):

    await bot.send_message(message.from_user.id, f"Привет, {message.from_user.first_name}, я БИМ чат-бот, Ваш помощник...", reply_markup=main_menu)


@dispatcher.message_handler(commands=['help'])

async def help(message: types.Message):

    await bot.send_message(message.from_user.id, intro_text, reply_markup=main_menu)


@dispatcher.message_handler(lambda message: message.text == 'Старт')

async def handle_start(message: types.Message):

    await bot.send_message(message.from_user.id, intro_text, reply_markup=main_menu)


@dispatcher.message_handler()

async def messages(message: types.Message):

    if message.text == 'Как оплатить':

        await bot.send_message(message.from_user.id, f' Рандомное число: {random.randint(0, 100)}')

    elif message.text == 'Сроки изготовления заказа':

        await bot.send_message(message.from_user.id, f'Заказ будет готов в течение 24 часов...', reply_markup=other_menu)

    elif message.text == 'Заказать услугу':

        markup = types.ReplyKeyboardMarkup()

        markup.add(types.KeyboardButton('Продолжить', web_app=WebAppInfo(url='https://forms.yandex.ru/u/64d4981deb6146039bd57a2f/')))

        await bot.send_message(message.from_user.id, 'Нажмите для оформления заказа', reply_markup=markup)

    elif message.text == 'Цена':

        await bot.send_message(message.from_user.id, 'Стоимость видеопослания 2900 руб.', reply_markup=other_menu)

    elif message.text == 'Вернуться в гл. меню':

        await bot.send_message(message.from_user.id, ' Открываю меню...', reply_markup=main_menu)

    else:

        await bot.send_message(message.from_user.id, 'Ботик вас не понял... :(', reply_markup=other_menu)


if __name__ == '__main__':

    from aiogram import executor

    executor.start_polling(dispatcher, skip_updates=True)

