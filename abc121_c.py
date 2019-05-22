import numpy as np
n,m = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(n)]
ans = 0

#>>> l
#[[1, 2, 3], [3, 2, 1], [2, 3, 1]]
#>>> l.sort()
#>>> l
#[[1, 2, 3], [2, 3, 1], [3, 2, 1]]

# リスト同士の順番は、最初に異なったリスト要素の大小できまる
# 今回はAの安い順にソートするので、
A.sort()
sum_b = 0
while sum_b = m:
