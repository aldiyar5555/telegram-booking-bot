import os
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from dotenv import load_dotenv

# Загрузка настроек
load_dotenv()
API_TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=API_TOKEN, parse_mode="HTML")
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start_cmd(message: types.Message):
    # Создаем красивое меню с кнопками
    kb = InlineKeyboardMarkup(row_width=1)
    
    # Замени ссылки на свои реальные профили!
    btns = [
        InlineKeyboardButton("📂 Моё Портфолио (GitHub)", url="https://github.com/aldiyar5555"),
        InlineKeyboardButton("💼 Профиль на FL.ru", url="https://www.fl.ru/users/aimbetovab/portfolio/"),
        InlineKeyboardButton("📱 Связаться со мной", url="https://t.me/aldi1k"),
        InlineKeyboardButton("⚡ Узнать стек технологий", callback_data="show_stack")
    ]
    kb.add(*btns)

    welcome_text = (
        f"<b>Привет, я Алдияр!</b> 👋\n\n"
        f"Я Python-разработчик, специализируюсь на создании:\n"
        f"• Telegram ботов любой сложности 🤖\n"
        f"• Парсеров данных 📊\n"
        f"• Автоматизации бизнес-процессов ⚙️\n\n"
        f"Чем я могу вам помочь?"
    )
    
    await message.answer(welcome_text, reply_markup=kb)

@dp.callback_query_handler(lambda c: c.data == 'show_stack')
async def process_callback_stack(callback_query: types.CallbackQuery):
    stack_text = (
        "<b>Мой стек технологий:</b>\n"
        "• 🐍 Python 3.11+\n"
        "• 🤖 Aiogram 2.x / 3.x\n"
        "• 🗄 PostgreSQL / SQLite\n"
        "• 🐳 Docker & CI/CD\n"
        "• ☁️ Linux (Ubuntu/Debian)"
    )
    # Редактируем старое сообщение, добавляя стек
    await bot.edit_message_text(
        chat_id=callback_query.from_user.id,
        message_id=callback_query.message.message_id,
        text=stack_text,
        reply_markup=InlineKeyboardMarkup().add(InlineKeyboardButton("⬅️ Назад", callback_data="back_to_main"))
    )

@dp.callback_query_handler(lambda c: c.data == 'back_to_main')
async def back_to_main(callback_query: types.CallbackQuery):
    # Возвращаем главное меню (вызываем функцию старта)
    await start_cmd(callback_query.message)
    await bot.delete_message(callback_query.from_user.id, callback_query.message.message_id)

if __name__ == "__main__":
    print("Бот-визитка запущен...")
    executor.start_polling(dp, skip_updates=True)