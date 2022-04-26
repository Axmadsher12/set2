from aiogram.types import KeyboardButton,ReplyKeyboardMarkup

Maktab_darsliklari_10sinf=ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Informatika 📙 10-sinf'),
            KeyboardButton(text="Ona tili 📙 10-sinf")
        ],
        [
            KeyboardButton(text="Asosiy Menu 🔝"),
            KeyboardButton(text='Orqaga 🔙')
        ]
    ],
    resize_keyboard=True
)