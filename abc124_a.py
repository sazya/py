a, b = map(int, input().split())
a1 = a
a2 = a-1
b1 = b
b2 = b-1

if a == b:
    ans = a1 + b1
elif a > b:
    ans = a1 + a2
elif b > a:
    ans = b1 + b2
print(ans) 
