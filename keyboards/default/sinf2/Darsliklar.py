from aiogram.types import KeyboardButton,ReplyKeyboardMarkup

Maktab_darsliklari_2sinf=ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Matematika 📙 2-sinf'),
            KeyboardButton(text='Musiqa 📙 2-sinf'),
        ],
        [
            KeyboardButton(text='Ona tili 📙 2-sinf'),
            KeyboardButton(text='Tabiy fanlar 📙 2-sinf')
        ],
        [
            KeyboardButton(text='Rus tili 📙 2-sinf'),
            KeyboardButton(text='Fransuz tili 📙 2-sinf')
        ],
        [
            KeyboardButton(text="Texnologya 📙 2-sinf"),
            KeyboardButton(text='Tarbiya 📙 2-sinf')
        ],
        [
            KeyboardButton(text='Tasviriy sanat 📙 2-sinf'),
        ],
        [
            KeyboardButton(text="Asosiy Menu 🔝"),
            KeyboardButton(text='Orqaga 🔙')
        ],
    ],
    resize_keyboard=True
)