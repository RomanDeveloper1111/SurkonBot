from aiogram.dispatcher.filters.state import StatesGroup, State


class StepsFrom(StatesGroup):
    GET_CHOSEN_CITY = State()
    VACANCY_OR_CV = State()

