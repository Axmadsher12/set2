from aiogram.types import KeyboardButton,ReplyKeyboardMarkup

Maktab_darsliklari_3sinf=ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Texnologya 📙 3-sinf"),
            KeyboardButton(text='Tarbiya 📙 3-sinf')
        ],
        [
            KeyboardButton(text="Asosiy Menu 🔝"),
            KeyboardButton(text='Orqaga 🔙')
        ]
    ],
    resize_keyboard=True
)