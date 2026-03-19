from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

API_TOKEN = "YOUR_TOKEN"

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.reply("Бот работает!")

if __name__ == "__main__":
    print("Бот запущен...")
    executor.start_polling(dp)