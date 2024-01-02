from aiogram import types


def make_main_menu_kb():
    kb = [
        [types.KeyboardButton(text="History")],
        [types.KeyboardButton(text="Stats")],
        [types.KeyboardButton(text="Instructions")],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
    )
    return keyboard
