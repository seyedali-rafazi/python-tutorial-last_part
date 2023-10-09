class Point:
    defualt_color = "red"

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.z = x + y

    def draw(self):
        print(f"{self.x} , {self.y} , {self.z}")


point = Point(3, 5)
point.defualt_color = "blue"

another = Point(8, 9)
another.defualt_color = "green"


print(point.defualt_color)
print(another.defualt_color)
print(Point.defualt_color)
