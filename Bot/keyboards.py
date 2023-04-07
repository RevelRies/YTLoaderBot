import asyncio

from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

async def main_menu():
    keyboard = [
        [KeyboardButton(text='Загрузить с YouTube')]
    ]

    markup = ReplyKeyboardMarkup(keyboard=keyboard,
                                 resize_keyboard=True,
                                 one_time_keyboard=True)
    return markup


