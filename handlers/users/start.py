from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp
from keyboards.default import timetable


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f'Hello'
                         f' {message.from_user.full_name}!' + ' Click on the button to get started',reply_markup=timetable)

