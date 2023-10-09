class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.z = x + y

    def draw(self):
        print(f"{self.x} , {self.y} , {self.z}")


point = Point(3, 5)
point.draw()

another = Point(8, 9)
another.draw()
