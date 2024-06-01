import unittest
import shikaku_main


class TestShikakuSolver(unittest.TestCase):
    def test_txt_average_chart_3x3(self):
        result = main.get_grid_for_file("test18.txt")
        self.assertEqual([[[-1, 'b', -1], ['a', 'b', 'c'], [-1, 'b', -1]]], result)

    def test_txt_average_chart_4x4(self):
        result = main.get_grid_for_file("test2.txt")
        self.assertEqual([[[-1, 'c', 'c', -1], ['a', 'a', 'a', 'a'], [-1, 'b', 'b', -1]]], result)

    def test_txt_average_chart_5x5(self):
        result = main.get_grid_for_file("test3.txt")
        self.assertEqual([[[-1, 'f', 'f', 'f', -1], ['a', 'a', 'a', 'a', 'a'], ['g', 'g', 'd', 'd', 'd'],
                           ['c', 'c', 'c', 'c', 'e'], [-1, 'b', 'b', 'b', -1]]], result)

        result = main.get_grid_for_file("test4.txt")
        self.assertEqual([[[-1, 'b', 'd', 'c', -1], ['e', 'b', 'd', 'c', 'g'], ['e', 'f', 'd', 'c', 'g'],
                           ['e', 'f', 'd', 'c', 'a'], [-1, 'f', 'd', 'c', -1]]], result)

        result = main.get_grid_for_file("test5.txt")
        self.assertEqual([[[-1, 'a', 'a', 'a', -1], ['e', 'e', 'f', 'b', 'b'], ['e', 'e', 'f', 'b', 'b'],
                           ['e', 'e', 'd', 'd', 'd'], [-1, 'c', 'c', 'c', -1]]], result)

        result = main.get_grid_for_file("test8.txt")
        self.assertEqual([[[-1, 'a', 'a', 'a', -1], ['e', 'a', 'a', 'a', 'b'], ['e', 'a', 'a', 'a', 'b'],
                           ['d', 'd', 'd', 'd', 'b'], [-1, 'c', 'c', 'c', -1]]], result)

    def test_txt_average_chart_8x8(self):
        result = main.get_grid_for_file("test1.txt")
        self.assertEqual([[[-1, -1, 'a', 'a', 'a', 'a', -1, -1], [-1, 'c', 'c', 'c', 'c', 'c', 'c', -1],
                           ['b', 'b', 'b', 'b', 'e', 'e', 'e', 'e'], ['d', 'd', 'd', 'd', 'd', 'd', 'd', 'd'],
                           [-1, 'f', 'f', 'f', 'f', 'f', 'f', -1], [-1, -1, 'g', 'g', 'g', 'g', -1, -1]]], result)

        result = main.get_grid_for_file("test6.txt")
        self.assertEqual([[[-1, -1, -1, 'f', 'b', -1, -1, -1], [-1, -1, 'g', 'f', 'b', 'e', -1, -1],
                           [-1, 'a', 'g', 'n', 'n', 'n', 'n', -1],
                           ['h', 'h', 'g', 'k', 'k', 'l', 'l', 'l'], ['h', 'h', 'g', 'k', 'k', 'd', 'j', 'j'],
                           [-1, 'c', 'g', 'k', 'k', 'o', 'o', -1], [-1, -1, 'g', 'm', 'm', 'm', -1, -1],
                           [-1, -1, -1, 'i', 'i', -1, -1, -1]]], result)

    def test_txt_for_rectangle(self):
        result = main.get_grid_for_file("test19.txt")
        self.assertEqual([[['e', 'e', 'f', 'c', 'c', 'a'], ['e', 'e', 'f', 'c', 'c', 'a'],
                           ['b', 'b', 'b', 'c', 'c', 'a'], ['b', 'b', 'b', 'c', 'c', 'a'],
                           ['b', 'b', 'b', 'c', 'c', 'a'], ['d', 'd', 'd', 'd', 'd', 'a']]], result)

    # def test_txt_wrong_cells(self):
    #     result = get_grid_for_file("test10.txt")
    #     self.assertEqual(sys.exit(), result)

    # def test_txt_wrong_format(self):
    #     result = get_grid_for_file("test_text.txt")
    #     self.assertEqual(sys.exit(), result)

    def test_txt_for_5x3_3x5(self):
        result = main.get_grid_for_file("test16.txt")
        self.assertEqual([[[-1, 'a', -1], [-1, 'a', -1], ['b', 'b', 'b'], [-1, 'c', -1], [-1, 'c', -1]]], result)
        result = main.get_grid_for_file("test17.txt")
        self.assertEqual([[[-1, -1, 'c', -1, -1], ['a', 'a', 'c', 'b', 'b'], [-1, -1, 'c', -1, -1]]], result)

    def test_txt_multiple_solutions(self):
        result = main.get_grid_for_file("test14.txt")
        self.assertEqual([[['a', 'b'], ['a', 'b']], [['b', 'b'], ['a', 'a']]], result)
        result = main.get_grid_for_file("test15.txt")
        self.assertEqual([[[-1, -1, 'd', 'd', 'd', -1, -1], [-1, 'b', 'g', 'g', 'g', 'c', -1],
                           ['e', 'b', 'h', 'h', 'h', 'c', 'a'], [-1, 'b', 'i', 'i', 'i', 'c', -1],
                           [-1, -1, 'f', 'f', 'f', -1, -1]],
                          [[-1, -1, 'd', 'd', 'd', -1, -1], [-1, 'b', 'h', 'g', 'i', 'c', -1],
                           ['e', 'b', 'h', 'g', 'i', 'c', 'a'], [-1, 'b', 'h', 'g', 'i', 'c', -1],
                           [-1, -1, 'f', 'f', 'f', -1, -1]],
                          [[-1, -1, 'd', 'd', 'd', -1, -1], [-1, 'b', 'g', 'g', 'g', 'c', -1],
                           ['e', 'b', 'i', 'f', 'h', 'c', 'a'], [-1, 'b', 'i', 'f', 'h', 'c', -1],
                           [-1, -1, 'i', 'f', 'h', -1, -1]]], result)
