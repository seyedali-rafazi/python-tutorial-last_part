
class Person:
    def __init__(self , name ,age):
        self.name = name.capitalize()
        self.age = age
        
    @property
    def esm(self):
        return self.__name
    @esm.setter
    def esm(self , name):
        self.__name = name
        
    @property
    def sen(self):
        return self.__age
    @sen.setter
    def sen(self , age):
        self.__age = age
        
        
humanone = Person("ali" , 22)
print(f"your name is {humanone.name} and your age is {humanone.age}")
    