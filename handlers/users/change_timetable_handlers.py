from loader import dp
from aiogram import types
from states import Test
from keyboards.default import day_change_timetable


@dp.message_handler(text='Change timetable')
async def choice_day(message: types.Message):
    await message.answer('Choice a day to change the timetable',reply_markup=day_change_timetable)
    await Test.Q1.set()


@dp.message_handler(text=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'],state=Test.Q1)
async def choice_is_made(message: types.Message):
    await message.answer('Вы выбрали день ')