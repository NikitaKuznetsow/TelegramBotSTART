from loader import dp

from aiogram import types

from aiogram.dispatcher.filters import Command


from keyboards.default import menu

@dp.message_handler(text='Расписание')
async def show_menu(message: types.Message):
    await message.answer('Выбери день для просмотра твоего раписания!', reply_markup=menu)

