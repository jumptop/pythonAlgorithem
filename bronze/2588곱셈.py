a = int(input())
b = int(input())
# int형 숫자 b를 문자열로 변환한 뒤, 각 자릿수를 정수로 나누어 리스트에 저장한다.
splitb = list(map(int, str(b)))

print(a * splitb[2])
print(a * splitb[1])
print(a * splitb[0])
print(a * b)