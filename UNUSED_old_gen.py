import random
from class_point import Point
import shikaku_main as m
from class_solver import Solver as s


# ------------------------------------------------------------------------------
def make_table_skeleton(h):
    tabl = []
    if h % 2 == 0:
        for i in range(2, h + 1, 2):
            tabl.append(i*[0])
        for i in range(h//2, 0, -1):
            tabl.append((i*2)*[0])
    else:
        for i in range(1, h + 1, 2):
            tabl.append(i*[0])
        for i in range(h - 2, 0, -2):
            tabl.append(i*[0])
        # for i in range(h//2, 0, -1):
        #     tabl.append((i)*[0])
    for i in range(len(tabl)):
        print (tabl[i])
    print("tabl:", tabl)
    return tabl


def calculate_count_cells(h):
    count_cells = (h // 2 + 1) * h if h % 2 == 0 else ((h - 1) // 2 + 1) * (h - 1) + 1
    return count_cells
    #print("cc", count_cells)
# ------------------------------------------------------------------------------


def find_points_thatwouldbe_taken(count_cells):
    k = 1
    population = 0
    while k > population:
         k = random.randint(1, count_cells)
         population = random.randint(1, count_cells)
    print("k", k, "pop", population)
    selected_points = sorted(random.sample(population=range(0, population), k=k))
    print("sp", selected_points)
    return selected_points


# Заполняем сетку рандомными числами в пределах разумного
def fill_tabl_with_taken_points(tabl, selected_points):
    c = 0
    for i in range(h):
        for j in range(len(tabl[i])):
            if c in selected_points:
                tabl[i][j] = random.randint(1, h)
            c += 1
    return tabl

# Добавляем границы
def add_bounds(tabl):
    padded_matrix = []
    for row in tabl:
        padding_needed = h - len(row)
        if padding_needed > 0:
            left_padding = padding_needed // 2
            right_padding = padding_needed - left_padding
            new_row = [-1] * left_padding + row + [-1] * right_padding
        else:
            new_row = row
        padded_matrix.append(new_row)
    print("padded matrix:")
    for i in range(len(padded_matrix)):
        print(padded_matrix[i])
    return padded_matrix


def handle_list_matrix(matrix_int):
    """Вычисляет и выводит решение в файл и в консоль"""
    rows_count = len(matrix_int)
    cols_count = len(matrix_int[0])
    # print(matrix_int)
    solver = s(matrix_int)

    solutions = solver.main_solve()
    if isinstance(solutions, bool) and not solutions:
        return None
        # sys.exit()
    else:
        unique_solutions = m.find_second_order_lists(solutions.copy())
        result = m.discard_zero_solutions(unique_solutions)
        if len(result) == 0:
            return None
            # print("Для такого Шикаку нет решения")
            # sys.exit()
        # print(result)
        table_rows = []
        for table in result:
            for row in table:
                row_str = ""
                for cell in row:
                    row_str += str(cell) + "\t"  # Добавляем значение ячейки и табуляцию
                table_rows.append(row_str.rstrip("\t"))  # Удаляем лишнюю табуляцию в конце строки
            table_rows.append('\n')
        file_path = "shikaku_generate.txt"
        #
        # # Создаем объект writer для записи в файл
        # with open(file_path, mode='w', newline='', encoding='utf-8') as file:
        #     writer = csv.writer(file, delimiter='\n', quotechar=' ', quoting=csv.QUOTE_MINIMAL)
        #
        #     # Записываем строки таблицы
        #     for row in table_rows:
        #         writer.writerow([row])

        # print(f"Таблица успешно записана в {file_path}")
        m.print_solutions(result, rows_count, cols_count)
        return result



if __name__ == "__main__":
    sol_exists = False
    sol = None
    old_sh = set()
    h = random.randint(3, 4)
    w = random.randint(1, 4)
    #h = 5
    while not sol_exists:
        flag = 0
        # count_cells = 0
        tabl_mt = make_table_skeleton(h)
        count_cells = calculate_count_cells(h)
        selected_points = find_points_thatwouldbe_taken(count_cells)
        tabl_w_p = fill_tabl_with_taken_points(tabl_mt, selected_points)
        print(tabl_w_p)
        tabl_tuple = tuple(map(tuple, tabl_w_p))  # Convert list of lists to tuple of tuples for set storage
        if tabl_tuple not in old_sh:
            old_sh.add(tabl_tuple)
            if flag == 0:
                tabl = add_bounds(tabl_w_p)
            else:
                tabl = tabl_w_p
            sol = handle_list_matrix(tabl)  # 5 секунд на решение
            if sol is not None:
                sol_exists = True
    print("puzzle:")
    print(tabl)
    print("solutions:")
    print(sol)
