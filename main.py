import sys
from solver import Solver as s
from reader import Shikaku_Reader as r
import re
import csv
import unittest


def find_second_order_lists(nested_list):
    """Возвращает список с неповторяющимися таблицами"""
    second_order_lists = []  # Список для хранения всех найденных таблиц с уникальными решениями

    def get_unique_solutions(sl):
        """Вкладывает в главный список таблиц одну уникальную таблицу"""
        for item in sl:
            solution = []
            if isinstance(item, list):  # Если элемент является списком
                if all(isinstance(i, list) for i in item):  # Проверяем, что все элементы внутри - списки
                    for row in range(len(item)):
                        # Проверяем, что все элементы внутри списка - либо цифры (-1), либо строки
                        if all(isinstance(i, int) or isinstance(i, str) for i in item[row]):
                            solution.append(item[row])
                            if row == len(item) - 1:
                                if solution not in second_order_lists:
                                    second_order_lists.append(solution.copy())
                                solution.clear()
                        else:
                            get_unique_solutions(item)

    get_unique_solutions(nested_list)
    return second_order_lists


def discard_zero_solutions(unique_solutions):
    """Отбрасывает все решения, в которых в строках встретились незаполненные прямоугольниками клетки, т.е. неверные"""
    right_unique_solutions = unique_solutions.copy()
    for sub_list in unique_solutions:
        for row in sub_list:
            for item in row:
                if item == 0:
                    right_unique_solutions.remove(sub_list)
                    break
    return right_unique_solutions


def handle_list_matrix(matrix_int):
    rows_count = len(matrix_int)
    cols_count = len(matrix_int[0])
    # print(matrix_int)
    solver = s(matrix_int)

    solutions = solver.main_solve()
    if isinstance(solutions, bool) and not solutions:
        print("There is no solutions for Shikaku task")
        sys.exit()
    else:
        unique_solutions = find_second_order_lists(solutions.copy())
        result = discard_zero_solutions(unique_solutions)
        if len(result) == 0:
            print("There is no solutions for Shikaku")
            sys.exit()
        # print(result)
        table_rows = []
        for table in result:
            for row in table:
                row_str = ""
                for cell in row:
                    row_str += str(cell) + "\t"  # Добавляем значение ячейки и табуляцию
                table_rows.append(row_str.rstrip("\t"))  # Удаляем лишнюю табуляцию в конце строки
            table_rows.append('\n')
        file_path = "shikaku_solutions.txt"

        # Создаем объект writer для записи в файл
        with open(file_path, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file, delimiter='\n', quotechar=' ', quoting=csv.QUOTE_MINIMAL)

            # Записываем строки таблицы
            for row in table_rows:
                writer.writerow([row])

        print(f"Таблица успешно записана в {file_path}")
        print_solutions(result, rows_count, cols_count)
        return result


def print_solutions(result, rows_count, cols_count):
    for l in range(len(result)):
        for i in range(rows_count):
            for j in range(cols_count):
                print(result[l][i][j], end='\t')
                pass
            print()
        print()


def get_grid_for_file(inputted_data):
    try:
        matrix_int = r.get_grid(inputted_data)
        return handle_list_matrix(matrix_int)
    except Exception:
        print("Ошибка - неверный формат файла")


def get_grid_for_console(inputted_data):
    try:
        matrix_int = r.read_matrix_from_console(inputted_data)
        handle_list_matrix(matrix_int)
    except ValueError as a:
        print('Ошибка: ', a)


if __name__ == "__main__":
    while True:
        print("Введите имя файла с неразрешенным Шикаку или количество строк для решения из консоли.")
        inputted_data = input()
        line = re.search(r'(^[a-zA-Z0-9!_-]+(\.[a-zA-Z0-9]+)$)', inputted_data)
        if line:
            get_grid_for_file(line.group())
        else:
            get_grid_for_console(inputted_data)


