import logging

import openai

from telegram import Update

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

from openai import ChatCompletion


# Вставьте ваш токен от OpenAI

OPENAI_API_KEY = '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'


# Вставьте ваш токен, полученный от BotFather

TELEGRAM_BOT_TOKEN = '6592509201:AAFvLop0ivVM2tMYD5kjrDXGi5yebp3gbic'


# Настройки для ChatGPT

openai.api_key = OPENAI_API_KEY

chatgpt = ChatCompletion.create(

    model="gpt-3.5-turbo",

    messages=[

        {"role": "system", "content": "Вы - математический бот, помогающий решать задачи."},

    ]

)


# Включаем логирование

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)


def start(update: Update, context: CallbackContext) -> None:

    update.message.reply_text("Привет! Я математический бот. Отправь мне математическую задачу, и я попробую помочь тебе решить её.")


def help_command(update: Update, context: CallbackContext) -> None:

    update.message.reply_text("Отправь мне математическую задачу, и я попробую помочь тебе решить её.")


def solve_math(update: Update, context: CallbackContext) -> None:

    try:

        user_message = update.message.text


        # Отправляем запрос в ChatGPT

        chat_response = chatgpt.append_message({"role": "user", "content": user_message})

        

        # Получаем ответ от ChatGPT

        bot_response = chat_response.choices[0].message["content"]

        

        update.message.reply_text(bot_response)

    except Exception as e:

        update.message.reply_text("Произошла ошибка при решении задачи. Пожалуйста, убедитесь, что вы ввели задачу верно.")


def main() -> None:

    updater = Updater(TELEGRAM_BOT_TOKEN)

    dispatcher = updater.dispatcher


    dispatcher.add_handler(CommandHandler("start", start))

    dispatcher.add_handler(CommandHandler("help", help_command))

    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, solve_math))


    updater.start_polling()


    updater.idle()


if __name__ == '__main__':

    main()

