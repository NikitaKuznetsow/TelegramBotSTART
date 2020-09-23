from aiogram import types
from data.gooogl import chech_table
from loader import dp
import datetime
import time
values = chech_table()
@dp.message_handler(text='Обновить')
async def update_board(message: types.Message):
    global values
    values = chech_table()
    await message.answer('Расписание обновлено')

@dp.message_handler(text='Today')
async def bot_echo(message: types.Message):
    stroka = ''
    number_week_day = datetime.datetime.today().isoweekday()
    for elem in values['values'][number_week_day - 1][1:]:
        stroka += elem + '\n'
    await message.answer(f'Today is ' + values['values'][number_week_day - 1][0] + ', Nikita!' + '\n')
    time.sleep(0.5)
    await message.answer(f'Your plan for today is:')
    await message.answer(stroka)


@dp.message_handler(text=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])
async def days_week(message: types.Message):
    all_day = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    number_day = all_day.index(message.text)
    all_day_gramm = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    stroka_del = ''
    for elem in values['values'][number_day][1:]:
        stroka_del += elem + '\n'
    await message.answer(f'Your plan for ' + all_day_gramm[number_day] + ' is:')
    time.sleep(0.5)
    await message.answer(stroka_del)


@dp.message_handler(text='Week')
async def week(message: types.Message):
    all_days = ''
    for i in range(7):
        time.sleep(0.5)
        for elem in values['values'][i]:
            all_days += elem + '\n'

        await message.answer(all_days)
        all_days = ''
