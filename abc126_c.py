<<<<<<< HEAD
n, k = map(int, input().split())

ans = 0
for i in range(1, n+1):
    p = 1/n
    point = i
    while point < k:
        point *= 2
        p /= 2
    ans += p
=======
import math
n, k = map(int, input().split())

# 一回目でk以上の値が出る確率
if n >= k:
    p1 = (n - k + 1) / n
else:
    p1 = 0

# n面サイコロがkより小さい値だった場合

p3 = 0
while p3 >= 10:
    nc = math.ceil(math.log2(k/n))
    pp3 = (1/2)**nc * (1/n)
    p3 += pp3
    print(nn, nc, pp3)
ans = p1 + p3
>>>>>>> 50311b467f8d3f335d0e4a702bb6e62b32e9ad89
print(ans)