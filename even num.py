a=[1,2,3,4]
def add_int(var,i=0):
    if len(var)-1==i:
        return var[i]
    return var[i]+add_int(var,i+1)