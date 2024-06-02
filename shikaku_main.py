from class_solver import Solver as s
from class_reader import Shikaku_Reader as r
import csv
import click
import re
import generator as generator


def find_second_order_lists(nested_list):
    """Возвращает список с неповторяющимися таблицами"""

    def is_second_order_list(lst):
        return all(isinstance(i, list) and all(isinstance(j, (int, str)) for j in i) for i in lst)

    second_order_lists = []
    seen = set()  # Множество для отслеживания уникальных таблиц
    stack = [nested_list]

    while stack:
        current = stack.pop()
        if isinstance(current, list):
            for item in current:
                if isinstance(item, list):
                    if is_second_order_list(item):
                        item_tuple = tuple(
                            tuple(row) for row in item)  # Преобразуем в кортежи для добавления в множество
                        if item_tuple not in seen:
                            seen.add(item_tuple)
                            second_order_lists.append(item)
                    stack.append(item)

    return second_order_lists


def discard_zero_solutions(unique_solutions):
    """Отбрасывает все решения, в которых в строках встретились незаполненные прямоугольниками клетки, т.е. неверные"""
    right_unique_solutions = unique_solutions.copy()  # Правильное создание копии списка

    for sub_list in unique_solutions:
        found_zero = False  # Проверяем, был ли найден ноль в текущем списке
        for row in sub_list:
            for item in row:
                if item == 0:
                    found_zero = True  # Помечаем, что в списке найден ноль
                    break  # Прерываем цикл, так как достаточно одного нуля для удаления списка
        if found_zero:  # Если был найден ноль, удаляем этот список из копии
            right_unique_solutions.remove(sub_list)

    return right_unique_solutions


def handle_list_matrix(matrix_int):
    """Вычисляет и выводит решение в файл и в консоль"""
    rows_count = len(matrix_int)
    cols_count = len(matrix_int[0])
    # print(matrix_int)
    solver = s(matrix_int)

    solutions = solver.main_solve()
    if isinstance(solutions, bool) and not solutions:
        print("Для такого Шикаку нет решения")
        # sys.exit()
    else:
        unique_solutions = find_second_order_lists(solutions.copy())
        result = discard_zero_solutions(unique_solutions)
        if len(result) == 0:
            print("Для такого Шикаку нет решения")
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
    """Печатает решение в консоль"""
    for chart in range(len(result)):
        for row in range(rows_count):
            for column in range(cols_count):
                print(result[chart][row][column], end='\t')
            print()
        print()


@click.command()
@click.option('--path', '-p', type=str, default=None, help='Решает головоломку Шикаку из .txt с введенным названием.')
@click.option('--console', '-c', type=str, default=None, help='Решает головоломку с указанным числом строк.')
@click.option('--generate', '-g', is_flag=True, help='Генерирует Шикаку с решением.')
def main(path, generate, console):
    if path:
        try:
            line = re.search(r'(^[a-zA-Z0-9!_-]+(\.txt)$)', path)
            if line:
                get_grid_for_file(line.group())
            else:
                print('Введите файл с расширением .txt для решения.')
        except Exception as e:
            print(f"Ошибка при чтении файла '{path}': {e}.")
    elif console:
        try:
            grid_rows_count = int(console)  # Попытка преобразовать строку в целое число
            if grid_rows_count > 0:  # Проверка, что число положительное
                get_grid_for_console(grid_rows_count)
            else:
                print('Число строк должно быть положительным.')
        except ValueError:
            print('Введите число - количество строк в Шикаку.')
    elif generate:
        generator.main()
    else:
        print("Необходимо указать название файла, количество вводимых строк или флаг --example.")


def get_grid_for_file(inputted_data):
    """Пытается вычислить решение при условии, когда введено имя файла"""
    try:
        matrix_int = r.get_grid(inputted_data)
        return handle_list_matrix(matrix_int)
    except Exception as e:
        print(f"Ошибка при чтении файла {inputted_data}: {e}")


def get_grid_for_console(inputted_data):
    """Пытается вычислить решение при условии, когда ввод производится через консоль"""
    try:
        matrix_int = r.read_matrix_from_console(inputted_data)
        handle_list_matrix(matrix_int)
    except Exception as a:
        print('Ошибка ввода в консоль: ', a)


if __name__ == "__main__":
    main()
