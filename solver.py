from copy import deepcopy
from pppoint import Point
from rrrrectangle import Rect


class Solver:
    def __init__(self, matrix):
        self.matrix = matrix
        self.dictionary_of_points = dict()
        self.rows_count = len(matrix)
        self.cols_count = len(matrix[0])
        self.points_on_grid = self.get_start_points()
        self.reserved_points = deepcopy(self.points_on_grid)
        # self.answer_matrix = [['0' for j in range(len(matrix))] for i in range(len(matrix))]
        self.answer_matrix = deepcopy(self.matrix)
        # self.fill_answer_matrix()
        self.counter_reserved_rect = 1
        self.determine_part_solve()

    def fill_answer_matrix(self):
        for j in range(self.rows_count):
            for i in range(self.cols_count):
                if self.matrix[j][i] >= 0:
                    self.answer_matrix[j][i] = 0

    # cols_count = None
    # rows_count = None

    # def calculate_dimensions(self) -> (int, int):
    #     #global cols_count, rows_count
    #     cols_count= len(self.matrix[0])
    #     rows_count = len(self.matrix)
    #     return cols_count, rows_count

    # def get_rect_various_all(self, x, y) -> set:
    #     """Возвращает множество допустимых вариантов прямоугольников для данной ячейки"""
    #     number = self.matrix[y][x]
    #     rect_various = set()
    #     for num in range(1, number + 1):
    #         if number % num == 0:
    #             height = num
    #             width = number // num
    #             # работало верно, надо было переставить размеры с квадратного на прямоугольники
    #             for i in range(max(0, x - width + 1), min(x + 1, self.cols_count - width + 1)):
    #                 for j in range(max(0, y - height + 1), min(y + 1, self.rows_count - height + 1)):
    #                     # if is_bound(matrix, i, j, height, width):
    #                     #     continue
    #                     rect_various.add(Rect(i, j, height, width))
    #     return rect_various

    def get_rect_various_bounds(self, point: Point) -> set:
        """Возвращает все возможные расположения прямоугольников для каждой ячейки"""
        number = self.matrix[point.Y][point.X]
        rect_various = set()
        for num in range(1, number + 1):
            if number % num == 0:
                height = num
                width = number // num
                # работало верно, надо было переставить размеры с квадратного на прямоугольники
                for i in range(max(0, point.X - width + 1), min(point.X + 1, self.cols_count - width + 1)):
                    for j in range(max(0, point.Y - height + 1), min(point.Y + 1, self.rows_count - height + 1)):
                        bounds = self.is_bound(i, j, height, width)
                        if bounds:
                            continue
                        if not self.is_reserved_points_in_rect(Rect(i, j, height, width), point):
                            rect_various.add(Rect(i, j, height, width))
        return rect_various

    def is_reserved_points_in_rect(self, rect: Rect, point: Point):
        """Проверяет, есть ли в данном прямоугольнике уже занятые клетки"""
        for reserved_point in self.reserved_points:
            if rect.contain(reserved_point) and reserved_point != point:
                return True
        return False

    def is_bound(self, i, j, height, width) -> bool:
        """Проверяет наличие границы"""
        # Проверяем, что координаты и размеры прямоугольника валидны
        if i < 0 or j < 0 or i + width > len(self.matrix[0]) or j + height > len(self.matrix):
            return False

        for row in range(j, j + height):
            for col in range(i, i + width):
                if self.matrix[row][col] == -1:
                    return True  # Найден символ "q", возвращаем True

        return False

    def get_start_points(self):
        """Ищет на поле числа, задающие прямоугольники, и возвращает их в виде множества"""
        points = set()
        for x in range(self.cols_count):
            for y in range(self.rows_count):
                if self.matrix[y][x] > 0:
                    points.add(Point(x, y))

        return points

    def reserve_rectangle(self, rect: Rect, point: Point):
        """Резервирует один прямоугольник на поле"""
        if point in self.points_on_grid:
            self.points_on_grid.remove(point)
        all_reserved_point_in_rect = set()
        wi = rect.X + rect.Width
        hi = rect.Y + rect.Height
        rectX = rect.X
        rectY = rect.Y
        flag = not(rect.X < 0 or rect.Y < 0 or wi >= self.cols_count or hi >= self.rows_count)
        if flag:
            for i in range(rect.X, rect.X + rect.Width):    # нужна ли проверка на границы?
                for j in range(rect.Y, rect.Y + rect.Height):
                    #if not(self.is_bound(i, j, rect.Height, rect.Width)):
                    self.answer_matrix[j][i] = chr(97 + self.counter_reserved_rect)
                    all_reserved_point_in_rect.add(Point(i, j))
                        #print(self.answer_matrix[j])

        self.reserved_points = self.reserved_points | all_reserved_point_in_rect
        self.counter_reserved_rect += 1

        for conflict_point in self.dictionary_of_points.keys():          # Не должны ли мы ничего копировать?
            is_conflict = False
            for rect in self.dictionary_of_points[conflict_point]:
                for reserved_point in all_reserved_point_in_rect:
                    if rect.contain(reserved_point):
                        self.dictionary_of_points[conflict_point].remove(rect)
                        is_conflict = True
                        break
                if is_conflict:
                    break

        if point in self.dictionary_of_points:
            self.dictionary_of_points.pop(point)

        # for key, val in self.dictionary_of_points.items():
        #     print(f"Point ({key.X}, {key.Y}):")
        #     for rectangle in val:
        #         print(rectangle)

    def determine_part_solve(self):
        """Заполняет словарь точка-прямоугольник либо резервирует прямоугольники на поле"""
        count_only_possible_point_solutions = 1
        while count_only_possible_point_solutions != 0:
            # Для каждой точки с поля != 0, -1 пересмотрим решения с помощью этого цикла:
            for point in self.points_on_grid.copy():
                rect_various = self.get_rect_various_bounds(point)    # Получаем все возможные прямоугольники для точки
                if len(rect_various) == 1:              # Если рект 1 - решение одно - резервируем
                    self.reserve_rectangle(list(rect_various)[0], point)
                    # self.dictionary_of_points[point] = rect_various
                else:           # Иначе все значения вносим в словарь с прямоугольниками
                    self.dictionary_of_points[point] = rect_various     # self.get_rect_various_bounds(point)

            count_only_possible_point_solutions = 0
            for point in self.points_on_grid:           # Не понимаю
                if len(self.dictionary_of_points[point]) == 1:
                    count_only_possible_point_solutions += 1

    def is_solution_impossible(self):
        """Проверяет, есть ли решение у какой-то точки из словаря"""
        for point in self.points_on_grid:
            if len(self.dictionary_of_points[point]) == 0:
                return True

        return False

    def get_solve_with_reserved_rect(self, rect: Rect, point: Point):
        self.reserve_rectangle(rect, point)
        self.determine_part_solve()
        return self.main_solve()

    def get_all_solves(self):
        answers = []
        if len(self.points_on_grid) == 0:
            answers.append(self.answer_matrix)

        if self.is_solution_impossible():
            return False

        if len(self.points_on_grid) != 0:
            unresolved_point = list(self.points_on_grid)[0]
            for poss_rect in self.dictionary_of_points[unresolved_point]:
                solver_copy = deepcopy(self)
                #solver_copy.reserve_rect(poss_rect, unresolved_point)
                #solver_copy.determine_part_solve()
                ans = solver_copy.get_all_solves_with_reserved_rect(poss_rect, unresolved_point)
                if ans:
                    answers.extend(ans)

        return answers

    def get_all_solves_with_reserved_rect(self, rect: Rect, point: Point):
        self.reserve_rectangle(rect, point)
        self.determine_part_solve()
        return self.get_all_solves()

    def main_solve(self):
        """Основная функция, вызывающая все остальные"""
        if len(self.points_on_grid) == 0:
            # self.fill_answer_matrix()
            return self.answer_matrix

        if self.is_solution_impossible():
            return False

        unresolved_point = list(self.points_on_grid)[0]
        for poss_rect in self.dictionary_of_points[unresolved_point]:
            solver_copy = deepcopy(self)
            # solver_copy.reserve_rect(poss_rect, unresolved_point)
            # solver_copy.determine_part_solve()
            ans = solver_copy.get_solve_with_reserved_rect(poss_rect, unresolved_point)
            if ans:
                return ans


        # for point in self.points_on_grid:
        #     # global dictionary_of_points
        #     self.dictionary_of_points[point] = None
        #
        # for key in self.dictionary_of_points:
        #     self.dictionary_of_points[key] = self.get_rect_various_bounds(key)
        #
        # return self.dictionary_of_points

        # print("Возможные прямоугольники у точки с учетом границ:")
        # print(self.get_rect_various_bounds(6, 3))
        # Вывод всех ректанглов для каждой точки в словаре
        # for point, rectangles in self.dictionary_of_points.items():
        #     print(f"Point ({point.X}, {point.Y}):")
        #     for rectangle in rectangles:
        #         print(rectangle)