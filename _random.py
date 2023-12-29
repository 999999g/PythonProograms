import random

num = random.randint(300,600)
 
while True:
    a= int(input('enter a number:-'))
    if a == num:
        print('congrates! you succesfully gussed the number',num)
        break 
    elif a < num:
        print('enter greater number')
    elif a > num:
        print('enter lesser number')