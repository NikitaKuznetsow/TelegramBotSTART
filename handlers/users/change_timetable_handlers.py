from loader import dp
from aiogram import types
from states import Test
from keyboards.default import day_change_timetable
from data.gooogl import change_table
from aiogram.dispatcher.storage import FSMContext
import re

@dp.message_handler(text='Change timetable')
async def choice_day(message: types.Message):
    await message.answer('Choose a day to change the timetable',reply_markup=day_change_timetable)
    await Test.Q1.set()

day_letters = {'Monday': 'A', 'Tuesday': 'B', 'Wednesday' : 'C', 'Thursday' : 'D', 'Friday' : 'E', 'Saturday' : 'F', 'Sunday' : 'G'}
@dp.message_handler(text=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'],state=Test.Q1)
async def choice_is_made(message: types.Message):
    global day
    day = message.text
    await message.answer('You chose ' + day)
    await message.answer('Enter the cell number')
    await Test.Q2.set()
pattern = r'\d'
@dp.message_handler(state=Test.Q2)
async def choice_is_made(message: types.Message):
    global cell
    cell = str(message.text)
    if re.match(pattern,cell):
        await message.answer('Perfect! I found your cell')
        await message.answer('Send in a reply message what you want to add to this cell')
        await Test.Q3.set()
    else:
        await message.answer('Enter cell number again ')

@dp.message_handler(state=Test.Q3)
async def add_text_to_the_cell(message: types.Message,state: FSMContext):
    task = message.text
    day_letter = day_letters[day]
    change_table(day_letter,cell,task)
    await message.answer('Thanks. Changes are saved')
    await state.finish()




