from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu=ReplyKeyboardMarkup([
    [
        KeyboardButton(text='Monday'), KeyboardButton(text='Tuesday')
    ],[
        KeyboardButton(text='Wednesday'), KeyboardButton(text='Thursday')
    ], [
        KeyboardButton(text='Friday'),  KeyboardButton(text='Saturday')

    ],[
        KeyboardButton(text='Sunday'),  KeyboardButton(text='Week'),
    ],[
            KeyboardButton(text='Change timetable')
         ]

],resize_keyboard=True

)
day_change_timetable = ReplyKeyboardMarkup([
[
        KeyboardButton(text='Monday'), KeyboardButton(text='Tuesday')
    ],[
        KeyboardButton(text='Wednesday'), KeyboardButton(text='Thursday')
    ], [
        KeyboardButton(text='Friday'),  KeyboardButton(text='Saturday')

    ],[
        KeyboardButton(text='Sunday')
    ]
],resize_keyboard=True)