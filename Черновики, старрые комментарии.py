# ИЗ MAIN:

 # import re
    # while True:
    #     try:
    #         print("Введите имя файла с неразрешенным Шикаку или количество строк для решения из консоли.")
    #         print("Для выхода из программы введите «exit»")
    #         print()
    #         inputted_data = input()
    #         line = re.search(r'(^[a-zA-Z0-9!_-]+(\.[a-zA-Z0-9]+)$)', inputted_data)
    #         if line:
    #             get_grid_for_file(line.group())
    #         elif inputted_data.isdigit():
    #             get_grid_for_console(inputted_data)
    #         elif inputted_data == 'exit':
    #             break
    #         else:
    #             print("Введенное значение не число и не имя файла в директории.")
    #
    #     except Exception:
    #         print("Введенное значение не число и не имя файла в директории.")

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
