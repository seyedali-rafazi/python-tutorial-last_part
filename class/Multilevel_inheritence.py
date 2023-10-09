class Animal:
    def __init__(self):
        self.age = 30
    def eat(self):
        print("eat")
       
class Fish(Animal):
    def swim(self):
        print("swim")
        
        
class Bird(Fish):
    pass
        