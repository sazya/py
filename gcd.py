import time
import math


def gcd(a,b):
    if b>a:
        a, b = b, a
    while b:
        a, b = b, a%b
    return a

#-------
# Check math.gcd calculate time!

x = 98983245000060298253847985 
y = 467589090900298237

start = time.time()
print('math.gcd = ', math.gcd(x,y))
t = time.time() - start
print('math.gcd time:{0}:'.format(t) + '[s]')

def my_gcd(x, y):
    if x < y:
        xx = y
        yy = x
    else:
        xx = x
        yy = y

    while y > 0:
        r = x % y
        x = y
        y = r
    return x

starts = time.time()
print('my_gcd =   ', my_gcd(x,y))
tt = time.time() - starts
print('my_gcd time  :{0}:'.format(tt) + '[s]')
