import asyncio
import os
from aiogram import Bot, Dispatcher, types
from aiogram.enums import ParseMode
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from aiogram.filters import Command
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("TELEGRAM_TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start(message: Message):
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="⭐ 50 звёзд")],
            [KeyboardButton(text="⭐ 100 звёзд")],
            [KeyboardButton(text="⭐ 200 звёзд")]
        ],
        resize_keyboard=True
    )
    await message.answer(
        "👋 Привет! Добро пожаловать в наш Telegram Stars бот!\n"
        "Мы продаём звёзды по самым низким ценам!\n"
        "Выберите нужное количество 👇",
        reply_markup=keyboard
    )

@dp.message()
async def process_selection(message: Message):
    text = message.text.strip()

    if text.startswith("⭐"):
        try:
            count = int(text.split()[1])
            price = round(count * 1.8 + 5)
            await message.answer(
                f"✅ Вы выбрали: {count} звёзд\n"
                f"💸 Цена: {price}₽\n"
                f"(Plati.Market: 1.8₽ × {count} + 5₽ комиссия)\n\n"
                "🔁 Оплатите через СБП (ВТБ) на номер:\n"
                "<b>+8 950 039 3214</b>\n\n"
                "📝 После оплаты, отправьте сообщение: <b>ОПЛАЧЕНО ✅</b>",
                parse_mode="HTML"
            )
        except Exception:
            await message.answer("❌ Ошибка при обработке количества звёзд.")

    elif text == "ОПЛАЧЕНО ✅":
        await message.answer(
            "📸 Пожалуйста, отправьте скриншот оплаты.\n\n"
            "После этого напишите в Telegram: @wellbinuk и отправьте туда:\n\n"
            "<pre>\nИНФО ОТ БОТА\nКоличество звёзд: [УКАЗАТЬ]\nСайт: Plati.Market\n</pre>",
            parse_mode="HTML"
        )

    elif message.photo:
        await message.answer(
            "✅ Спасибо! Ваш заказ скоро будет обработан.\n"
            "Ожидайте ответа от @wellbinuk."
        )
    else:
        await message.answer("❓ Пожалуйста, выберите количество звёзд или следуйте инструкциям.")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
