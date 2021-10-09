from aiogram import types

from loader import dp


# Echo bot

@dp.message_handler(state=None)
async def bot_echo(message: types.Message):
    res = await search_lyrics(message.text)
    await message.answer(res)
