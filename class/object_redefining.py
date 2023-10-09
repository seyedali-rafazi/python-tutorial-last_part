class Animal:
    def __init__(self):
        self.age = 30
        print("animal")
    def eat(self):
        print("eat")

        
        
class Fish(Animal):
    def __init__(self):
        super().__init__()
        self.weight = 99    
        print("fish")
    def swim(self):
        print("swim")
        
animal = Fish()
print(animal.age)
