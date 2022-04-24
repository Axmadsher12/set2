from aiogram import types
from keyboards.default.sinf1.Darsliklar import Maktab_darsliklari_1sinf
from keyboards.default.sinf2.Darsliklar import Maktab_darsliklari_2sinf
from keyboards.default.sinf3.Darsliklar import Maktab_darsliklari_3sinf
from keyboards.default.sinf4.Darsliklar import Maktab_darsliklari_4sinf
from keyboards.default.sinf5.Darsliklar import Maktab_darsliklari_5sinf
from keyboards.default.sinflar import Maktab_darsliklari_menu
from loader import dp


@dp.message_handler(text="Asosiy Menu 🔝")
async def bot_echo(message: types.Message):
    await message.answer(text='Nechanchi sinf darsliklari kerak: 🔍',reply_markup=Maktab_darsliklari_menu)




"1-sinf___________________________________________________________________________________"
@dp.message_handler(text="1-sinf 📚 darsliklari")
async def bot_echo(message: types.Message):
    await message.answer(text='Darslikni tanlang:',reply_markup=Maktab_darsliklari_1sinf)

@dp.message_handler(text="Matematika 📙 1-sinf")
async def bot_echo(message: types.Message):
    await message.answer(text='Matematika 📙 1-sinf')
    await message.answer(text="https://t.me/maktabdarslik2022/6?single")

@dp.message_handler(text="Musiqa 📙 1-sinf")
async def bot_echo(message: types.Message):
    await message.answer(text='Musiqa 📙 1-sinf\n')
    await message.answer('https://t.me/maktabdarslik2022/14')

@dp.message_handler(text="Ona tili 📙 1-sinf")
async def bot_echo(message: types.Message):
    await message.answer(text='Ona tili 📙 1-sinf\n')
    await message.answer('https://t.me/maktabdarslik2022/8')

@dp.message_handler(text="Tabiy fanlar 📙 1-sinf")
async def bot_echo(message: types.Message):
    await message.answer(text='Tabiy fanlar 📙 1-sinf\n')
    await message.answer('https://t.me/maktabdarslik2022/15?single')

@dp.message_handler(text="Ingiliz tili 📙 1-sinf")
async def bot_echo(message: types.Message):
    await message.answer(text='Ingiliz tili 📙 1-sinf\n')
    await message.answer('https://t.me/maktabdarslik2022/5')

@dp.message_handler(text="Fransuz tili 📙 1-sinf")
async def bot_echo(message: types.Message):
    await message.answer(text='Fransuz tili 📙 1-sinf\n')
    await message.answer('https://t.me/maktabdarslik2022/4')

@dp.message_handler(text="Nemis tili 📙 1-sinf")
async def bot_echo(message: types.Message):
    await message.answer(text='Nemis tili 📙 1-sinf\n')
    await message.answer('https://t.me/maktabdarslik2022/3')

@dp.message_handler(text="Tarbiya 📙 1-sinf")
async def bot_echo(message: types.Message):
    await message.answer(text='Tarbiya 📙 1-sinf\n')
    await message.answer('https://t.me/maktabdarslik2022/7?single')

@dp.message_handler(text="Tasviriy sanat 📙 1-sinf")
async def bot_echo(message: types.Message):
    await message.answer(text='Tasviriy sanat 📙 1-sinf\n')
    await message.answer('https://t.me/maktabdarslik2022/17?single')

@dp.message_handler(text="Alifbe 📙 1-sinf")
async def bot_echo(message: types.Message):
    await message.answer(text='Alifbe 📙 1-sinf\n')
    await message.answer('https://t.me/maktabdarslik2022/19')

@dp.message_handler(text="Texnologya 📙 1-sinf")
async def bot_echo(message: types.Message):
    await message.answer(text='Texnologya 📙 1-sinf\n')
    await message.answer('https://t.me/maktabdarslik2022/18')

"___________________________________________________________________________________________"




"2-sinf_____________________________________________________________________________________"
@dp.message_handler(text="2-sinf 📚 darsliklari")
async def bot_echo(message: types.Message):
    await message.answer(text='Darslikni tanlang:',reply_markup=Maktab_darsliklari_2sinf)

@dp.message_handler(text="Matematika 📙 2-sinf")
async def bot_echo(message: types.Message):
    await message.answer(text='Matematika 📙 2-sinf')
    await message.answer(text="https://t.me/maktabdarslik2022/35")

@dp.message_handler(text="Musiqa 📙 2-sinf")
async def bot_echo(message: types.Message):
    await message.answer(text='Musiqa 📙 2-sinf\n')
    await message.answer('https://t.me/maktabdarslik2022/27')

@dp.message_handler(text="Ona tili 📙 2-sinf")
async def bot_echo(message: types.Message):
    await message.answer(text='Ona tili 📙 2-sinf\n')
    await message.answer('https://t.me/maktabdarslik2022/29')

@dp.message_handler(text="Tabiy fanlar 📙 2-sinf")
async def bot_echo(message: types.Message):
    await message.answer(text='Tabiy fanlar 📙 2-sinf\n')
    await message.answer('https://t.me/maktabdarslik2022/31')

