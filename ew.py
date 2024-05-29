from pppoint import Point


points_on_grid = set()


def get_grid(file_name):
    matrix = [] #список списков-строк
    try:
        with open(file_name, 'r') as file:
            for line in file:
                row_str = line[:-1] if line[:-1] == '\n' else line
                row_str = row_str.replace('_', '0').replace('Q', '-1')
                row = [int(x) for x in row_str.split()]
                matrix.append(row)
        return matrix

    except FileNotFoundError:
        print("File not found.")
        return None

    except Exception as e:
        print("An error occurred:", e)
        return None

# cols_count = None
# rows_count = None


dictionary_of_points = {}


def calculate_lenwidth(matrix):
    #global cols_count, rows_count
    cols_count= len(matrix[0])
    rows_count = len(matrix)
    return (cols_count, rows_count)


def get_rect_various_all(matrix, x, y) -> set:
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


def get_rect_various_bounds(matrix, x, y) -> set:
    """Возвращает множество допустимых вариантов прямоугольников для данной ячейки"""
    number = matrix[y][x]
    rect_various = set()
    razmerSlevaNapravo, razmerSnizuVverh = calculate_lenwidth(matrix)
    print("!", points_on_grid)
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
    matrix_str = "test-.txt"
    matrix_int = get_grid(matrix_str)
    #global points_on_grid
    points_on_grid = get_start_points(matrix_int)

    for point in points_on_grid:
        #global dictionary_of_points
        dictionary_of_points[point] = None

    #for key in dictionary_of_points:
        #print("Все полученные точки поля: ", key)

    x, y = calculate_lenwidth(matrix_int)
    #calculate_lenwidth(matrix_int)
    print("Парсинг матрицы:", matrix_int)
    print("Размеры матрицы:", x, "*", y)
    print("Возможные прямоугольники у точки без учета границ:")
    print(get_rect_various_all(matrix_int, 4,0))
    print("Возможные прямоугольники у точки с учетом границ:")
    print(get_rect_various_bounds(matrix_int, 4,0))

    # В словаре каждой точке сопоставили кортеж с прямоугольником
    for key in dictionary_of_points:
        dictionary_of_points[key] = get_rect_various_bounds(matrix_int, key.X, key.Y)

    # Вывод всех ректанглов для каждой точки в словаре
    # for point, rectangles in dictionary_of_points.items():
    #     print(f"Point ({point.X}, {point.Y}):")
    #     for rectangle in rectangles:
    #         print(rectangle)

    # all_the_points_on_grid = get_start_points(matrix_int)
    # print("Список всех координат чисел на поле в хэше:", all_the_points_on_grid)
    # print("Есть ли границы в прямоугольниках:", is_bound(matrix_int, 4,2, 4, 1))
