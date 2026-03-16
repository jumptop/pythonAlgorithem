N, M = map(int, input().split())
card = list(map(int, input().split()))
add = 0
is_not = 0

for i in range(N):
    for j in range(i+1, N):
        for x in range(j+1, N):
            add = card[i] + card[j] + card[x]

            if add <= M:
                if add > is_not:
                    is_not = add

print(is_not)