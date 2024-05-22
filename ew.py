def get_grid(file_name):
    matrix = [] #список списков-строк
    try:
        with open(file_name, 'r') as file:
            for line in file:
                row_str = line[:-1].replace('_', '0').replace('Q', '-1')
                row = [int(x) for x in row_str.split()]
                matrix.append(row)
        return matrix

    except FileNotFoundError:
        print("File not found.")
        return None

    except Exception as e:
        print("An error occurred:", e)
        return None


if __name__ == "__main__":
    matrix = input("Enter a filename in your directory:")
    print(get_grid(matrix))
