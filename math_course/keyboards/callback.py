from aiogram.filters.callback_data import CallbackData


class QuizCb(CallbackData, prefix="quiz"):
    quiz_id: int


class VideoCb(CallbackData, prefix="video"):
    index: int
