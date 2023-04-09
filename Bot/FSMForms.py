from aiogram.fsm.state import State, StatesGroup

class Download(StatesGroup):
    link = State()
