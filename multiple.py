class multi:
    @ staticmethod
    def multi(a,b):
        return a+b
class divi:
    @ staticmethod
    def divi(a,b):
        return a-b
class cal(multi,divi):
    pass

obj = cal()
obj.multi(3,5)
obj.divi(2,3)
