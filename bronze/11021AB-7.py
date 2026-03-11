# 정수입력
t = int(input())

# 입력받기 시작
for i in range(1, 1+t):
    a, b = map(int, input().split())
    print(f'Case #{i}: {a+b}')