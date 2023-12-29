a='ABCDEF'
b={a[i]:i for i in range(len(a)) if i%2==0}
print(a,b)