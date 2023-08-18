
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.web_app_info import WebAppInfo
bot = Bot('6328102875:AAEV8V21UUzlqAei24Fsy7LTtRxYKbKlcVA')
dp = Dispatcher(bot)
@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    markup = types.ReplyKeyboardMarkup()
    markup.add(types.KeyboardButton('Записаться на Сокол', web_app=WebAppInfo(url='https://b399707.yclients.com/company/379257/menu?o='))) 
    markup.add(types.KeyboardButton('Записаться на Курскую', web_app=WebAppInfo(url='https://b399707.yclients.com/company/33760/menu?o=')))
    await message.answer('Добро пожаловать в барбершоп СЕМЬ!', reply_markup=markup)


executor.start_polling(dp)
