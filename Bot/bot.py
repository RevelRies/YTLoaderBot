import asyncio
import os
import logging
import keyboards
import crud

from dotenv import load_dotenv
from magic_filter import F
from FSMForms import Download

from aiogram.types import FSInputFile
from aiogram.dispatcher.dispatcher import Dispatcher
from aiogram.client.bot import Bot
from aiogram.filters import Command, Text
from aiogram.types import Message
from aiogram.fsm.context import FSMContext


load_dotenv()
logging.basicConfig(level=logging.INFO)

dp = Dispatcher()
bot = Bot(os.getenv('TOKEN'))

@dp.message(Command(commands=['start']))
async def hello_func(message: Message):
    text = 'Этот бот создан чтобы ты мог загружать видео и фото с различных социальных сетей\n' \
           'Выбери откуда ты хочешь загрузить фото/видео'
    markup = await keyboards.main_menu()
    await message.answer(text=text, reply_markup=markup)


# Обработка кнопок главного меню
#-------------------------------------------------------
@dp.message(Text(text='Загрузить с YouTube'))
async def yt_download(message: Message, state: FSMContext):
    # бот ожидает ссылку на файл
    await state.set_state(Download.link)

    text = 'Отправте ссылку на видео'
    await message.answer(text=text)
#-------------------------------------------------------

# Обработка ФСМ состояний
#-------------------------------------------------------
# состояние ожидания ссылки на файл который нужно скачать
@dp.message(Download.link)
async def get_upload_file(message: Message, state: FSMContext):
    url = message.text

    text_wait = 'Скачивание займет некоторое время\n' \
           'Подождите пожалуйста'
    await message.answer(text=text_wait)

    # скачивание видео
    if crud.download_video(url):
        vid = FSInputFile('video.mp4')
        await bot.send_video(chat_id=message.chat.id, video=vid)
        os.remove('video.mp4')
    else:
        text_error = 'При скачивании видео произошла ошибка'
        await message.answer(text=text_error)




async def main() -> None:
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())