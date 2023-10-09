class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.z = x + y

    def __str__(self):
        return f"({self.x} , {self.y})"

    def draw(self):
        print(f"{self.x} , {self.y} , {self.z}")


point = Point(6, 7)
print(point)
