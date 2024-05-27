from solver import Solver as s
from reader import shikaku_reader as r
from pppoint import Point
from rrrrectangle import Rect

if __name__ == "__main__":
    # matrix = input("Enter a filename in your directory:")
    matrix_str = "test1.txt"
    matrix_int = r.get_grid(matrix_str)
    rows_count = len(matrix_int)
    cols_count = len(matrix_int[0])
    print(matrix_int)

    solver = s(matrix_int)

    solutions = solver.main_solve()     # сейчас там возвращается словарь прямоугольников
    for i in range(rows_count):
        for j in range(cols_count):
            print(solutions[i][j], end='\t')
        print()
    print()



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