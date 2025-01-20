from aiogram import Router, Bot
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, PollAnswer

from math_course.entities.quiz import QUIZZES, Question
from math_course.keyboards.callback import QuizCb
from math_course.states import QuizState

quiz_router = Router()


async def _send_poll(bot: Bot, chat_id: int | str, question: Question) -> None:
    await bot.send_poll(
        chat_id=chat_id,
        type="quiz",
        question=question.text,
        options=[
            answer.text
            for answer in question.answers
        ],
        correct_option_id=question.correct_answer_index,
        is_anonymous=False,
    )


@quiz_router.callback_query(QuizCb.filter())
async def start_test(
        query: CallbackQuery,
        callback_data: QuizCb,
        state: FSMContext,
) -> None:
    quiz_id = callback_data.quiz_id

    await query.message.delete_reply_markup()
    await state.set_state(QuizState.waiting_for_answer)
    await state.update_data(
        quiz_id=quiz_id,
        question_index=0,
        correct_answers=0,
    )

    question = QUIZZES[quiz_id].questions[0]
    await _send_poll(query.bot, query.from_user.id, question)


@quiz_router.poll_answer()
async def check_answer(
        poll_answer: PollAnswer,
        state: FSMContext,
        bot: Bot,
) -> None:
    data = await state.get_data()
    quiz_id = data["quiz_id"]
    question_index = data["question_index"]
    correct_answers = data["correct_answers"]

    quiz = QUIZZES[quiz_id]
    question = quiz.questions[question_index]

    if poll_answer.option_ids[0] == question.correct_answer_index:
        correct_answers += 1

    question_index += 1
    if question_index == len(quiz.questions):
        await state.clear()
        await quiz.callback(poll_answer, correct_answers == len(quiz.questions))
        return

    await state.update_data(
        question_index=question_index,
        correct_answers=correct_answers,
    )

    question = quiz.questions[question_index]
    await _send_poll(bot, poll_answer.user.id, question)