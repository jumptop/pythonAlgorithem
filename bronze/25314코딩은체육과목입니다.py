# 문제의 정수
n = int(input())

# 4이상이라면 반복문을 적용하여 n의 수만큼 long을 출력, 4씩 증가하게 만들어 4마다 long 하나 출력하게 만듦
if n >= 4:
    for i in range(1, n + 1, 4):
        print("long ", end="")
print("int")