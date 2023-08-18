from telegram import ReplyKeyboardMarkup, Update

from telegram.ext import Updater, CommandHandler, MessageHandler, filters, CallbackContext, ConversationHandler


# Состояния для конечного автомата

MENU, ORDER, PRICE, PAYMENT, TIMING, WORKING_HOURS = range(6)


# Обработчик команды /start

def start(update: Update, context: CallbackContext) -> int:

    user = update.message.from_user

    update.message.reply_text(

        f"Привет, {user.first_name}! Я БИМ чат-бот, ваш помощник в оформлении заказа на видеопослание от ведущих БИМ-радио. "

        "Чтобы вы смогли легко во всем разобраться - жмите на кнопку: 'Хочу разобраться'",

        reply_markup=ReplyKeyboardMarkup([['Хочу разобраться']], one_time_keyboard=True),

    )

    return MENU


def show_menu(update: Update, context: CallbackContext) -> int:

    update.message.reply_text(

        "Выберите действие из меню:",

        reply_markup=ReplyKeyboardMarkup([['Заказать услугу', 'Цена'], ['Как оплатить', 'Сроки изготовления заказа'], ['Время приема заказов']]),

    )

    return MENU


def show_price(update: Update, context: CallbackContext) -> int:

    update.message.reply_text(

        "Стоимость видеопослания: 2900 руб. Вы можете вернуться в главное меню или перейти к оформлению заказа.",

        reply_markup=ReplyKeyboardMarkup([['Вернуться в гл. меню', 'Заказать услугу']]),

    )

    return PRICE


def how_to_pay(update: Update, context: CallbackContext) -> int:

    update.message.reply_text(

        "С вами свяжется наш оператор, который вышлет QR-код или ссылку на оплату на ваш мессенджер. "

        "После получения оплаты - он подтвердит прием заказа в работу.",

        reply_markup=ReplyKeyboardMarkup([['Вернуться в гл. меню', 'Заказать услугу']]),

    )

    return PAYMENT


def show_timing(update: Update, context: CallbackContext) -> int:

    update.message.reply_text(

        "Заказ будет готов в течение 24 часов с момента подтверждения оплаты. В выходные и праздничные дни заказы не принимаются. "

        "Если заказ совершается в пятницу или перед/во время выходных, то видеопослание будет готово вечером следующего рабочего дня.",

        reply_markup=ReplyKeyboardMarkup([['Вернуться в гл. меню', 'Заказать услугу']]),

    )

    return TIMING


def show_working_hours(update: Update, context: CallbackContext) -> int:

    update.message.reply_text(

        "Режим работы оператора, который подтвердит прием заказа в работу: с понедельника по пятницу с 9.00 до 17.00, кроме праздничных дней.",

        reply_markup=ReplyKeyboardMarkup([['Вернуться в гл. меню', 'Заказать услугу']]),

    )

    return WORKING_HOURS


def cancel(update: Update, context: CallbackContext) -> int:

    update.message.reply_text("Вы вернулись в главное меню.", reply_markup=ReplyKeyboardMarkup([['Заказать услугу', 'Цена'], ['Как оплатить', 'Сроки изготовления заказа'], ['Время приема заказов']]))

    return MENU


def main():

    # Замените "YOUR_BOT_TOKEN" на токен вашего бота

    updater = Updater(token="6621567054:AAGI9I4yS36Ma1vMCe-YjUmJda701HiD10c", use_context=True)

    dispatcher = updater.dispatcher


    conv_handler = ConversationHandler(

        entry_points=[MessageHandler(Filters.text & ~Filters.command, start)],

        states={

            MENU: [MessageHandler(Filters.regex('^Хочу разобраться$'), show_menu)],

            PRICE: [MessageHandler(Filters.regex('^Цена$'), show_price), MessageHandler(Filters.regex('^Заказать услугу$'), cancel)],

            PAYMENT: [MessageHandler(Filters.regex('^Как оплатить$'), how_to_pay), MessageHandler(Filters.regex('^Вернуться в гл. меню$'), cancel), MessageHandler(Filters.regex('^Заказать услугу$'), cancel)],

            TIMING: [MessageHandler(Filters.regex('^Сроки изготовления заказа$'), show_timing), MessageHandler(Filters.regex('^Вернуться в гл. меню$'), cancel), MessageHandler(Filters.regex('^Заказать услугу$'), cancel)],

            WORKING_HOURS: [MessageHandler(Filters.regex('^Время приема заказов$'), show_working_hours), MessageHandler(Filters.regex('^Вернуться в гл. меню$'), cancel), MessageHandler(Filters.regex('^Заказать услугу$'), cancel)]

        },

        fallbacks=[]

    )


    dispatcher.add_handler(CommandHandler("start", start))

    dispatcher.add_handler(conv_handler)


    updater.start_polling()

    updater.idle()


if __name__ == '__main__':

    main()

