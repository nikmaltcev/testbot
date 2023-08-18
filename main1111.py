from aiogram.types import ReplyKeyboardMarkup, KeyboardButton  # pip install aiogram

from aiogram import Dispatcher, Bot, executor, types

from aiogram.types.web_app_info import WebAppInfo

from random import randint, choice

from string import ascii_letters, digits, punctuation


API_TOKEN = "6507610313:AAF-hsgN_ds5G3Us7aCMo_3bhw06ufYMW4Q"


# инициализация ботика...

bot = Bot(token=API_TOKEN)

dispatcher = Dispatcher(bot)


intro_text = "Добро пожаловать в БИМ чат-бот!\n\nЯ помогу вам оформить заказ на видеопосл\ние от ведущих Бим-радио. Пожалуйста, нажмите\

ание от ведущих Бим-радио. Пожалуйста, нажмите кнопку 'Старт' ниже, чтобы начать."

# Создание клавиатуры

date = KeyboardButton ("Сроки изготовления заказа")

price = KeyboardButton('Цена')

how = KeyboardButton("Как оплатить")

time = KeyboardButton("Время приема заказа")

order = KeyboardButton("Заказать услугу")

start_button = KeyboardButton("Хочу разобраться")


main_menu = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False).add(date, order, price, how, time)


btn_order = KeyboardButton('Заказать услугу')

btn_main = KeyboardButton('Вернуться в гл. меню')


other_menu = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False).add(btn_order, btn_main)


@dispatcher.message_handler(commands=['start'])

async def send_welcome(message: types.Message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True).add(start_button)

    await bot.send_message(message.from_user.id,"Привет! Я БИМ чат-бот, Ваш помощник в оформлении заказа на видеопослание от ведущих БИМ-радио. Чтобы Вы смогли легко во всем разобраться - жмите на кнопку.", reply_markup=markup)

    


@dispatcher.message_handler(lambda message: message.text == start_button.text)

async def show_main_menu(message: types.Message):

    await bot.send_message(message.from_user.id, "Выберите пункт меню:", reply_markup=main_menu)



@dispatcher.message_handler()

async def messages(message: types.Message):

    if message.text == 'Как оплатить':

        await bot.send_message(message.from_user.id, f'С Вами свяжется наш оператор, который вышлет  QR-код или ссылку на оплату на Ваш мессенджер. После получения оплаты - он подтвердит прием заказа в работу', reply_markup=other_menu)

    elif message.text == 'Заказать услугу':

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True).add(

            types.KeyboardButton('Ясно, продолжим!', web_app=WebAppInfo(url='https://forms.yandex.ru/u/64d4981deb6146039bd57a2f/')),

            types.KeyboardButton('Вернуться в гл. меню'))

        

        await bot.send_message(message.from_user.id, 'Видеопослание от ведущих БИМ-радио - это качественная и неповторимая импровизация. Заполните форму заказа, и получите 100% креативный уникальный продукт! Оплата совершается по QR-коду или ссылке, высланной Вам нашим оператором. Готовность заказа - через 24 ч. с момента подтверждения оплаты. В выходные и праздничные дни заказы не принимаются. Режим работы оператора: пн-пт с 9.00 до 18.00', reply_markup=markup)

    elif message.text == 'Вернуться в гл. меню':

        await bot.send_message(message.from_user.id, ' Открываю меню...', reply_markup=main_menu)

    

    elif message.text == 'Сроки изготовления заказа':

    

        await bot.send_message(message.from_user.id, f'Заказ будет готов в течение 24 часов с момента подтверждения оплаты. В выходные и праздничные дни заказы не принимаются. Если заказ совершается в пятницу или перед/во время выходных, то видеопослание будет готово вечером следущего рабочего дня.', reply_markup=other_menu)

    elif message.text == 'Заказать услугу':

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True).add(

            types.KeyboardButton('Ясно, продолжим!', web_app=WebAppInfo(url='https://forms.yandex.ru/u/64d4981deb6146039bd57a2f/')),

            types.KeyboardButton('Вернуться в гл. меню'))

        

        await bot.send_message('Видеопослание от ведущих БИМ-радио - это качественная и неповторимая импровизация. Заполните форму заказа, и получите 100% креативный уникальный продукт! Оплата совершается по QR-коду или ссылке, высланной Вам нашим оператором. Готовность заказа - через 24 ч. с момента подтверждения оплаты. В выходные и праздничные дни заказы не принимаются. Режим работы оператора: пн-пт с 9.00 до 18.00', reply_markup=markup)

    elif message.text == 'Вернуться в гл. меню':

        await bot.send_message(message.from_user.id, ' Открываю меню...', reply_markup=main_menu)

    

    elif message.text == 'Цена':


        await bot.send_message(message.from_user.id, 'Стоимость видеопослания 2900 руб.', reply_markup=other_menu)

    elif message.text == 'Заказать услугу':

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True).add(

            types.KeyboardButton('Ясно, продолжим!', web_app=WebAppInfo(url='https://forms.yandex.ru/u/64d4981deb6146039bd57a2f/')),

            types.KeyboardButton('Вернуться в гл. меню'))

    

        await bot.send_message('Видеопослание от ведущих БИМ-радио - это качественная и неповторимая импровизация. Заполните форму заказа, и получите 100% креативный уникальный продукт! Оплата совершается по QR-коду или ссылке, высланной Вам нашим оператором. Готовность заказа - через 24 ч. с момента подтверждения оплаты. В выходные и праздничные дни заказы не принимаются. Режим работы оператора: пн-пт с 9.00 до 18.00', reply_markup=markup)

    elif message.text == 'Вернуться в гл. меню':

        await bot.send_message(message.from_user.id, ' Открываю меню...', reply_markup=main_menu)


    elif message.text == "Время приема заказа":

        await bot.send_message(message.from_user.id, 'Режим работы оператора, который подтвердит прием заказа в работу: с понедельника по пятницу с 9.00 до 17.00, кроме праздничных дней.', reply_markup=other_menu)

    elif message.text == 'Заказать услугу':

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True).add(

            types.KeyboardButton('Ясно, продолжим!', web_app=WebAppInfo(url='https://forms.yandex.ru/u/64d4981deb6146039bd57a2f/')),

            types.KeyboardButton('Вернуться в гл. меню'))

        

        await bot.send_message('Видеопослание от ведущих БИМ-радио - это качественная и неповторимая импровизация. Заполните форму заказа, и получите 100% креативный уникальный продукт! Оплата совершается по QR-коду или ссылке, высланной Вам нашим оператором. Готовность заказа - через 24 ч. с момента подтверждения оплаты. В выходные и праздничные дни заказы не принимаются. Режим работы оператора: пн-пт с 9.00 до 18.00', reply_markup=markup)

    elif message.text == 'Вернуться в гл. меню':

        await bot.send_message(message.from_user.id, ' Открываю меню...', reply_markup=main_menu)


    else:

        await bot.send_message(message.from_user.id, f'Если вы потерялись, нажмите /start')

        



if __name__ == '__main__':

    executor.start_polling(dispatcher, skip_updates=True)
