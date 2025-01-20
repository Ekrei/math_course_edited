from aiogram.fsm.state import State, StatesGroup


class QuizState(StatesGroup):
    """Quiz state."""
    waiting_for_answer = State()