from abc import ABC , abstractclassmethod

class UIcontrol(ABC):
    @abstractclassmethod
    def draw(self):
        pass
    
class TextBox(UIcontrol):
    def draw(self):
        print("Textbox")
        
        
class DropDownList(UIcontrol):
    def draw(self):
        print("DropDownList")
        
        
def draw(controls):
    for control in controls:
        control.draw()
    
ddl = DropDownList()
text = TextBox()
draw([ddl , text])