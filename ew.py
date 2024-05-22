from Point import Point
def get_grid(file_name):
    matrix = [] #список списков-строк
    try:
        with open(file_name, 'r') as file:
            for line in file:
                row_str = line[:-1].replace('_', '0').replace('Q', '-1')
                row = [int(x) for x in row_str.split()]
                matrix.append(row)
        return matrix

    except FileNotFoundError:
        print("File not found.")
        return None

    except Exception as e:
        print("An error occurred:", e)
        return None


def calculate_lenwidth(matrix):
    rows_count = len(matrix)
    cols_count = len(matrix[0])
    return (cols_count, rows_count)


def get_rect_various(matrix, x, y) -> set:
    """Возвращает множество допустимых вариантов прямоугольников для данной ячейки"""
    number = matrix[y][x]
    rect_various = set()
    razmerSlevaNapravo, razmerSnizuVverh = calculate_lenwidth(matrix)
    for num in range(1, number + 1):
        if number % num == 0:
            height = num
            width = number // num
            # работало верно, надо было переставить размеры с квадратного на прямоугольники
            for i in range(max(0, x - width + 1), min(x + 1, razmerSlevaNapravo - width + 1)):
                for j in range(max(0, y - height + 1), min(y + 1, razmerSnizuVverh - height + 1)):
                    # if is_bound(matrix, i, j, height, width):
                    #     continue
                    rect_various.add((i, j, height, width))
    return rect_various
                    # print("x", i, "y", j, "I", height, "--", width) - работает верно
                # if not self.__is_reserved_points_in_rect(Rect(i, j, height, width), point):
                # if matrix[j][i] == -1 or matrix[j][i + width - 1] == -1:
                # continue
                # print(i, j, height, width)
                # rect_various.add(i, j, height, width)


def get_rect_various1(matrix, x, y) -> set:
    """Возвращает множество допустимых вариантов прямоугольников для данной ячейки"""
    number = matrix[y][x]
    rect_various = set()
    razmerSlevaNapravo, razmerSnizuVverh = calculate_lenwidth(matrix)
    for num in range(1, number + 1):
        if number % num == 0:
            height = num
            width = number // num
            # работало верно, надо было переставить размеры с квадратного на прямоугольники
            for i in range(max(0, x - width + 1), min(x + 1, razmerSlevaNapravo - width + 1)):
                for j in range(max(0, y - height + 1), min(y + 1, razmerSnizuVverh - height + 1)):
                    if is_bound(matrix, i, j, height, width):
                        continue
                    rect_various.add((i, j, height, width))
    return rect_various


def is_bound(matrix, i, j, height, width):
    # Проверяем, что координаты и размеры прямоугольника валидны
    if i < 0 or j < 0 or i + width > len(matrix[0]) or j + height > len(matrix):
        return False, "yadurak, чето выходит"

    # Проходим по каждому символу в прямоугольнике
    for row in range(j, j + height):
        for col in range(i, i + width):
            if matrix[row][col] == -1:
                return True  # Найден символ "q", возвращаем True

    return False


def get_start_points(matrix):
    """Ищет и возвращает множество изначальных точек из Shikaku"""
    points = set()
    for y in range(len(matrix)):
        for x in range(len(matrix[y])):
            if matrix[y][x] > 0:
                points.add(Point(x, y))

    return points


if __name__ == "__main__":
    # matrix = input("Enter a filename in your directory:")
    matrix_str = "test1.txt"
    matrix_int = get_grid(matrix_str)
    x, y = calculate_lenwidth(matrix_int)
    print("Парсинг матрицы:", matrix_int)
    print("Размеры матрицы:", x, "*", y)
    print("Возможные прямоугольники без учета границ:")
    print(get_rect_various(matrix_int, 6,3))
    print("Возможные прямоугольники с учетом границ:")
    print(get_rect_various1(matrix_int, 6,3))
    # all_the_points_on_grid = get_start_points(matrix_int)
    # print("Список всех координат чисел на поле в хэше:", all_the_points_on_grid)
    # print("Есть ли границы в прямоугольниках:", is_bound(matrix_int, 4,2, 4, 1))
