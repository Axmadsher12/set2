from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.sinflar import Maktab_darsliklari_menu
from loader import dp
"🖊📋"

@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Maktab darsliklari\n"
                         f"Yangilangan darsliklar PDF\n"
                         f"Nechanchi sinf darsliklari kerak: 🔍\n",reply_markup=Maktab_darsliklari_menu)

