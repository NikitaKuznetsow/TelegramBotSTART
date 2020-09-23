from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu=ReplyKeyboardMarkup([
    [
        KeyboardButton(text='Monday'), KeyboardButton(text='Tuesday')
    ],[
        KeyboardButton(text='Wednesday'), KeyboardButton(text='Thursday')
    ], [
        KeyboardButton(text='Friday'),  KeyboardButton(text='Saturday')

    ],[
        KeyboardButton(text='Sunday'),  KeyboardButton(text='Week')
    ]
],resize_keyboard=True

)