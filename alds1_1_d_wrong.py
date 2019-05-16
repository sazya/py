#n = int(input())
#nums = [int(input()) for _ in range(n)]
n = 12
nums = [5,4,4,8,2,3,2,4,1,3,4,3]

# 最小値とそのインデックスを得る
def min_index(list):
    return [i for i, x in enumerate(list) if x == min(list)]

# 最小値のインデックスでリストを分割したい
min_i = min_index(nums)

print("min_i = ", min_i)

if min_i[0] == (len(nums) - 1):
    print(max([nums[i+1] - nums[i] for i in range(len(nums)-1)]))
else:
    print('Lets Kill Da Ho!!!!!')
    # リストのリストの初期化はリスト内包表記を使う
    cuts = [[] * (len(min_i)) for i in range(len(min_i))]
    for i, t in enumerate(min_i):
        print(i, t)
        if i != len(min_i) - 1:
            cuts[i] = nums[min_i[i] : min_i[i+1]]
        else:
            cuts[i] = nums[min_i[i] : ]
        print("cuts[i] = ", cuts[i])   
    # リストの各要素リストへmax - min関数を適用したい
    def max_min(l):
        return max(l) - min(l)

    cuts_mm = list(map(max_min, cuts))
    print(max(cuts_mm))