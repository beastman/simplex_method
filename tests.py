# -*- coding: utf-8 -*-
import unittest

from simplex_solver import SimplexSolver
from simplex_solver.exceptions import NoSolutionException


class SimplexSolverTestCase(unittest.TestCase):
    """Несколько задач из методички для тестов"""
    def test_task_1(self):
        print("\n".join((
            "Задача 1",
            "Минимизировать функцию z = -3x - 4y",
            "Ожидаемый ответ: Минимальное значение функции   = –68 и достигается ",
            "в точке = (12, 8).",
        )))
        solver = SimplexSolver()
        solver.add_target_variable(-3)
        solver.add_target_variable(-4)
        solver.add_constraint(1, 0, '>=', 10)
        solver.add_constraint(0, 1, '>=', 5)
        solver.add_constraint(1, 1, '<=', 20)
        solver.add_constraint(-1, 4, '<=', 20)
        result = solver.solve_minimize()
        self.assertEqual(result, ([12.0, 8.0], -68.0))

    def test_task_2(self):
        print("\n".join((
            "Задача 2",
            "Фирма производит две модели А и В книжных полок. Их производство ",
            "ограничено поставкой сырья (высококачественных досок) и временем машинной ",
            "обработки. Для каждой модели А требуется 3 м2, а для В – 4 м2  досок. ",
            "Фирма может получить от поставщиков до 1700 м2 досок в неделю. Для каждой ",
            "модели А требуется 12 мин. машинного времени, а для В – 30 мин. В неделю ",
            "можно использовать 160 часов машинного времени. Сколько изделий каждой ",
            "модели следует фирме выпускать в неделю, если каждое изделие модели А ",
            "приносит 2 дол. прибыли,  а каждое изделие модели В - 4 дол. прибыли?",
            "",
            "Ожидаемый ответ: Линией уровня с наибольшим значением P, имеющей хотя бы",
            " одну общую точку с допустимой областью, является прямая  с , проходящая ",
            "через вершину В. На ней P принимает значение 1400. Точка В, в которой ",
            "x_1=300 x_2=200",
        )))
        solver = SimplexSolver()
        solver.add_target_variable(2)
        solver.add_target_variable(4)
        solver.add_constraint(3, 4, '<=', 1700)
        solver.add_constraint(2, 5, '<=', 1600)
        result = solver.solve_maximize()
        self.assertEqual(result, ([300.0, 200.0], 1400.0))

    def test_task_3(self):
        print("Минимизировать функцию  z = 2x_1 + 3x_2")
        print("Ожидаемый ответ: Единственное допустимое решение: x_1=5, x_2=0, z=10.")
        solver = SimplexSolver()
        solver.add_target_variable(2)
        solver.add_target_variable(3)
        solver.add_constraint(1, 1, '>=', 10)
        solver.add_constraint(3, 5, '<=', 15)
        result = solver.solve_minimize()
        self.assertEqual(result, ([5.0, 0.0], 10))

    def test_task_4(self):
        print("Максимизировать функцию z=x_1+x_2")
        print("Ожидаемый ответ: Исключение - задача не ограничена")
        solver = SimplexSolver()
        solver.add_target_variable(1)
        solver.add_target_variable(1)
        solver.add_constraint(1, -1, '>=', 1)
        solver.add_constraint(0, 1, '<=', 2)
        with self.assertRaises(NoSolutionException):
            solver.solve_maximize()


if __name__ == '__main__':
    unittest.main()
