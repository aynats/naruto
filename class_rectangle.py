from class_point import Point


class Rect:
    def __init__(self, x: int, y: int, height: int, width: int):
        self.X = x
        self.Y = y
        self.Height = height
        self.Width = width

    def __str__(self):
        return f'(X: {self.X}, Y: {self.Y}, Width: {self.Width}, Height: {self.Height})'

    def __hash__(self):
        return (self.X, self.Y, self.Height, self.Width).__hash__()

    def __eq__(self, other):
        return self.X == other.X \
               and self.Y == other.Y \
               and self.Height == other.Height \
               and self.Width == other.Width

    def __copy__(self):
        return Rect(self.X, self.Y, self.Height, self.Width)

    def __deepcopy__(self, memo):
        return Rect(self.X, self.Y, self.Height, self.Width)

    def contain(self, point: Point):
        return self.X <= point.X <= self.X + self.Width - 1 and self.Y <= point.Y <= self.Y + self.Height - 1