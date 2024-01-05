class grand:
    
    
    def _init_(self,c):
        self.c=c
class derived(grand):

    def _init_(self,c,d,e):
        super()._init_(c)
        
        self.e=e
        self.d=d
        self.c=c

obj = derived()