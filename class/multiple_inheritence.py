class Animal:
    def eat(self):
        print("sham")
       
class Fish:
    def eat(self):
        print("nahar")
        
        
class Bird(Fish , Animal):
    pass
        
        
animal = Bird()
animal.eat()