from aiogram.types import KeyboardButton,ReplyKeyboardMarkup

Maktab_darsliklari_5sinf=ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Informatika 📙 5-sinf'),
            KeyboardButton(text='Biologya 📙 5-sinf'),
        ],
        [
            KeyboardButton(text='Ona tili 📙 5-sinf'),
            KeyboardButton(text='Geografya 📙 5-sinf')
        ],
        [
            KeyboardButton(text='Texnologya 📙 5-sinf'),
        ],
        [
            KeyboardButton(text="Asosiy Menu 🔝"),
            KeyboardButton(text='Orqaga 🔙')
        ]
    ],
    resize_keyboard=True
)