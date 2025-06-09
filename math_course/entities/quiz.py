from typing import Awaitable, Callable

from aiogram.types import PollAnswer
from pydantic.dataclasses import dataclass

from math_course.handlers.user_flow import first_lesson, second_lesson, third_lesson, fourth_lesson, sixth_lesson, final_test_done


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
                text=(
                    "В параллелограмме ABCD диагональ AC равна 8, а сторона AB равна 5. "
                    "Найдите периметр параллелограмма, если его площадь равна 24."
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
                    "В параллелограмме ABCD биссектриса угла A пересекает сторону BC "
                    "в точке M. Найдите BM, если AB = 6, BC = 4."
                ),
                answers=[
                    Answer(text="2"),
                    Answer(text="2.5"),
                    Answer(text="3"),
                    Answer(text="3.5"),
                ],
                correct_answer_index=0
            ),
            Question(
                text=(
                    "В параллелограмме ABCD проведены биссектрисы углов A и B, "
                    "которые пересекаются в точке M. Найдите угол AMB."
                ),
                answers=[
                    Answer(text="45°"),
                    Answer(text="60°"),
                    Answer(text="90°"),
                    Answer(text="120°"),
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
                    "Векторы a и b образуют угол 60°. Известно, что |a| = 3, |b| = 4. "
                    "Найдите |a + b|."
                ),
                answers=[
                    Answer(text="5"),
                    Answer(text="6"),
                    Answer(text="7"),
                    Answer(text="8"),
                ],
                correct_answer_index=1,
            ),
            Question(
                text=(
                    "Векторы a и b перпендикулярны. Известно, что |a| = 5, |b| = 12. "
                    "Найдите |a - b|."
                ),
                answers=[
                    Answer(text="13"),
                    Answer(text="14"),
                    Answer(text="15"),
                    Answer(text="16"),
                ],
                correct_answer_index=0,
            ),
        ],
        callback=third_lesson,
    ),
    Quiz(
        questions=[
            Question(
                text=(
                    "В равнобедренной трапеции ABCD с основаниями AD и BC "
                    "диагональ AC перпендикулярна боковой стороне CD. "
                    "Найдите площадь трапеции, если AD = 12, BC = 4."
                ),
                answers=[
                    Answer(text="32"),
                    Answer(text="36"),
                    Answer(text="40"),
                    Answer(text="48"),
                ],
                correct_answer_index=1
            ),
            Question(
                text=(
                    "В трапеции ABCD с основаниями AD и BC диагонали пересекаются "
                    "в точке O. Площадь треугольника AOD равна 16, а площадь "
                    "треугольника BOC равна 4. Найдите площадь трапеции."
                ),
                answers=[
                    Answer(text="36"),
                    Answer(text="40"),
                    Answer(text="44"),
                    Answer(text="48"),
                ],
                correct_answer_index=0
            ),
            Question(
                text=(
                    "В трапеции ABCD с основаниями AD и BC проведена средняя линия MN. "
                    "Найдите площадь трапеции, если площадь треугольника MNC равна 12, "
                    "а площадь треугольника MND равна 8."
                ),
                answers=[
                    Answer(text="40"),
                    Answer(text="48"),
                    Answer(text="56"),
                    Answer(text="64"),
                ],
                correct_answer_index=2
            ),
            Question(
                text=(
                    "В трапеции ABCD с основаниями AD и BC проведены высоты BH и CK. "
                    "Найдите площадь трапеции, если BH = 6, CK = 8, а основания "
                    "относятся как 2:3."
                ),
                answers=[
                    Answer(text="60"),
                    Answer(text="72"),
                    Answer(text="84"),
                    Answer(text="96"),
                ],
                correct_answer_index=1
            ),
        ],
        callback=fourth_lesson,
    ),
    Quiz(
        questions=[
            Question(
                text=(
                    "В окружности радиуса 5 проведены две хорды AB и CD, "
                    "пересекающиеся в точке M. Найдите длину хорды AB, если "
                    "AM = 3, CM = 4, DM = 6."
                ),
                answers=[
                    Answer(text="8"),
                    Answer(text="9"),
                    Answer(text="10"),
                    Answer(text="12"),
                ],
                correct_answer_index=1
            ),
            Question(
                text=(
                    "В окружности проведены две пересекающиеся хорды AB и CD. "
                    "Найдите длину хорды CD, если AB = 12, а отрезки, на которые "
                    "делится точка пересечения хорду AB, равны 3 и 9."
                ),
                answers=[
                    Answer(text="6"),
                    Answer(text="8"),
                    Answer(text="10"),
                    Answer(text="12"),
                ],
                correct_answer_index=0
            ),
            Question(
                text=(
                    "В окружности радиуса 13 проведена хорда AB длиной 24. "
                    "Найдите расстояние от центра окружности до хорды AB."
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
                    "В окружности проведены две хорды AB и CD, пересекающиеся "
                    "в точке M. Найдите длину хорды CD, если AM = 4, BM = 6, "
                    "CM = 3."
                ),
                answers=[
                    Answer(text="5"),
                    Answer(text="6"),
                    Answer(text="7"),
                    Answer(text="8"),
                ],
                correct_answer_index=2
            ),
        ],
        callback=fourth_lesson,
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
    ),
    Quiz(
        questions=[
            Question(
                text=(
                    "В прямоугольном параллелепипеде ABCDA1B1C1D1 ребра AB, AD и AA1 равны 3, 4 и 5 соответственно. "
                    "Найдите площадь сечения, проходящего через вершины A, C и B1."
                ),
                answers=[
                    Answer(text="15"),
                    Answer(text="20"),
                    Answer(text="25"),
                    Answer(text="30"),
                ],
                correct_answer_index=1
            ),
            Question(
                text=(
                    "В кубе ABCDA1B1C1D1 найдите угол между плоскостями ABC и A1B1C1."
                ),
                answers=[
                    Answer(text="0°"),
                    Answer(text="45°"),
                    Answer(text="90°"),
                    Answer(text="180°"),
                ],
                correct_answer_index=0
            ),
            Question(
                text=(
                    "В правильной треугольной призме ABCA1B1C1 все ребра равны 1. "
                    "Найдите расстояние от точки A до плоскости BCA1."
                ),
                answers=[
                    Answer(text="1/2"),
                    Answer(text="1/3"),
                    Answer(text="1/4"),
                    Answer(text="1/6"),
                ],
                correct_answer_index=1
            ),
        ],
        callback=sixth_lesson,
    ),
]
