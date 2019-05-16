import sys
from functools import reduce

input = sys.stdin.readline

def gcd(a,b):
    if b>a:
        a, b = b, a
    while b:
        a, b = b, a%b
    return a

n = int(input())
a = [int(i) for i in input().split()]


ans = 0
l = [0]*(n+1)
r = [0]*(n+1)
for i in range(n):
    l[i+1] = gcd(l[i], a[i])
    r[n-i-1] = gcd(r[n-i], a[n-i-1])
for i in range(n):
    ans = max(ans, gcd(l[i], r[i+1]))
print(ans)