# 入出力
import sys
input = sys.stdin.readline

# 改行で連続している可変長入力(n個とする)
n = int(input())
nums = [int(input()) for _ in range(n)]

# 最小値とそのインデックスを得る
def min_index(list):
    return [i for i, x in enumerate(list) if x == min(list)]

# リストのリストの初期化はリスト内包表記を使う
ll = [[] * 4 for _ in range(4)]
