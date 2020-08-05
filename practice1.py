for i in range(10):
     print("hello world")


a=True
b=False
d=(not(a and b))
c=(a or b)
if d==c:
   print(d and c)
e=(a and b)
f=not(a or b)
if e==f:
   print(e or f)

def simplify():
    a = 2
    b = 2
    if (not(a<b)):
        print('yes')
    elif not(a>b):
        print('yes')
    else:
        return 


import random
def randoInt():
    a = int(input('Enter first number: '))
    b = int(input('Enter second number: '))
    x = random.randint(a,b)
    print(x)



import random
def randRa():
    a = int(input('Enter first number: '))
    b = int(input('Enter second number: '))
    #x = random.randint(a,b)
    if a and b in range(7):
        y = random.randrange(a,b)
        x = random.randrange(a,b)
        print('Random number: ','(', y,')',',','(', x,')' )
        print('Sum of Random numbers: ','(',y + x,')')
    else:
        print('no')



import math

t = int(input("T is: "))

e=2*t
d=3*t
pay = math.sin(e)
may = math.sin(d)

print(pay+may)


import math

t = int(input("Time is: "))
v0 = int(input("Velocity is: "))
x0 = int(input("Initial position is: "))
G = 9.80665
d = (x0 + v0 - G*t*2/2)


print(d)





