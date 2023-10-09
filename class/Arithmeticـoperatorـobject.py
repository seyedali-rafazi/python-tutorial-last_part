class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.z = x + y

    def __str__(self):
        return f"({self.x} , {self.y})"

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)


point = Point(6, 7)
another = Point(1, 3)
print(point + another)
