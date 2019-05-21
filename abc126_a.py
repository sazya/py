n, k = map(int, input().split())
#文字列.upper()
#文字列.lower()

s = str(input())
print(s[:k-1] + s[k-1].lower() + s[k:])