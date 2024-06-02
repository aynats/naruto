
def find_second_order_lists(nested_list):
    second_order_lists = []  # Список для хранения всех найденных таблиц с уникальными решениями
    def get_unique_solutions(sl):
        for item in sl:
            solution = []
            if isinstance(item, list):      # Если элемент является списком
                if all(isinstance(i, list) for i in item):      # Проверяем, что все элементы внутри - списки
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

lis = [[]]

if __name__ == '__main__':
    listik = [[[[[[-1, -1, 'a', 'a', 'a', 'a', -1, -1], [-1, 'c', 'c', 'c', 'c', 'c', 'c', -1], ['b', 'b', 'b', 'b', 'e', 'e', 'e', 'e'], ['d', 'd', 'd', 'f', 'f', 'f', 'd', 'd'], [-1, 0, 0, 'f', 'f', 'f', 0, -1], [-1, -1, 'g', 'g', 'g', 'g', -1, -1]]], [[[[-1, -1, 'a', 'a', 'a', 'a', -1, -1], [-1, 'c', 'c', 'c', 'c', 'c', 'c', -1], ['b', 'b', 'b', 'b', 'e', 'e', 'e', 'e'], ['d', 'd', 'd', 'f', 'f', 'f', 'd', 'd'], [-1, 0, 0, 'f', 'f', 'f', 0, -1], [-1, -1, 'g', 'g', 'g', 'g', -1, -1]]], [[-1, -1, 'a', 'a', 'a', 'a', -1, -1], [-1, 'c', 'c', 'c', 'c', 'c', 'c', -1], ['b', 'b', 'b', 'b', 'e', 'e', 'e', 'e'], ['d', 'd', 'f', 'f', 'f', 'd', 'd', 'd'], [-1, 0, 'f', 'f', 'f', 0, 0, -1], [-1, -1, 'g', 'g', 'g', 'g', -1, -1]]], [[[[-1, -1, 'a', 'a', 'a', 'a', -1, -1], [-1, 'c', 'c', 'c', 'c', 'c', 'c', -1], ['b', 'b', 'b', 'b', 'e', 'e', 'e', 'e'], ['d', 'd', 'd', 'f', 'f', 'f', 'd', 'd'], [-1, 0, 0, 'f', 'f', 'f', 0, -1], [-1, -1, 'g', 'g', 'g', 'g', -1, -1]]], [[[[-1, -1, 'a', 'a', 'a', 'a', -1, -1], [-1, 'c', 'c', 'c', 'c', 'c', 'c', -1], ['b', 'b', 'b', 'b', 'e', 'e', 'e', 'e'], ['d', 'd', 'd', 'f', 'f', 'f', 'd', 'd'], [-1, 0, 0, 'f', 'f', 'f', 0, -1], [-1, -1, 'g', 'g', 'g', 'g', -1, -1]]], [[-1, -1, 'a', 'a', 'a', 'a', -1, -1], [-1, 'c', 'c', 'c', 'c', 'c', 'c', -1], ['b', 'b', 'b', 'b', 'e', 'e', 'e', 'e'], ['d', 'd', 'f', 'f', 'f', 'd', 'd', 'd'], [-1, 0, 'f', 'f', 'f', 0, 0, -1], [-1, -1, 'g', 'g', 'g', 'g', -1, -1]]], [[-1, -1, 'a', 'a', 'a', 'a', -1, -1], [-1, 'c', 'c', 'c', 'c', 'c', 'c', -1], ['b', 'b', 'b', 'b', 'e', 'e', 'e', 'e'], ['d', 'd', 'd', 'd', 'd', 'd', 'd', 'd'], [-1, 'f', 'f', 'f', 'f', 'f', 'f', -1], [-1, -1, 'g', 'g', 'g', 'g', -1, -1]]], [[[[-1, -1, 'a', 'a', 'a', 'a', -1, -1], [-1, 'c', 'c', 'c', 'c', 'c', 'c', -1], ['b', 'b', 'b', 'b', 'e', 'e', 'e', 'e'], ['d', 'd', 'd', 'f', 'f', 'f', 'd', 'd'], [-1, 0, 0, 'f', 'f', 'f', 0, -1], [-1, -1, 'g', 'g', 'g', 'g', -1, -1]]], [[[[-1, -1, 'a', 'a', 'a', 'a', -1, -1], [-1, 'c', 'c', 'c', 'c', 'c', 'c', -1], ['b', 'b', 'b', 'b', 'e', 'e', 'e', 'e'], ['d', 'd', 'd', 'f', 'f', 'f', 'd', 'd'], [-1, 0, 0, 'f', 'f', 'f', 0, -1], [-1, -1, 'g', 'g', 'g', 'g', -1, -1]]], [[-1, -1, 'a', 'a', 'a', 'a', -1, -1], [-1, 'c', 'c', 'c', 'c', 'c', 'c', -1], ['b', 'b', 'b', 'b', 'e', 'e', 'e', 'e'], ['d', 'd', 'f', 'f', 'f', 'd', 'd', 'd'], [-1, 0, 'f', 'f', 'f', 0, 0, -1], [-1, -1, 'g', 'g', 'g', 'g', -1, -1]]], [[[[-1, -1, 'a', 'a', 'a', 'a', -1, -1], [-1, 'c', 'c', 'c', 'c', 'c', 'c', -1], ['b', 'b', 'b', 'b', 'e', 'e', 'e', 'e'], ['d', 'd', 'd', 'f', 'f', 'f', 'd', 'd'], [-1, 0, 0, 'f', 'f', 'f', 0, -1], [-1, -1, 'g', 'g', 'g', 'g', -1, -1]]], [[[[-1, -1, 'a', 'a', 'a', 'a', -1, -1], [-1, 'c', 'c', 'c', 'c', 'c', 'c', -1], ['b', 'b', 'b', 'b', 'e', 'e', 'e', 'e'], ['d', 'd', 'd', 'f', 'f', 'f', 'd', 'd'], [-1, 0, 0, 'f', 'f', 'f', 0, -1], [-1, -1, 'g', 'g', 'g', 'g', -1, -1]]], [[-1, -1, 'a', 'a', 'a', 'a', -1, -1], [-1, 'c', 'c', 'c', 'c', 'c', 'c', -1], ['b', 'b', 'b', 'b', 'e', 'e', 'e', 'e'], ['d', 'd', 'f', 'f', 'f', 'd', 'd', 'd'], [-1, 0, 'f', 'f', 'f', 0, 0, -1], [-1, -1, 'g', 'g', 'g', 'g', -1, -1]]], [[-1, -1, 'a', 'a', 'a', 'a', -1, -1], [-1, 'c', 'c', 'c', 'c', 'c', 'c', -1], ['b', 'b', 'b', 'b', 'e', 'e', 'e', 'e'], ['d', 'd', 'd', 'd', 'd', 'd', 'd', 'd'], [-1, 'f', 'f', 'f', 'f', 'f', 'f', -1], [-1, -1, 'g', 'g', 'g', 'g', -1, -1]]], [[-1, -1, 'a', 'a', 'a', 'a', -1, -1], [-1, 'c', 'c', 'c', 'c', 'c', 'c', -1], ['b', 'b', 'b', 'b', 'e', 'e', 'e', 'e'], ['d', 'd', 'f', 'f', 'd', 'd', 'd', 'd'], [-1, 0, 'f', 'f', 'g', 'g', 0, -1], [-1, -1, 'f', 'f', 'g', 'g', -1, -1]]]]]]
    result = find_second_order_lists(listik)
    print(result)