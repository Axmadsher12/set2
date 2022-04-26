from aiogram.types import KeyboardButton,ReplyKeyboardMarkup

Maktab_darsliklari_8sinf=ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Informatika 📙 8-sinf'),
            KeyboardButton(text="Tarbiya 📙 8-sinf")
        ],
        [
            KeyboardButton(text="Asosiy Menu 🔝"),
            KeyboardButton(text='Orqaga 🔙')
        ]
    ],
    resize_keyboard=True
)