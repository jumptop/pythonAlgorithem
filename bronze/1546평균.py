M = int(input())
N = list(map(int, input().split()))
avg = 0
list_max = max(N)

for i in range(M):
    avg += N[i] / list_max * 100

print(avg / M)