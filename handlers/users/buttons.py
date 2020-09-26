from loader import dp

from aiogram import types

from aiogram.dispatcher.filters import Command


from keyboards.default import menu

@dp.message_handler(text='Timetable')
async def show_menu(message: types.Message):
    await message.answer('Chose a day to look at timetable!', reply_markup=menu)

