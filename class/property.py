class Product:
    def __init__(self , price):
        self.price = price
               
    @property
    def price(self):
        return self.price
    
    @price.setter
    def price(self , value):
        if value < 10:
            raise ValueError("It is not can be negetive")
        self.price = value 

        
        
        
product = Product(-10)