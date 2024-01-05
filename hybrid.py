class multi3:
    @ staticmethod
    def multi3 (a,b,c):
        return a*b*c
class multi2:
    @ staticmethod
    def multi(a,b):
        return a*b
class multi(multi2,multi3):
    pass
class divi2:
    @ staticmethod
    def divi(a,b):
        return a%b
class cal(multi,divi2):
    pass
obj = cal()
obj.multi(4,5)
obj.divi(2,4)