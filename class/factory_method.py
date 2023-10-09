class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.z = x + y
        
    @classmethod
    def zero(cls):
        return Point(0 , 0)

    def draw(self):
        print(f"{self.x} , {self.y} , {self.z}")


point = Point.zero()
point.draw()

