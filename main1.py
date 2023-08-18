from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.web_app_info import WebAppInfo

bot = Bot('6364600037:AAFjP3bBeOntNn72ScFRjIL1IRL8rEtILa8')
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    markup = types.ReplyKeyboardMarkup()
    markup.add(types.KeyboardButton('Записаться!', web_app=WebAppInfo(url='https://salon1c.ru/widget-org/812444535')))
    await message.answer('Приветствуем в нашем барбершопе!', reply_markup=markup)

executor.start_polling(dp)
