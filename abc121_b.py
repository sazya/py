import numpy as np
n,m,c = map(int, input().split())
b = np.array([int(i) for i in input().split()])
ans = 0
for ii in range(n):
    a = np.array([int(i) for i in input().split()])
    if (np.dot(a,b) + c) > 0:
        ans += 1
print(ans)
