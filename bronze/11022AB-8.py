# 테스트 케이스
t = int(input())

# 반복문
for i in range(1, t+1):
    a, b = map(int, input().split())
    print(f'Case #{i}: {a} + {b} = {a+b}')