@dp.message_handler(text="Fransuz tili 📙 2-sinf")
async def bot_echo(message: types.Message):
    await message.answer(text='Fransuz tili 📙 2-sinf\n')
    await message.answer('https://t.me/maktabdarslik2022/33')

@dp.message_handler(text="Rus tili 📙 2-sinf")
async def bot_echo(message: types.Message):
    await message.answer(text='Rus tili 📙 2-sinf\n')
    await message.answer('https://t.me/maktabdarslik2022/34')

@dp.message_handler(text="Tarbiya 📙 2-sinf")
async def bot_echo(message: types.Message):
    await message.answer(text='Tarbiya 📙 2-sinf\n')
    await message.answer('https://t.me/maktabdarslik2022/32')

@dp.message_handler(text="Tasviriy sanat 📙 2-sinf")
async def bot_echo(message: types.Message):
    await message.answer(text='Tasviriy sanat 📙 2-sinf\n')
    await message.answer('https://t.me/maktabdarslik2022/28')

@dp.message_handler(text="Texnologya 📙 2-sinf")
async def bot_echo(message: types.Message):
    await message.answer(text='Texnologya 📙 2-sinf\n')
    await message.answer('https://t.me/maktabdarslik2022/30')

"___________________________________________________________________________________________"




"3-sinf_____________________________________________________________________________________"
@dp.message_handler(text="3-sinf 📚 darsliklari")
async def bot_echo(message: types.Message):
    await message.answer(text='Darslikni tanlang:',reply_markup=Maktab_darsliklari_3sinf)
    await message.answer(text="@kitoblarni_ulashaman_bot")

@dp.message_handler(text="Texnologya 📙 3-sinf")
async def bot_echo(message: types.Message):
    await message.answer(text='Texnologya 📙 3-sinf')
    await message.answer(text="https://t.me/maktabdarslik2022/37?single")

@dp.message_handler(text="Tarbiya 📙 3-sinf")
async def bot_echo(message: types.Message):
    await message.answer(text='Tarbiya 📙 3-sinf')
    await message.answer(text="https://t.me/maktabdarslik2022/38?single")
"___________________________________________________________________________________________"




"4-sinf_____________________________________________________________________________________"
@dp.message_handler(text="4-sinf 📚 darsliklari")
async def bot_echo(message: types.Message):
    await message.answer(text='Darslikni tanlang:',reply_markup=Maktab_darsliklari_4sinf)

@dp.message_handler(text="Matematika 📙 4-sinf")
async def bot_echo(message: types.Message):
    await message.answer(text='Matematika 📙 4-sinf')
    await message.answer(text="https://t.me/maktabdarslik2022/41")

@dp.message_handler(text="Tabiyatshunoslik 📙 4-sinf")
async def bot_echo(message: types.Message):
    await message.answer(text='Tabiyatshunoslik 📙 4-sinf')
    await message.answer(text="https://t.me/maktabdarslik2022/40")

@dp.message_handler(text="Ona tili 📙 4-sinf")
async def bot_echo(message: types.Message):
    await message.answer(text='Ona tili 📙 4-sinf')
    await message.answer(text="https://t.me/maktabdarslik2022/42")

@dp.message_handler(text="Tarbiya 📙 4-sinf")
async def bot_echo(message: types.Message):
    await message.answer(text='Tarbiya 📙 4-sinf')
    await message.answer(text="https://t.me/maktabdarslik2022/43")

@dp.message_handler(text="Texnologya 📙 4-sinf")
async def bot_echo(message: types.Message):
    await message.answer(text='Texnologya 📙 4-sinf')
    await message.answer(text="https://t.me/maktabdarslik2022/44")
"___________________________________________________________________________________________"




"5-sinf_____________________________________________________________________________________"
@dp.message_handler(text="5-sinf 📚 darsliklari")
async def bot_echo(message: types.Message):
    await message.answer(text='Darslikni tanlang:',reply_markup=Maktab_darsliklari_5sinf)

@dp.message_handler(text="Informatika 📙 5-sinf")
async def bot_echo(message: types.Message):
    await message.answer(text='Informatika 📙 5-sinf')
    await message.answer(text="https://t.me/maktabdarslik2022/50")

@dp.message_handler(text="Biologya 📙 5-sinf")
async def bot_echo(message: types.Message):
    await message.answer(text='Biologya 📙 5-sinf')
    await message.answer(text="https://t.me/maktabdarslik2022/47")

@dp.message_handler(text="Ona tili 📙 5-sinf")
async def bot_echo(message: types.Message):
    await message.answer(text='Ona tili 📙 5-sinf')
    await message.answer(text="https://t.me/maktabdarslik2022/46")

@dp.message_handler(text="Geografya 📙 5-sinf")
async def bot_echo(message: types.Message):
    await message.answer(text='Geografya 📙 5-sinf')
    await message.answer(text="https://t.me/maktabdarslik2022/49")

@dp.message_handler(text="Texnologya 📙 5-sinf")
async def bot_echo(message: types.Message):
    await message.answer(text='Texnologya 📙 5-sinf')
    await message.answer(text="https://t.me/maktabdarslik2022/48")
"___________________________________________________________________________________________"




"6-sinf_____________________________________________________________________________________"

"___________________________________________________________________________________________"