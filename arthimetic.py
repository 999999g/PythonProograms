num=int(input('enter a number'))
option = int(input('enter option here'))
match option:
    case 1:
        print('operand 1')
        add = (2,4)
    case 2:
        print('operand 2')
        sub = (7,8)
    case 3:
        print('operand 3')
        mulity = (6,3)
    case _ :
        print('invalid option')
        divi = None
print(num)