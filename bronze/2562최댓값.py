# 숫자들을 담아줄 빈 배열 arr을 생성
arr = []

# 9개의 숫자들을 append 함수로 받아줌
for i in range(0, 9):
    arr.append(int(input()))

# 받은 수들을 하나하나 arr의 가장 큰 수와 비교, 일치하면 최대값을 출력하고 0번부터 시작하는 배열의 특성에 맞춰 현재 배열+1을 하여 몇번째 수인지 출력
for j in range(0, 9):
    if arr[j] == max(arr):
        print(max(arr))
        print(j+1)
        break