class TestShikakuSolver(unittest.TestCase):
    def test_txt_average_chart_3x3(self):
        result = get_grid_for_file("test18.txt")
        self.assertEqual([[[-1, 'b', -1], ['a', 'b', 'c'], [-1, 'b', -1]]], result)

    def test_txt_average_chart_4x4(self):
        result = get_grid_for_file("test2.txt")
        self.assertEqual([[[-1, 'c', 'c', -1], ['a', 'a', 'a', 'a'], [-1, 'b', 'b', -1]]], result)

    def test_txt_average_chart_5x5(self):
        result = get_grid_for_file("test3.txt")
        self.assertEqual([[[-1, 'f', 'f', 'f', -1], ['a', 'a', 'a', 'a', 'a'], ['g', 'g', 'd', 'd', 'd'],
                           ['c', 'c', 'c', 'c', 'e'], [-1, 'b', 'b', 'b', -1]]], result)

        result = get_grid_for_file("test4.txt")
        self.assertEqual([[[-1, 'b', 'd', 'c', -1], ['e', 'b', 'd', 'c', 'g'], ['e', 'f', 'd', 'c', 'g'],
                           ['e', 'f', 'd', 'c', 'a'], [-1, 'f', 'd', 'c', -1]]], result)

        result = get_grid_for_file("test5.txt")
        self.assertEqual([[[-1, 'a', 'a', 'a', -1], ['e', 'e', 'f', 'b', 'b'], ['e', 'e', 'f', 'b', 'b'],
                           ['e', 'e', 'd', 'd', 'd'], [-1, 'c', 'c', 'c', -1]]], result)

        result = get_grid_for_file("test8.txt")
        self.assertEqual([[[-1, 'a', 'a', 'a', -1], ['e', 'a', 'a', 'a', 'b'], ['e', 'a', 'a', 'a', 'b'],
                           ['d', 'd', 'd', 'd', 'b'], [-1, 'c', 'c', 'c', -1]]], result)

    def test_txt_average_chart_8x8(self):
        result = get_grid_for_file("test1.txt")
        self.assertEqual([[[-1, -1, 'a', 'a', 'a', 'a', -1, -1], [-1, 'c', 'c', 'c', 'c', 'c', 'c', -1],
                           ['b', 'b', 'b', 'b', 'e', 'e', 'e', 'e'], ['d', 'd', 'd', 'd', 'd', 'd', 'd', 'd'],
                           [-1, 'f', 'f', 'f', 'f', 'f', 'f', -1], [-1, -1, 'g', 'g', 'g', 'g', -1, -1]]], result)

        result = get_grid_for_file("test6.txt")
        self.assertEqual([[[-1, -1, -1, 'f', 'b', -1, -1, -1], [-1, -1, 'g', 'f', 'b', 'e', -1, -1],
                           [-1, 'a', 'g', 'n', 'n', 'n', 'n', -1],
                           ['h', 'h', 'g', 'k', 'k', 'l', 'l', 'l'], ['h', 'h', 'g', 'k', 'k', 'd', 'j', 'j'],
                           [-1, 'c', 'g', 'k', 'k', 'o', 'o', -1], [-1, -1, 'g', 'm', 'm', 'm', -1, -1],
                           [-1, -1, -1, 'i', 'i', -1, -1, -1]]], result)

    def test_txt_for_rectangle(self):
        result = get_grid_for_file("test19.txt")
        self.assertEqual([[['e', 'e', 'f', 'c', 'c', 'a'], ['e', 'e', 'f', 'c', 'c', 'a'],
                           ['b', 'b', 'b', 'c', 'c', 'a'], ['b', 'b', 'b', 'c', 'c', 'a'],
                           ['b', 'b', 'b', 'c', 'c', 'a'], ['d', 'd', 'd', 'd', 'd', 'a']]], result)

    # def test_txt_wrong_cells(self):
    #     result = get_grid_for_file("test10.txt")
    #     self.assertEqual(sys.exit(), result)

    # def test_txt_wrong_format(self):
    #     result = get_grid_for_file("test_text.txt")
    #     self.assertEqual(sys.exit(), result)
    def test_txt_for_5x3_3x5(self):
        result = get_grid_for_file("test16.txt")
        self.assertEqual([[[-1, 'a', -1], [-1, 'a', -1], ['b', 'b', 'b'], [-1, 'c', -1], [-1, 'c', -1]]], result)
        result = get_grid_for_file("test17.txt")
        self.assertEqual([[[-1, -1, 'c', -1, -1], ['a', 'a', 'c', 'b', 'b'], [-1, -1, 'c', -1, -1]]], result)

    def test_txt_multiple_solutions(self):
        result = get_grid_for_file("test14.txt")
        self.assertEqual([[['a', 'b'], ['a', 'b']], [['b', 'b'], ['a', 'a']]], result)
        result = get_grid_for_file("test15.txt")
        self.assertEqual([[[-1, -1, 'd', 'd', 'd', -1, -1], [-1, 'b', 'g', 'g', 'g', 'c', -1],
                           ['e', 'b', 'h', 'h', 'h', 'c', 'a'], [-1, 'b', 'i', 'i', 'i', 'c', -1],
                           [-1, -1, 'f', 'f', 'f', -1, -1]],
                          [[-1, -1, 'd', 'd', 'd', -1, -1], [-1, 'b', 'h', 'g', 'i', 'c', -1],
                           ['e', 'b', 'h', 'g', 'i', 'c', 'a'], [-1, 'b', 'h', 'g', 'i', 'c', -1],
                           [-1, -1, 'f', 'f', 'f', -1, -1]],
                          [[-1, -1, 'd', 'd', 'd', -1, -1], [-1, 'b', 'g', 'g', 'g', 'c', -1],
                           ['e', 'b', 'i', 'f', 'h', 'c', 'a'], [-1, 'b', 'i', 'f', 'h', 'c', -1],
                           [-1, -1, 'i', 'f', 'h', -1, -1]]], result)


    # Проверка с консоли
    # matrix = r.read_matrix_from_console()
    # print(matrix)

    # # Проверка метода reserve_rectangle
    # print()
    # first_key = next(iter(solutions))
    #
    # # Теперь мы можем получить доступ к первому кортежу первого ключа
    # desired_tuple = list(solutions[first_key])[0]
    #
    # # print("reserve", desired_tuple)
    # print("reserve", solver.reserve_rectangle(desired_tuple, list(solutions.keys())[2]))

    # for key, val in dict.items():
    #     print(f"Point ({key.X}, {key.Y}):")
    #     for rectangle in val:
    #         print(rectangle)

    # points_on_grid = get_start_points(matrix_int)
    # for point in points_on_grid:
    #     #global dictionary_of_points
    #     dictionary_of_points[point] = None
    #
    # #for key in dictionary_of_points:
    #     #print("Все полученные точки поля: ", key)
    #
    # x, y = calculate_lenwidth(matrix_int)
    # #calculate_lenwidth(matrix_int)
    # print("Парсинг матрицы:", matrix_int)
    # print("Размеры матрицы:", x, "*", y)
    # print("Возможные прямоугольники у точки без учета границ:")
    # print(get_rect_various_all(matrix_int, 4,0))
    # print("Возможные прямоугольники у точки с учетом границ:")
    # print(get_rect_various_bounds(matrix_int, 4,0))
    #
    # # В словаре каждой точке сопоставили кортеж с прямоугольником
    # for key in dictionary_of_points:
    #     dictionary_of_points[key] = get_rect_various_bounds(matrix_int, key.X, key.Y)

    # Вывод всех ректанглов для каждой точки в словаре
    # for point, rectangles in dictionary_of_points.items():
    #     print(f"Point ({point.X}, {point.Y}):")
    #     for rectangle in rectangles:
    #         print(rectangle)

    # all_the_points_on_grid = get_start_points(matrix_int)
    # print("Список всех координат чисел на поле в хэше:", all_the_points_on_grid)
    # print("Есть ли границы в прямоугольниках:", is_bound(matrix_int, 4,2, 4, 1))
