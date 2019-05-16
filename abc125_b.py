import numpy as np
n = int(input())
v = np.array([int(i) for i in input().split()])
c = np.array([int(i) for i in input().split()])

v_list = v - c
v_list = np.array(sorted(v_list, reverse=True))

ans = sum(v_list[v_list > 0])
print(ans)