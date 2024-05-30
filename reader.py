class Shikaku_Reader:
    @staticmethod
    def get_grid(file_name):
        # список списков-строк
        matrix = []
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
            print("Не можем обработать ваш Шикаку, потому что:", e)
            return None

    @staticmethod
    def read_matrix_from_console(data):
        try:
            num_rows = int(data)
        except ValueError:
            print("Введенное значение не является числом.")
            return None
        matrix = []
        for _ in range(num_rows):
            row_elements = input(f'Введите элементы {len(matrix) + 1}-й строки, разделённые пробелами: ')

            # Добавление строки в матрицу
            matrix.append([elem for elem in row_elements.split()])

        # Находим длину самой длинной строки
        max_length = 0
        for row in matrix:
            max_length = max(max_length, len(row))

        if len(matrix[num_rows // 2]) != max_length:
            raise ValueError("Похоже, введен не выпуклый шестиугольник.")

        if num_rows % 2 == 0:
            if len(matrix[(num_rows - 1) // 2]) != len(matrix[(num_rows - 1) // 2]) + 1:
                raise ValueError("Серединные строки шестиугольника с четным количеством строк должны быть одинаковой длины.")
        # print(matrix)

        if num_rows % 2 == 0:
            for i in range(num_rows):
                if len(matrix[(num_rows - 1) // 2 - i]) != len(matrix[(num_rows - 1) // 2 + 1 + i]):
                    raise ValueError(
                        "Симметричные строки должны быть одинаковой длины.")

        if num_rows % 2 != 0:
            for i in range(1, num_rows):
                if len(matrix[(num_rows - 1) // 2 - i]) != len(matrix[(num_rows - 1) // 2 + i]):
                    raise ValueError(
                        "Симметричные строки должны быть одинаковой длины.")

        # Дополняем все строки до размера max_length
        padded_matrix = []
        for row in matrix:
            padding_needed = max_length - len(row)
            if padding_needed > 0:
                left_padding = padding_needed // 2
                right_padding = padding_needed - left_padding
                new_row = ['-1'] * left_padding + row + ['-1'] * right_padding
            else:
                new_row = row
            padded_matrix.append(new_row)

        result_list = []
        try:
            for row in padded_matrix:
                row_str = [i.replace('_', '0').replace('Q', '-1') for i in row]
                result_list.append(row_str)
                result_list = [[int(x) for x in row] for row in result_list]

            # print(result_list)
            return result_list

        except FileNotFoundError:
            print("File not found.")
            return None

        except Exception as e:
            print("Не можем обработать ваш Шикаку, потому что:", e)
            return None


