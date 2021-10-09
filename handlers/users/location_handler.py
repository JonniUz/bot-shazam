from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp
from aiogram.types import ReplyKeyboardRemove

from loader import dp
from utils.misc.get_distance import choose_shortest


@dp.message_handler(content_types='contact')
async def bot_help(message: types.Message):
    contact = message.contact
    if not contact.phone_number.startswith('998'):
        await message.reply(contact)
    else:
        await message.reply('contact')


@dp.message_handler(content_types='location')
async def bot_help(message: types.Message):
    location = message.location
    latitude = location.latitude
    longitude = location.longitude
    closest_shops = choose_shortest(location)

    text = '\n\n'.join([f"<a href='{url}'>{shop_name}</a>\nMasofa: {distance: 1f} km"
                        for shop_name, distance, url, shop_location in closest_shops])

    await message.answer(f"Rahmat. \n"
                         f"Latitude: {latitude}\n"
                         f"Longitude: {longitude}\n\n"
                         f"{text}", disable_web_page_preview=True, reply_markup=ReplyKeyboardRemove())

    for shop_name, distance, url, shop_location in closest_shops:
        await message.answer_location(latitude=shop_location['lat'],
                                      longitude=shop_location['lon'])