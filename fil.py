def fname(a):
    
    
        if 'A'<=a<='z':
            return True
        else:
            return False
      
out=filter(fname,"ab2c3Def12@#9z")     
print(list(out))
            
        