class Baz(list):
    def append(self , object):
        print("append join")
        super().append(object)
        
        
mathlist = Baz()
mathlist.append(1)