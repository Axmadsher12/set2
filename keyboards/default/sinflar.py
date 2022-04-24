from aiogram.types import KeyboardButton,ReplyKeyboardMarkup

Maktab_darsliklari_menu=ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='1-sinf 📚 darsliklari'),
            KeyboardButton(text='2-sinf 📚 darsliklari'),
        ],
        [
            KeyboardButton(text='3-sinf 📚 darsliklari'),
            KeyboardButton(text='4-sinf 📚 darsliklari')
        ],
        [
            KeyboardButton(text='5-sinf 📚 darsliklari'),
            KeyboardButton(text='6-sinf 📚 darsliklari')
        ],
        [
            KeyboardButton(text='7-sinf 📚 darsliklari'),
            KeyboardButton(text='8-sinf 📚 darsliklari')
        ],
        [
            KeyboardButton(text='9-sinf 📚 darsliklari'),
            KeyboardButton(text='10-sinf 📚 darsliklari')
        ],
        [
            KeyboardButton(text='11-sinf 📚 darsliklari'),
            #KeyboardButton(text='Sinflar uchun 📚 darsliklar ro\'yxati')
        ]
    ],
    resize_keyboard=True
)