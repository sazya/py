s = str(input())
ans1 = s[::2].count('0') + s[1::2].count('1')
ans2 = s[::2].count('1') + s[1::2].count('0')
print(min(ans1, ans2))
