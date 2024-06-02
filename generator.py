import csv
import random
import shikaku_main as m
from class_solver import Solver as s


def make_hexagon_grid(h):
    tabl = []
    if h % 2 == 0:
        for i in range(2, h + 1, 2):
            tabl.append(i * [0])
        for i in range(h // 2, 0, -1):
            tabl.append((i * 2) * [0])
    else:
        for i in range(1, h + 1, 2):
            tabl.append(i * [0])
        for i in range(h - 2, 0, -2):
            tabl.append(i * [0])
    return tabl


def make_rectangular_grid(height, width):
    return [[0 for _ in range(width)] for _ in range(height)]


def calculate_count_cells(grid, height):
    count = 0
    for i in range(height):
        count += len(grid[height - 1])
    return count


def select_points(count_cells):
    k = random.randint(1, count_cells)
    selected_points = sorted(random.sample(range(count_cells), k))
    return selected_points


def set_selected_points_to_grid(grid, selected_points, height):
    count = 0
    for i in range(height):
        for j in range(len(grid[i])):
            if count in selected_points:
                grid[i][j] = random.randint(1, height)
            count += 1
    return grid


def add_bounds(grid, height):
    padded_matrix = []
    for row in grid:
        padding_needed = height - len(row)
        left_padding = padding_needed // 2
        right_padding = padding_needed - left_padding
        new_row = [-1] * left_padding + row + [-1] * right_padding
        padded_matrix.append(new_row)
    return padded_matrix


def handle_list_matrix(matrix_int):
    solver = s(matrix_int)
    solutions = solver.main_solve()
    if isinstance(solutions, bool) and not solutions:
        return None
    unique_solutions = m.find_second_order_lists(solutions.copy())
    result = m.discard_zero_solutions(unique_solutions)
    if len(result) == 0:
        return None
    return result


def print_puzzle_and_solutions(matrix_int, result):
    rows_count = len(matrix_int)
    cols_count = len(matrix_int[0])

    print("puzzle:")
    for row in matrix_int:
        print("\t".join(str(cell) for cell in row))
    print()

    puzzle_rows = ["puzzle"]
    for row in matrix_int:
        row_str = "\t".join(str(cell) for cell in row)
        puzzle_rows.append(row_str)
    puzzle_rows.append('\n')

    table_rows = ["solutions"]
    for table in result:
        for row in table:
            row_str = "\t".join(str(cell) for cell in row)
            table_rows.append(row_str)
        table_rows.append('\n')
    file_path = "shikaku_generations.txt"

    # Создаем объект writer для записи в файл
    with open(file_path, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file, delimiter='\n', quotechar=' ', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(puzzle_rows)

        for row in table_rows:
            writer.writerow([row])
    print("solutions:")
    m.print_solutions(result, rows_count, cols_count)
    print(f"Таблицы успешно записаны в {file_path}")



def main():
    grid_to_solve = []
    solution_exists = False
    solution = None
    tested_combinations = set()
    height = random.randint(3, 4)
    width = random.randint(1, 4)
    while not solution_exists:
        type_of_grid = random.randint(0, 100)
        count_cells = 0
        zero_grid = []

        if type_of_grid == 1:
            zero_grid = make_rectangular_grid(height, width)
            count_cells = calculate_count_cells(zero_grid, height)

        if type_of_grid != 1:
            zero_grid = make_hexagon_grid(height)
            count_cells = calculate_count_cells(zero_grid, height)

        selected_nonzero_points = select_points(count_cells)
        grid_to_solve = set_selected_points_to_grid(zero_grid, selected_nonzero_points, height)
        grid_tuple = tuple(map(tuple, grid_to_solve))
        if grid_tuple not in tested_combinations:
            tested_combinations.add(grid_tuple)
            if type_of_grid != 1:
                grid_to_solve = add_bounds(grid_to_solve, height)
            solution = handle_list_matrix(grid_to_solve)
            if solution is not None:
                solution_exists = True
    # print(grid_to_solve)
    print_puzzle_and_solutions(grid_to_solve, solution)


if __name__ == "__main__":
    main()

