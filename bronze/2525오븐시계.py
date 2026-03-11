a, b = map(int, input().split())
c = int(input())

# b(분) 값에 c(분)를 더함
b += c
#아래 모든 코드가 돌았는데 60보다 b가 크다면 여러번 돌림
while True:
    # 만약 b값이 60보다 작다면 즉시 멈춤
    if b < 60:
        break
    # 아니라면 a(시간)를 1 더하고 b값을 60분 빼줌
    a += 1
    b -= 60
    # 만약 시간이 24를 넘었다면 0으로 초기화해줌
    if a >= 24:
        a = 0

print(a, b)