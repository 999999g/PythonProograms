class model:
    def _init_(self,a):
        self.a=a
    def _add_(self,other):
        return self.a+other.a
    
    def _sub_(self,other):
        return self.a-other.abcd
x = model(20)
y = model(40)