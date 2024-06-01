from class_solver import Solver as s
from class_reader import Shikaku_Reader as r
import csv
import click
import re


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
@click.option('--grid-input', '-i', type=str, default=None, help='Решает головоломку с указанным числом строк.')
@click.option('--example', '-e', is_flag=True, help='Генерирует Шикаку с решением.')
def main(path, example, grid_input):
    if path:
        try:
            line = re.search(r'(^[a-zA-Z0-9!_-]+(\.txt)$)', path)
            if line:
                get_grid_for_file(line.group())
            else:
                print('Введите файл с расширением .txt для решения.')
        except Exception as e:
            print(f"Ошибка при чтении файла '{path}': {e}.")
    elif grid_input:
        try:
            grid_rows_count = int(grid_input)  # Попытка преобразовать строку в целое число
            if grid_rows_count > 0:  # Проверка, что число положительное
                get_grid_for_console(grid_rows_count)
            else:
                print('Число строк должно быть положительным.')
        except ValueError:
            print('Введите число - количество строк в Шикаку.')
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
