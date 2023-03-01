from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_buttons = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Инструкция"),
            KeyboardButton(text="Услуги и цены")
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=False
)
