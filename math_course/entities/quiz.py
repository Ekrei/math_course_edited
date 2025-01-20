from typing import Awaitable, Callable

from aiogram.types import PollAnswer
from pydantic.dataclasses import dataclass

from math_course.handlers.user_flow import first_lesson, second_lesson, sixth_lesson, \
    final_test_done


@dataclass
class Answer:
    """Answer entity."""

    text: str


@dataclass
class Question:
    """Question entity."""

    text: str
    answers: list[Answer]
    correct_answer_index: int


@dataclass
class Quiz:
    """Quiz entity."""

    questions: list[Question]
    callback: Callable[[PollAnswer, bool], Awaitable[None]] | None = None


QUIZZES = [
    Quiz(
        questions=[
            Question(
                text=(
                    "В прямоугольном треугольнике гипотенуза равна 5, синус одного из "
                    "острых углов равен 24/25.\nНайдите прилежащий к этому углу катет."
                ),
                answers=[
                    Answer(text="1.4"),
                    Answer(text="1.5"),
                    Answer(text="1.2"),
                    Answer(text="1.6"),
                ],
                correct_answer_index=0
            ),
            Question(
                text=(
                    "Даны векторы a(16; -0,4) и b(2;5).\n"
                    "Найдите скалярное произведение a*b"
                ),
                answers=[
                    Answer(text="25"),
                    Answer(text="35"),
                    Answer(text="30"),
                ],
                correct_answer_index=2,
            ),
            Question(
                text=(
                    "Основания равнобедренной трапеции равны 14 и 26, а ее периметр"
                    " равен 60. Найдите площадь трапеции."
                ),
                answers=[
                    Answer(text="140"),
                    Answer(text="150"),
                    Answer(text="160"),
                    Answer(text="170"),
                    Answer(text="180"),
                ],
                correct_answer_index=2,
            ),
        ],
        callback=first_lesson,
    ),
    Quiz(
        questions=[
            Question(
                text="Выберете верное высказывание",
                answers=[
                    Answer(
                        text=(
                            "Биссектриса параллелограмма отсекает от него"
                            " равносторонний треугольник"
                        )
                    ),
                    Answer(
                        text=(
                            "Биссектрисы углов, прилежащих к одной стороне "
                            "параллелограмма пересекаются под острым углом"
                        )
                    ),
                    Answer(
                        text=(
                            "Отрезки биссектрис противоположных углов "
                            "равны и параллельны"
                        )
                    ),
                ],
                correct_answer_index=1
            ),
            Question(
                text=(
                    "Выберете верные формулы площади\n"
                    "а) S = a × b × sinα\n"
                    "б) S = 0,5 × (d1 × d2)"
                ),
                answers=[
                    Answer(text="а"),
                    Answer(text="б"),
                    Answer(text="все верные")
                ],
                correct_answer_index=2
            ),
        ],
        callback=second_lesson,
    ),
    Quiz(
        questions=[
            Question(
                text=(
                    "Выберете верные свойства прямоугольного параллелепипеда"
                ),
                answers=[
                    Answer(
                        text=(
                            "В прямоугольном параллелепипеде 8 граней"
                            " и все они являются прямоугольниками."
                        )
                    ),
                    Answer(
                        text=(
                            "Все двугранные углы прямоугольного "
                            "параллелепипеда – тупые."
                        )
                    ),
                    Answer(text="Диагонали прямоугольного параллелепипеда равны."),
                ],
                correct_answer_index=2
            ),
            Question(
                text=(
                    "Выберете верную формулу объема прямого параллелепипеда"
                ),
                answers=[
                    Answer(text="V = S × h"),
                    Answer(text="V = a × b × h"),
                    Answer(text="V = a^3"),
                ],
                correct_answer_index=0
            ),
            Question(
                text=(
                    "Верно ли высказывание?\n"
                    "Диагональ куба в √3 раз больше его ребра."
                ),
                answers=[
                    Answer(text="верно"),
                    Answer(text="не верно"),
                ],
                correct_answer_index=0
            ),
        ],
        callback=sixth_lesson,
    ),
    Quiz(
        questions=[
            Question(
                text=(
                    "Во сколько раз увеличится объем пирамиды, "
                    "если ее высоту увеличить в четыре раза?"
                ),
                answers=[
                    Answer(text="2"),
                    Answer(text="3"),
                    Answer(text="4"),
                ],
                correct_answer_index=2
            ),
            Question(
                text=(
                    "Ребра прямоугольного параллелепипеда, "
                    "выходящие из одной вершины, равны 1, 2, 3"
                ),
                answers=[
                    Answer(text="20"),
                    Answer(text="22"),
                    Answer(text="24"),
                    Answer(text="26"),
                ],
                correct_answer_index=1
            ),
            Question(
                text=(
                    "Найдите объем пирамиды, вписанной в куб, если ребро куба равно 3"
                ),
                answers=[
                    Answer(text="5"),
                    Answer(text="7"),
                    Answer(text="9"),
                    Answer(text="12"),
                ],
                correct_answer_index=2
            ),
            Question(
                text=(
                    "Найдите длину диагонали прямоугольника, вершины "
                    "которого имеют координаты (2; 1), (2; 4), (6; 1), (6; 4)"
                ),
                answers=[
                    Answer(text="5"),
                    Answer(text="6"),
                    Answer(text="7"),
                    Answer(text="8"),
                ],
                correct_answer_index=0
            ),
            Question(
                text=(
                    "Верно ли утверждение? В трапецию можно вписать окружность, "
                    "если сумма оснований трапеции равна сумме её боковых сторон"
                ),
                answers=[
                    Answer(text="верно"),
                    Answer(text="не верно"),
                ],
                correct_answer_index=0
            ),
            Question(
                text=(
                    "Два угла треугольника равны 33° и 105°. Найдите тупой угол, "
                    "который образуют высоты треугольника, "
                    "выходящие из вершин этих углов. Ответ дайте в градусах."
                ),
                answers=[
                    Answer(text="42"),
                    Answer(text="126"),
                    Answer(text="138"),
                    Answer(text="176"),
                ],
                correct_answer_index=2,
            ),
            Question(
                text=(
                    "В треугольнике ABC отрезок DE - средняя линия. "
                    "Площадь треугольника CDE равна 38.\n"
                    "Найдите площадь треугольника ABC. "
                ),
                answers=[
                    Answer(text="116"),
                    Answer(text="122"),
                    Answer(text="144"),
                    Answer(text="152"),
                ],
                correct_answer_index=3,
            ),
            Question(
                text=(
                    "В ромбе ABCD угол ABC равен 122°.\n"
                    "Найдите угол ACD. Ответ дайте в градусах."
                ),
                answers=[
                    Answer(text="14"),
                    Answer(text="29"),
                    Answer(text="58"),
                    Answer(text="122"),
                ],
                correct_answer_index=1,
            ),
            Question(
                text=(
                    "Площадь параллелограмма ABCD равна 189. "
                    "Точка E — середина стороны AD.\n"
                    "Найдите площадь трапеции AECB."
                ),
                answers=[
                    Answer(text="94.5"),
                    Answer(text="111.75"),
                    Answer(text="122.75"),
                    Answer(text="122.5"),
                    Answer(text="141.75")
                ],
                correct_answer_index=4,
            ),
            Question(
                text=(
                    "Площадь поверхности куба равна 24.\n"
                    "Найдите его объем"
                ),
                answers=[
                    Answer(text="4"),
                    Answer(text="8"),
                    Answer(text="12"),
                    Answer(text="16"),
                    Answer(text="24")
                ],
                correct_answer_index=1,
            ),
            Question(
                text=(
                    "Выберете верное определение для медианы"
                ),
                answers=[
                    Answer(text=(
                        "отрезок, соединяющий вершину треугольника с "
                        "серединой противоположной стороны"
                    )),
                    Answer(text=(
                        "прямая, перпендикулярная стороне треугольника "
                        "и проходящая через его середину."
                    )),
                    Answer(text=(
                        "луч, который соединяет вершину треуг. с противоположной "
                        "стороной, разделяя угол на две равные части"
                    )),
                ],
                correct_answer_index=0,
            ),
        ],
        callback=final_test_done,
    )
]
