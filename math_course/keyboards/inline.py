from dataclasses import asdict

from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

from math_course.entities.video import Video
from math_course.keyboards.callback import QuizCb, VideoCb


def get_quiz_keyboard(quiz_id: int) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.button(
        text="📚 Запустить тест",
        callback_data=QuizCb(quiz_id=quiz_id),
    )
    return builder.as_markup()


def get_first_lesson_keyboard(with_video: bool = True) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.button(
        text="📚 Теория",
        url="https://teletype.in/@bennnnnja/YwFt8IrnWr8",
    )
    builder.button(
        text="📝 Домашнее задание",
        url="https://teletype.in/@bennnnnja/g6P_nZ_I-We",
    )
    if with_video:
        builder.button(
            text="📹 Получить видео",
            callback_data=VideoCb(index=0),
        )
    builder.adjust(1)
    return builder.as_markup()


def get_second_lesson_keyboard() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.button(
        text="📚 Теория",
        url="https://teletype.in/@bennnnnja/qqS8Xj11rp9",
    )
    builder.button(
        text="📝 Домашнее задание",
        url="https://teletype.in/@bennnnnja/5GrP3WNjZWg",
    )
    builder.button(
        text="📹 Получить видео",
        callback_data=VideoCb(index=1),
    )
    builder.adjust(1)
    return builder.as_markup()


def get_third_lesson_keyboard() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.button(
        text="📚 Теория",
        url="https://teletype.in/@bennnnnja/bA4hckGggEL",
    )
    builder.button(
        text="📝 Домашнее задание",
        url="https://teletype.in/@bennnnnja/lilw2wy5VPh",
    )
    builder.button(
        text="📹 Получить видео",
        callback_data=VideoCb(index=2),
    )
    builder.adjust(1)
    return builder.as_markup()


def get_fourth_lesson_keyboard() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.button(
        text="📚 Теория",
        url="https://teletype.in/@bennnnnja/hvt5UA9wgcp",
    )
    builder.button(
        text="📝 Домашнее задание",
        url="https://teletype.in/@bennnnnja/FlG0_F6XAZX",
    )
    builder.button(
        text="✅ Я посмотрел",
        callback_data="fourth-lesson-done",
    )
    builder.adjust(1)
    return builder.as_markup()


def get_fifth_lesson_keyboard() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.button(
        text="📚 Теория",
        url="https://teletype.in/@bennnnnja/a8-onXhJwBd",
    )
    builder.button(
        text="📝 Домашнее задание",
        url="https://teletype.in/@bennnnnja/LV4rK4paKTh",
    )
    builder.button(
        text="📹 Получить видео",
        callback_data=VideoCb(index=3),
    )
    builder.adjust(1)
    return builder.as_markup()


def get_sixth_lesson_keyboard() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.button(
        text="📚 Теория",
        url="https://teletype.in/@bennnnnja/UUVWEfytAhH",
    )
    builder.button(
        text="📝 Домашнее задание",
        url="https://teletype.in/@bennnnnja/hwmJmcNtc9H",
    )
    builder.button(
        text="📹 Получить видео",
        callback_data=VideoCb(index=4),
    )
    builder.adjust(1)
    return builder.as_markup()


def get_seventh_lesson_keyboard() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.button(
        text="📚 Теория",
        url="https://teletype.in/@bennnnnja/WZKQKEqugZH",
    )
    builder.button(
        text="📝 Домашнее задание",
        url="https://teletype.in/@bennnnnja/W9_PLGecd9N",
    )
    builder.button(
        text="📹 Получить видео",
        callback_data=VideoCb(index=5),
    )
    builder.adjust(1)
    return builder.as_markup()


def get_video_keyboard(video: Video) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    for index, url in enumerate(video.urls, start=1):
        builder.button(text=f"Видео №{index}", url=url)
    builder.button(
        **asdict(video.button),
    )
    builder.adjust(1)
    return builder.as_markup()
