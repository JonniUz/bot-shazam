from aiogram import types
from aiogram.dispatcher.filters import Command

from keyboards.default.menuKeyboard import menu, lct
from loader import dp


@dp.message_handler(Command('bozor'))
async def bot_start(message: types.Message):
    photo_1 = 'https://lh5.googleusercontent.com/p/AF1QipNVkwcE8kGRzUm4E8mhJYWIzvvpGH2_pmTxlZ0u=w408-h544-k-no'
    msg = 'Evos fast food'
    await message.reply_photo(photo_1, caption=msg, reply_markup=menu)


@dp.message_handler(text='Yaqin do\'konlarni qidirish')
async def bot_start(message: types.Message):
    await message.answer('Lokatsiyani yuboring: ', reply_markup=lct)



