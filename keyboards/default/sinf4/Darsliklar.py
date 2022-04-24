from aiogram.types import KeyboardButton,ReplyKeyboardMarkup

Maktab_darsliklari_4sinf=ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Matematika 📙 4-sinf'),
            KeyboardButton(text='Tabiyatshunoslik 📙 4-sinf'),
        ],
        [
            KeyboardButton(text='Ona tili 📙 4-sinf'),
            KeyboardButton(text='Tarbiya 📙 4-sinf')
        ],
        [
            KeyboardButton(text='Texnologya 📙 4-sinf'),
        ],
        [
            KeyboardButton(text="Asosiy Menu 🔝"),
            KeyboardButton(text='Orqaga 🔙')
        ]
    ],
    resize_keyboard=True
)