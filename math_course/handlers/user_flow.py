import asyncio
from os import getenv
from typing import cast

from aiogram import Router, Bot, F
from aiogram.filters import Command
from aiogram.types import Message, PollAnswer, CallbackQuery, FSInputFile

from math_course import consts
from math_course.entities.video import VIDEOS
from math_course.keyboards.callback import VideoCb
from math_course.keyboards import inline

TOKEN = getenv("BOT_TOKEN")

flow_router = Router()


@flow_router.message(Command("send"))
async def command_send(message: Message):
    await message.answer_video_note(
        video_note=FSInputFile("files/welcome_circle.mp4")
    )

@flow_router.message(Command("start"))
async def command_start(message: Message, bot: Bot):
    await message.answer_video_note(
        video_note=consts.WELCOME_CIRCLE,
    )
    await bot.send_chat_action(
        chat_id=message.chat.id,
        action="typing",
    )
    await asyncio.sleep(25)
    await message.answer(
        text=(
            "<b>👋 Перед началом курса мы проведем небольшой вступительный тест, "
            "чтобы оценить ваши текущие знания по геометрии.</b>\n"
            "Этот тест включает в себя решение заданий и выбор правильного варианта"
            " ответа для каждого вопроса."
        ),
        reply_markup=inline.get_quiz_keyboard(quiz_id=0),
    )

@flow_router.callback_query(VideoCb.filter())
async def send_video(query: CallbackQuery, callback_data: VideoCb):
    index = callback_data.index
    video = VIDEOS[index]
    await query.message.answer(
        text="Видео уже готовы, переходи по ссылкам и изучай материал!",
        reply_markup=inline.get_video_keyboard(video),
    )

async def first_lesson(
        poll_answer: PollAnswer,
        correct: bool,
) -> None:
    bot = cast(Bot, poll_answer.bot)

    await bot.send_chat_action(
        chat_id=poll_answer.user.id,
        action="typing",
    )
    await asyncio.sleep(5)
    await poll_answer.bot.send_message(
        chat_id=poll_answer.user.id,
        text=consts.SUCCESS_FIRST_TEST if correct else consts.FAIL_FIRST_TEST,
        reply_markup=inline.get_first_lesson_keyboard(),
    )



@flow_router.callback_query(F.data == "first-lesson-done")
async def first_lesson_done(query: CallbackQuery):
    await query.message.answer(
        text=consts.SECOND_LESSON,
        reply_markup=inline.get_quiz_keyboard(quiz_id=1),
    )


async def second_lesson(
        poll_answer: PollAnswer,
        correct: bool,
) -> None:
    bot = cast(Bot, poll_answer.bot)

    await bot.send_chat_action(
        chat_id=poll_answer.user.id,
        action="typing",
    )
    await asyncio.sleep(5)
    await poll_answer.bot.send_message(
        chat_id=poll_answer.user.id,
        text=consts.SUCCESS_SECOND_TEST if correct else consts.FAIL_SECOND_TEST,
        reply_markup=inline.get_second_lesson_keyboard(),
    )

@flow_router.callback_query(F.data == "second-lesson-done")
async def second_lesson_done(query: CallbackQuery):
    await query.message.answer(
        text=consts.THIRD_LESSON,
        reply_markup=inline.get_third_lesson_keyboard(),
    )

@flow_router.callback_query(F.data == "third-lesson-done")
async def third_lesson_done(query: CallbackQuery):
    await query.message.answer(
        text=consts.FOURTH_LESSON,
        reply_markup=inline.get_fourth_lesson_keyboard(),
    )

@flow_router.callback_query(F.data == "fourth-lesson-done")
async def fourth_lesson_done(query: CallbackQuery):
    await query.message.answer(
        text=consts.FIFTH_LESSON,
        reply_markup=inline.get_fifth_lesson_keyboard(),
    )

@flow_router.callback_query(F.data == "fifth-lesson-done")
async def fifth_lesson_done(query: CallbackQuery):
    await query.message.answer(
        text=consts.SIXTH_LESSON,
        reply_markup=inline.get_quiz_keyboard(quiz_id=2),
    )

async def sixth_lesson(
        poll_answer: PollAnswer,
        correct: bool,
) -> None:
    bot = cast(Bot, poll_answer.bot)

    await bot.send_chat_action(
        chat_id=poll_answer.user.id,
        action="typing",
    )
    await asyncio.sleep(5)
    await poll_answer.bot.send_message(
        chat_id=poll_answer.user.id,
        text=consts.SUCCESS_THIRD_TEST if correct else consts.FAIL_THIRD_TEST,
        reply_markup=inline.get_sixth_lesson_keyboard(),
    )

@flow_router.callback_query(F.data == "sixth-lesson-done")
async def sixth_lesson_done(query: CallbackQuery):
    await query.message.answer(
        text=consts.SEVENTH_LESSON,
        reply_markup=inline.get_seventh_lesson_keyboard(),
    )

@flow_router.callback_query(F.data == "seventh-lesson-done")
async def seventh_lesson_done(query: CallbackQuery):
    await query.message.answer(
        text=consts.FINAL_TEST,
        reply_markup=inline.get_quiz_keyboard(quiz_id=3),
    )

async def final_test_done(
        poll_answer: PollAnswer,
        _: bool,
) -> None:
    bot = cast(Bot, poll_answer.bot)

    await bot.send_chat_action(
        chat_id=poll_answer.user.id,
        action="typing",
    )
    await asyncio.sleep(5)
    await poll_answer.bot.send_message(
        chat_id=poll_answer.user.id,
        text=consts.FINAL_TEST_DONE,
        reply_markup=inline.get_quiz_keyboard(quiz_id=3),
    )