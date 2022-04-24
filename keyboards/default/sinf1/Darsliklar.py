from aiogram.types import KeyboardButton,ReplyKeyboardMarkup

Maktab_darsliklari_1sinf=ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Matematika 📙 1-sinf'),
            KeyboardButton(text='Musiqa 📙 1-sinf'),
        ],
        [
            KeyboardButton(text='Ona tili 📙 1-sinf'),
            KeyboardButton(text='Tabiy fanlar 📙 1-sinf')
        ],
        [
            KeyboardButton(text='Ingiliz tili 📙 1-sinf'),
            KeyboardButton(text='Fransuz tili 📙 1-sinf')
        ],
        [
            KeyboardButton(text="Nemis tili 📙 1-sinf"),
            KeyboardButton(text='Tarbiya 📙 1-sinf')
        ],
        [
            KeyboardButton(text='Tasviriy sanat 📙 1-sinf'),
            KeyboardButton(text='Alifbe 📙 1-sinf')
        ],
        [
            KeyboardButton(text='Texnologya 📙 1-sinf'),
        ],
        [
            KeyboardButton(text="Asosiy Menu 🔝"),
            KeyboardButton(text='Orqaga 🔙')
        ],
    ],
    resize_keyboard=True
)