# 개인적으로 메모리 제한때문에 가장 빡셌던 문제인듯

import sys
input = sys.stdin.readline

N = int(input())
new_list = [0] * 10001

for i in range(N):
    new_list[int(input())] += 1

for j in range(1, 10001):
        for _ in range(new_list[j]):
            print(j)