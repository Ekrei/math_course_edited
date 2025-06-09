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
    await message.answer(
        text=(
            "<b>👋 Добро пожаловать в курс по геометрии!</b>\n\n"
            "Я помогу вам освоить геометрию и подготовиться к экзаменам.\n"
            "Выберите действие в меню ниже:"
        ),
        reply_markup=inline.get_main_menu_keyboard()
    )

@flow_router.message()
async def handle_any_message(message: Message):
    await message.answer(
        text=(
            "👋 Для начала работы с ботом, пожалуйста, используйте команду /start\n\n"
            "Эта команда откроет главное меню, где вы сможете:\n"
            "• Начать обучение\n"
            "• Узнать о курсе\n"
            "• Посмотреть структуру курса"
        )
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
    await query.message.answer(
        text="Вы можете вернуться к предыдущим урокам:",
        reply_markup=inline.get_previous_lessons_keyboard(1)
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
    
    if correct:
        await poll_answer.bot.send_message(
            chat_id=poll_answer.user.id,
            text=(
                "<b>Поздравляем! Вы успешно прошли тест по теме параллелограммов!</b>\n\n"
                "Ваше понимание материала на высоком уровне, и это отличный результат.\n\n"
                f"{consts.THIRD_LESSON}"
            ),
            reply_markup=inline.get_third_lesson_keyboard(),
        )
    else:
        await poll_answer.bot.send_message(
            chat_id=poll_answer.user.id,
            text=consts.FAIL_SECOND_TEST,
            reply_markup=inline.get_second_lesson_keyboard(),
        )

@flow_router.callback_query(F.data == "second-lesson-done")
async def second_lesson_done(query: CallbackQuery):
    await query.message.answer(
        text=(
            "<b>Теперь, когда вы посмотрели видео, давайте проверим ваши знания "
            "по теме параллелограммов.</b>\n\n"
            "Пожалуйста, ответьте на следующие вопросы:"
        ),
        reply_markup=inline.get_quiz_keyboard(quiz_id=1),
    )
    await query.message.answer(
        text="Вы можете вернуться к предыдущим урокам:",
        reply_markup=inline.get_previous_lessons_keyboard(2)
    )

async def third_lesson(
        poll_answer: PollAnswer,
        correct: bool,
) -> None:
    bot = cast(Bot, poll_answer.bot)

    await bot.send_chat_action(
        chat_id=poll_answer.user.id,
        action="typing",
    )
    await asyncio.sleep(5)
    
    if correct:
        await poll_answer.bot.send_message(
            chat_id=poll_answer.user.id,
            text=(
                "<b>Поздравляем! Вы успешно прошли тест по теме трапеция!</b>\n\n"
                "Ваше понимание материала на высоком уровне, и это отличный результат.\n\n"
                f"{consts.FOURTH_LESSON}"
            ),
            reply_markup=inline.get_fourth_lesson_keyboard(),
        )
    else:
        await poll_answer.bot.send_message(
            chat_id=poll_answer.user.id,
            text=consts.FAIL_THIRD_TEST,
            reply_markup=inline.get_third_lesson_keyboard(),
        )

async def fourth_lesson(
        poll_answer: PollAnswer,
        correct: bool,
) -> None:
    bot = cast(Bot, poll_answer.bot)

    await bot.send_chat_action(
        chat_id=poll_answer.user.id,
        action="typing",
    )
    await asyncio.sleep(5)
    
    if correct:
        await poll_answer.bot.send_message(
            chat_id=poll_answer.user.id,
            text=(
                "<b>Поздравляем! Вы успешно прошли тест по теме окружность!</b>\n\n"
                "Ваше понимание материала на высоком уровне, и это отличный результат.\n\n"
                f"{consts.FIFTH_LESSON}"
            ),
            reply_markup=inline.get_fifth_lesson_keyboard(),
        )
    else:
        await poll_answer.bot.send_message(
            chat_id=poll_answer.user.id,
            text=consts.FAIL_FOURTH_TEST,
            reply_markup=inline.get_fourth_lesson_keyboard(),
        )

@flow_router.callback_query(F.data == "third-lesson-done")
async def third_lesson_done(query: CallbackQuery):
    await query.message.answer(
        text=(
            "<b>Теперь, когда вы посмотрели видео, давайте проверим ваши знания "
            "по теме трапеция.</b>\n\n"
            "Пожалуйста, ответьте на следующие вопросы:"
        ),
        reply_markup=inline.get_quiz_keyboard(quiz_id=2),
    )
    await query.message.answer(
        text="Вы можете вернуться к предыдущим урокам:",
        reply_markup=inline.get_previous_lessons_keyboard(3)
    )

@flow_router.callback_query(F.data == "fourth-lesson-done")
async def fourth_lesson_done(query: CallbackQuery):
    await query.message.answer(
        text=(
            "<b>Теперь, когда вы посмотрели видео, давайте проверим ваши знания "
            "по теме окружность.</b>\n\n"
            "Пожалуйста, ответьте на следующие вопросы:"
        ),
        reply_markup=inline.get_quiz_keyboard(quiz_id=3),
    )
    await query.message.answer(
        text="Вы можете вернуться к предыдущим урокам:",
        reply_markup=inline.get_previous_lessons_keyboard(4)
    )

@flow_router.callback_query(F.data == "fifth-lesson-done")
async def fifth_lesson_done(query: CallbackQuery):
    await query.message.answer(
        text=consts.SIXTH_LESSON,
        reply_markup=inline.get_quiz_keyboard(quiz_id=2),
    )
    await query.message.answer(
        text="Вы можете вернуться к предыдущим урокам:",
        reply_markup=inline.get_previous_lessons_keyboard(5)
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
        text=(
            "<b>Теперь, когда вы посмотрели видео, давайте проверим ваши знания "
            "по теме стереометрии.</b>\n\n"
            "Пожалуйста, ответьте на следующие вопросы:"
        ),
        reply_markup=inline.get_quiz_keyboard(quiz_id=5),
    )
    await query.message.answer(
        text="Вы можете вернуться к предыдущим урокам:",
        reply_markup=inline.get_previous_lessons_keyboard(6)
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

@flow_router.callback_query(F.data == "start_learning")
async def start_learning(query: CallbackQuery, bot: Bot):
    await query.message.answer(
        text=(
            "<b>👋 Перед началом курса мы проведем небольшой вступительный тест, "
            "чтобы оценить ваши текущие знания по геометрии.</b>\n"
            "Этот тест включает в себя решение заданий и выбор правильного варианта"
            " ответа для каждого вопроса."
        ),
        reply_markup=inline.get_quiz_keyboard(quiz_id=0),
    )

@flow_router.callback_query(F.data == "about_course")
async def about_course(query: CallbackQuery):
    await query.message.answer(
        text=(
            "<b>О курсе:</b>\n\n"
            "Этот курс поможет вам:\n"
            "• Освоить все основные темы геометрии\n"
            "• Научиться решать задачи разной сложности\n"
            "• Подготовиться к экзаменам\n\n"
            "Курс включает в себя:\n"
            "• Теоретический материал\n"
            "• Практические задания\n"
            "• Видео с разбором примеров\n"
            "• Тесты для проверки знаний"
        ),
        reply_markup=inline.get_main_menu_keyboard()
    )

@flow_router.callback_query(F.data == "course_structure")
async def course_structure(query: CallbackQuery):
    await query.message.answer(
        text=(
            "<b>Структура курса:</b>\n\n"
            "1. Треугольники и прямые\n"
            "2. Параллелограммы\n"
            "3. Трапеция\n"
            "4. Окружность\n"
            "5. Векторы\n"
            "6. Стереометрия (параллелепипеды)\n"
            "7. Пирамиды и тетраэдры\n\n"
            "<i>Каждая тема включает в себя:\n"
            "• Теоретический материал\n"
            "• Практические задания\n"
            "• Видео с разбором примеров</i>"
        ),
        reply_markup=inline.get_main_menu_keyboard()
    )

@flow_router.callback_query(F.data.startswith("return_to_lesson_"))
async def return_to_lesson(query: CallbackQuery):
    lesson_number = int(query.data.split("_")[-1])
    
    # Map lesson numbers to their respective texts and keyboards
    lesson_data = {
        1: (consts.FIRST_LESSON, inline.get_first_lesson_keyboard()),
        2: (consts.SECOND_LESSON, inline.get_second_lesson_keyboard()),
        3: (consts.THIRD_LESSON, inline.get_third_lesson_keyboard()),
        4: (consts.FOURTH_LESSON, inline.get_fourth_lesson_keyboard()),
        5: (consts.FIFTH_LESSON, inline.get_fifth_lesson_keyboard()),
        6: (consts.SIXTH_LESSON, inline.get_sixth_lesson_keyboard()),
        7: (consts.SEVENTH_LESSON, inline.get_seventh_lesson_keyboard()),
    }
    
    if lesson_number in lesson_data:
        text, keyboard = lesson_data[lesson_number]
        await query.message.answer(text=text, reply_markup=keyboard)