n = int(input())
nums = [int(i) for i in input().split()]
ans = 0
while True:
    if [i for i in nums if i % 2 == 1]