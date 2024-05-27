from copy import deepcopy
from pppoint import Point


class Solver:
    def __init__(self, matrix):
        self.matrix = matrix
        self.dictionary_of_points = dict()
        self.rows_count = len(matrix)
        self.cols_count = len(matrix[0])
        self.points_on_grid = self.get_start_points()

        self.unresolved_points = self.get_start_points()
        self.reserved_points = deepcopy(self.unresolved_points)
        self.answer_matrix = [['0' for j in range(len(matrix))] for i in range(len(matrix))]
        self.counter_reserved_rect = 1
        #self.__determine_part_solve()

    # cols_count = None
    # rows_count = None

    # def calculate_dimensions(self) -> (int, int):
    #     #global cols_count, rows_count
    #     cols_count= len(self.matrix[0])
    #     rows_count = len(self.matrix)
    #     return cols_count, rows_count

    def get_rect_various_all(self, x, y) -> set:
        """Возвращает множество допустимых вариантов прямоугольников для данной ячейки"""
        number = self.matrix[y][x]
        rect_various = set()
        for num in range(1, number + 1):
            if number % num == 0:
                height = num
                width = number // num
                # работало верно, надо было переставить размеры с квадратного на прямоугольники
                for i in range(max(0, x - width + 1), min(x + 1, self.cols_count - width + 1)):
                    for j in range(max(0, y - height + 1), min(y + 1, self.rows_count - height + 1)):
                        # if is_bound(matrix, i, j, height, width):
                        #     continue
                        rect_various.add((i, j, height, width))
        return rect_various

    def get_rect_various_bounds(self, x, y) -> set:
        """Возвращает все возможные расположения прямоугольников для каждой ячейки"""
        number = self.matrix[y][x]
        rect_various = set()
        for num in range(1, number + 1):
            if number % num == 0:
                height = num
                width = number // num
                # работало верно, надо было переставить размеры с квадратного на прямоугольники
                for i in range(max(0, x - width + 1), min(x + 1, self.cols_count - width + 1)):
                    for j in range(max(0, y - height + 1), min(y + 1, self.rows_count - height + 1)):
                        if self.is_bound(i, j, height, width):
                            continue
                        rect_various.add((i, j, height, width))
        return rect_various

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

    def reserve_rectangle(self, rect, point: Point):
        if point in self.points_on_grid:
            self.points_on_grid.remove(point)
        all_reserved_point_in_rect = set()
        for i in range(rect.X, rect.X + rect.Height):
            for j in range(rect.Y, rect.Y + rect.Width):
                self.answer_matrix[j][i] = chr(97 + self.counter_reserved_rect)
                all_reserved_point_in_rect.add(Point(i, j))
        self.reserved_points = self.reserved_points | all_reserved_point_in_rect
        self.counter_reserved_rect += 1

        for conflict_point in self.dictionary_of_points.keys():
            is_conflict = False
            for rect in self.dictionary_of_points[conflict_point]:
                for result_point in all_reserved_point_in_rect:
                    if rect.contain(result_point):
                        self.dictionary_of_points[conflict_point].remove(rect)
                        is_conflict = True
                        break
                if is_conflict:
                    break

        if point in self.dictionary_of_points:
            self.dictionary_of_points.pop(point)


    def main_solve(self):
        """Основная функция, вызывающая все остальные"""
        for point in self.points_on_grid:
            # global dictionary_of_points
            self.dictionary_of_points[point] = None

        for key in self.dictionary_of_points:
            self.dictionary_of_points[key] = self.get_rect_various_bounds(key.X, key.Y)

        return self.dictionary_of_points

        # print("Возможные прямоугольники у точки с учетом границ:")
        # print(self.get_rect_various_bounds(6, 3))
        # Вывод всех ректанглов для каждой точки в словаре
        # for point, rectangles in self.dictionary_of_points.items():
        #     print(f"Point ({point.X}, {point.Y}):")
        #     for rectangle in rectangles:
        #         print(rectangle)

