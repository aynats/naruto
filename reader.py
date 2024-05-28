class shikaku_reader:
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
            print("An error occurred:", e)
            return None

    @staticmethod
    def read_matrix_from_console():
        num_rows = int(input('Введите количество строк: '))
        matrix = []
        for _ in range(num_rows):
            row_elements = input(f'Введите элементы {len(matrix) + 1}-й строки, разделённые пробелами: ')

            # Добавление строки в матрицу
            matrix.append([int(elem) for elem in row_elements.split()])

        # Находим длину самой длиной строки
        max_length = 0
        for row in matrix:
            max_length = max(max_length, len(row))

        # Дополняем все строки до размера max_length
        padded_matrix = []
        for row in matrix:
            padding_needed = max_length - len(row)
            if padding_needed > 0:
                left_padding = padding_needed // 2
                right_padding = padding_needed - left_padding
                new_row = [-1] * left_padding + row + [-1] * right_padding
            else:
                new_row = row
            padded_matrix.append(new_row)

        return padded_matrix
