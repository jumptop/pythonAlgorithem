# 영수증에 적힌 총 금액 x와 구매한 물건의 종류 y, 모두 더한 값 all 생성
x = int(input())
y = int(input())
all = 0
# 이후 각 물건의 가격 a와 개수 b가 주어짐
for i in range(1, y+1):
    a, b = map(int, input().split())
    all += a * b

# 반복문이 끝난 이후 모두 더한값(all)과 총 금액(x)를 비교하여 Yes나 No 출력
if x == all:
    print("Yes")
else:
    print("No")
