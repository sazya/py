import numpy as np
s = str(input())
s_list = np.array([int(list(s)[i]) for i in range(len(s))])

if len(s_list) % 2 == 0:
    s01 = np.array([0,1]*(len(s_list)//2))
    s10 = np.array([1,0]*(len(s_list)//2))
else:
    s01 = np.array([0,1]*(len(s_list)//2))
    s01 = np.append(s01, 0)
    s10 = np.array([1,0]*(len(s_list)//2))
    s10 = np.append(s10, 1)

ans = min(np.sum(s_list == s01), np.sum(s_list == s10))
print(ans)

