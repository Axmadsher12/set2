from aiogram.types import KeyboardButton,ReplyKeyboardMarkup

Maktab_darsliklari_1_sinf=ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Matematika 📚'),
            KeyboardButton(text='Informatika 📚'),
        ],
        [
            KeyboardButton(text='Ona tili 📚'),
            KeyboardButton(text='Biologya 📚')
        ],
        [
            KeyboardButton(text='Ingiliz tili 📚'),
            KeyboardButton(text='Fransuz tili 📚')
        ],
        [
            KeyboardButton(text="Nemis tili 📚")
        ]
    ],
    resize_keyboard=True
)