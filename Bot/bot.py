import asyncio
import os
import logging

from dotenv import load_dotenv

from aiogram.dispatcher.dispatcher import Dispatcher
from aiogram.client.bot import Bot

load_dotenv()
logging.basicConfig(level=logging.INFO)

dp = Dispatcher()
bot = Bot(os.getenv('TOKEN'))

