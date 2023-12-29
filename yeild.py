def sample(a):
    for i in range(0,len(a)):
     if a[i] in [1,[4,5,6,],{7,8},'efg',{'a':1},9.5,12]:
      yield a[i]
      yield i


out = sample('4,5')

print(out)
