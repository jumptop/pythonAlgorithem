a, b, c = map(int, input().split()) # 주사위 값 받기
gold = 0 # 저장해놓을 돈

# 1번 경우, 3개가 다 같다면 10000 + 주사위눈 수 * 1000 값 출력
if a == b == c:
    gold = 10000
    gold += a * 1000
    print(gold)
# 2번 경우, 2개가 같다면 1000 + 같은 주사위의 눈 수 * 100값 출력
elif a == b or b == c:
    gold = 1000
    gold += b * 100
    print(gold)
elif a == c:
    gold = 1000
    gold += a * 100
    print(gold)
# 3번 경우, 3개가 다 다르다면 가장 큰 수 * 100값 출력
else:
    if a > b:
        if a > c : print(a * 100)
        else : print(c * 100)
    else :
        if b > c : print(b * 100)
        else : print(c * 100)