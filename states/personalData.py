from aiogram.dispatcher.filters.state import StatesGroup, State

class PersonalData(StatesGroup):
    fullName = State()
    phoneNum = State() 
    question = State() 
