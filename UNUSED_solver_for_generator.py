# import threading
# from copy import deepcopy
# from class_point import Point
# from class_rectangle import Rect
#
# class TimeoutException(Exception):
#     pass
#
# class Solver:
#     def __init__(self, matrix):
#         self.matrix = matrix
#         self.dictionary_of_points = dict()
#         self.rows_count = len(matrix)
#         self.cols_count = len(matrix[0])
#         self.points_on_grid = self.get_start_points()
#         self.reserved_points = deepcopy(self.points_on_grid)
#         self.answer_matrix = deepcopy(self.matrix)
#         self.counter_reserved_rect = 1
#         self.determine_part_solve()
#         self.list_of_solutions = list()
#
#     def get_rect_various_bounds(self, point: Point) -> set:
#         number = self.matrix[point.Y][point.X]
#         rect_various = set()
#         for num in range(1, number + 1):
#             if number % num == 0:
#                 height = num
#                 width = number // num
#                 for i in range(max(0, point.X - width + 1), min(point.X + 1, self.cols_count - width + 1)):
#                     for j in range(max(0, point.Y - height + 1), min(point.Y + 1, self.rows_count - height + 1)):
#                         bounds = self.is_bound(i, j, height, width)
#                         if bounds:
#                             continue
#                         if not self.is_reserved_points_in_rect(Rect(i, j, height, width), point):
#                             rect_various.add(Rect(i, j, height, width))
#         return rect_various
#
#     def is_reserved_points_in_rect(self, rect: Rect, point: Point):
#         for reserved_point in self.reserved_points:
#             if rect.contain(reserved_point) and reserved_point != point:
#                 return True
#         return False
#
#     def is_bound(self, i, j, height, width) -> bool:
#         if i < 0 or j < 0 or i + width > len(self.matrix[0]) or j + height > len(self.matrix):
#             return False
#         for row in range(j, j + height):
#             for col in range(i, i + width):
#                 if self.matrix[row][col] == -1:
#                     return True
#         return False
#
#     def get_start_points(self):
#         points = set()
#         for x in range(self.cols_count):
#             for y in range(self.rows_count):
#                 if self.matrix[y][x] > 0:
#                     points.add(Point(x, y))
#         return points
#
#     def reserve_rectangle(self, rect: Rect, point: Point):
#         if point in self.points_on_grid:
#             self.points_on_grid.remove(point)
#         all_reserved_point_in_rect = set()
#         flag = (rect.X >= 0 or rect.Y >= 0
#                 or rect.X + rect.Width <= self.cols_count or rect.Y + rect.Height <= self.rows_count)
#         if flag:
#             for i in range(rect.X, rect.X + rect.Width):
#                 for j in range(rect.Y, rect.Y + rect.Height):
#                     self.answer_matrix[j][i] = chr(96 + self.counter_reserved_rect)
#                     all_reserved_point_in_rect.add(Point(i, j))
#         self.reserved_points = self.reserved_points | all_reserved_point_in_rect
#         self.counter_reserved_rect += 1
#
#         for conflict_point in self.dictionary_of_points.keys():
#             is_conflict = False
#             for rect in self.dictionary_of_points[conflict_point]:
#                 for reserved_point in all_reserved_point_in_rect:
#                     if rect.contain(reserved_point):
#                         self.dictionary_of_points[conflict_point].remove(rect)
#                         is_conflict = True
#                         break
#                 if is_conflict:
#                     break
#
#         if point in self.dictionary_of_points:
#             self.dictionary_of_points.pop(point)
#
#     def determine_part_solve(self):
#         count_only_possible_point_solutions = 1
#         while count_only_possible_point_solutions != 0:
#             for point in self.points_on_grid.copy():
#                 rect_various = self.get_rect_various_bounds(point)
#                 if len(rect_various) == 1:
#                     self.reserve_rectangle(list(rect_various)[0], point)
#                 else:
#                     self.dictionary_of_points[point] = rect_various
#             count_only_possible_point_solutions = 0
#             for point in self.points_on_grid:
#                 if len(self.dictionary_of_points[point]) == 1:
#                     count_only_possible_point_solutions += 1
#
#     def is_solution_impossible(self):
#         for point in self.points_on_grid:
#             if len(self.dictionary_of_points[point]) == 0:
#                 return True
#         return False
#
#     def get_solve_with_reserved_rect(self, rect: Rect, point: Point):
#         self.reserve_rectangle(rect, point)
#         self.determine_part_solve()
#         return self.main_solve()
#
#     def get_all_solves(self):
#         if len(self.points_on_grid) == 0:
#             return [deepcopy(self.answer_matrix)]
#         if self.is_solution_impossible():
#             return []
#         answers = []
#         unresolved_point = list(self.points_on_grid)[0]
#         for poss_rect in self.dictionary_of_points[unresolved_point]:
#             solver_copy = deepcopy(self)
#             try:
#                 ans = solver_copy.get_all_solves_with_reserved_rect(poss_rect, unresolved_point)
#                 answers.extend(ans)
#             except TimeoutException:
#                 continue
#         return answers
#
#     def get_all_solves_with_reserved_rect(self, rect: Rect, point: Point):
#         self.reserve_rectangle(rect, point)
#         self.determine_part_solve()
#         return self.get_all_solves()
#
#     def main_solve(self):
#         timer = threading.Timer(5, lambda: (_ for _ in ()).throw(TimeoutException))
#         timer.start()
#         try:
#             if len(self.points_on_grid) == 0:
#                 if [self.answer_matrix] not in self.list_of_solutions:
#                     self.list_of_solutions.append(self.answer_matrix)
#                     return self.list_of_solutions
#             if self.is_solution_impossible():
#                 return False
#             unresolved_point = list(self.points_on_grid)[0]
#             for poss_rect in self.dictionary_of_points[unresolved_point]:
#                 solver_copy = deepcopy(self)
#                 try:
#                     ans = solver_copy.get_solve_with_reserved_rect(poss_rect, unresolved_point)
#                     if ans:
#                         self.list_of_solutions.append(ans)
#                 except TimeoutException:
#                     continue
#             if len(self.list_of_solutions) != 0:
#                 return self.list_of_solutions
#             else:
#                 return False
#         except TimeoutException:
#             return False
#         finally:
#             timer.cancel()
