from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Yaqin do'konlarni qidirish")
        ]
    ],
    resize_keyboard=True
)
lct = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🔎", request_location=True)
        ]
    ],
    resize_keyboard=True
)
