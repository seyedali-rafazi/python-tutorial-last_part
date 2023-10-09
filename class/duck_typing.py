from abc import ABC , abstractclassmethod

 #see polymorphism first
    
class TextBox:
    def draw(self):
        print("Textbox")
        
        
class DropDownList:
    def draw(self):
        print("DropDownList")
        
        
def draw(controls):
    for control in controls:
        control.draw()
    
ddl = DropDownList()
text = TextBox()
draw([ddl , text])