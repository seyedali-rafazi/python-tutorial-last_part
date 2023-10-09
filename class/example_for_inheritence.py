from abc import ABC , abstractclassmethod

class InvalidOporationEror(Exception):
    pass


class Stream(ABC):
    def __intit__(self):
        self.opened = False
        
    def open(self):
        if self.opened:
            raise InvalidOporationEror("Your clasd is opened")
        self.opened = True
       
    def close(self):
        if not self.opened:
            raise InvalidOporationEror("Your clasd is closed")
        self.opened = False     
    
    @abstractclassmethod
    def read(self):
        pass
    
class Filestream(Stream):
    def read(self):
        print("Reading data from file")
        
        
class Networkstream(Stream):
    def read(self):
        print("Reading data from Network")
        
        
class Memorystream(Stream):
    def read(self):
        print("Reading data from Memorystream")        
        
stream = Memorystream()