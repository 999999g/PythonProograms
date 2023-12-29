def double(a):
      if type(a) in [list,str,tuple,set,dict]:
         return len(a)
      else:
         return a
a=map(double,[1,(4,5),[7,9],{1:12}])
print(list(a))
