from loader import dp
from model import response_prediction

from aiogram import types
from aiogram.types import ContentType

from keyboards import main_buttons
from bot_text import answer_error_text, prices_text, help_text, start_text
from aiogram.dispatcher.filters import Command, Text


# Start command handler
@dp.message_handler(Command("start"))
async def start(message: types.Message):
    await message.answer(start_text, reply_markup=main_buttons)


# Instruction description
@dp.message_handler(Text(equals=["Инструкция"]))
async def help_function(message: types.Message):
    await message.answer(help_text)


# Prices description
@dp.message_handler(Text(equals=["Услуги и цены"]))
async def prices(message: types.Message):
    await message.answer(prices_text)


# Chat handler
@dp.message_handler(content_types=ContentType.TEXT)
async def chat_handling(message: types.message):
    try:
        user_text = message.text
        answer, confidence = response_prediction(user_text)
        if confidence > 0.03:
            await message.answer(answer, reply_markup=main_buttons)

        else:
            await message.answer(answer_error_text, reply_markup=main_buttons)

    except AttributeError:
        print("something went wrong🤯")
