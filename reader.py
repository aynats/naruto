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