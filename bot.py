import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from aiogram.filters import Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram.fsm.storage.memory import MemoryStorage
import config

bot = Bot(token=config.BOT_TOKEN)
dp = Dispatcher(storage=MemoryStorage())

lang = config.LANGUAGE

main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text=config.TEXTS[lang]["button"])]
    ],
    resize_keyboard=True
)

cancel_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text=config.TEXTS[lang]["cancel"])]
    ],
    resize_keyboard=True
)


class LeadForm(StatesGroup):
    name = State()
    phone = State()
    service = State()
    comment = State()


@dp.message(Command("start"))
async def start(message: Message, state: FSMContext):
    await state.clear()
    await message.answer(
        config.TEXTS[lang]["start"],
        reply_markup=main_menu
    )


@dp.message(F.text == config.TEXTS[lang]["button"])
async def start_form(message: Message, state: FSMContext):
    await state.set_state(LeadForm.name)
    await message.answer(
        config.TEXTS[lang]["ask_name"],
        reply_markup=cancel_menu
    )


@dp.message(F.text == config.TEXTS[lang]["cancel"])
async def cancel_form(message: Message, state: FSMContext):
    await state.clear()
    await message.answer(
        f"{config.TEXTS[lang]['cancel_text']}\n\n{config.TEXTS[lang]['restart']}",
        reply_markup=main_menu
    )


@dp.message(LeadForm.name)
async def get_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(LeadForm.phone)
    await message.answer(config.TEXTS[lang]["ask_phone"], reply_markup=cancel_menu)


@dp.message(LeadForm.phone)
async def get_phone(message: Message, state: FSMContext):
    await state.update_data(phone=message.text)
    await state.set_state(LeadForm.service)
    await message.answer(config.TEXTS[lang]["ask_service"], reply_markup=cancel_menu)


@dp.message(LeadForm.service)
async def get_service(message: Message, state: FSMContext):
    await state.update_data(service=message.text)
    await state.set_state(LeadForm.comment)
    await message.answer(config.TEXTS[lang]["ask_comment"], reply_markup=cancel_menu)


@dp.message(LeadForm.comment)
async def get_comment(message: Message, state: FSMContext):
    await state.update_data(comment=message.text)
    data = await state.get_data()

    await bot.send_message(
        config.ADMIN_ID,
        f"📥 Новая заявка\n\n"
        f"Имя: {data['name']}\n"
        f"Телефон: {data['phone']}\n"
        f"Услуга: {data['service']}\n"
        f"Комментарий: {data['comment']}\n\n"
        f"От пользователя: {message.from_user.full_name}\n"
        f"Username: @{message.from_user.username if message.from_user.username else 'no username'}\n"
        f"User ID: {message.from_user.id}"
    )

    await state.clear()
    await message.answer(
        config.TEXTS[lang]["success"],
        reply_markup=main_menu
    )


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
