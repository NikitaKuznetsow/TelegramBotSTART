from aiogram import types
from data.gooogl import chech_table
from loader import dp
import datetime




@dp.message_handler(commands = 'today')
async def bot_echo(message: types.Message):
    stroka = ''
    number_week_day = datetime.datetime.today().isoweekday()
    values = chech_table()
    for elem in values['values'][number_week_day - 1][1:]:
        stroka += elem +'\n'
    await message.answer(f'Сегодня '+ values['values'][number_week_day - 1][0] + ' хозяин!' + '\n')
    await message.answer(f'Твой список дел на сегодня:')
    await message.answer(stroka)