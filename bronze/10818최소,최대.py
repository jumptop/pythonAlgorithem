# 들어갈 수 n과 배열을 담을 arr 생성
n = int(input())
arr = list(map(int, input().split()))

# 반복문을 통하여 0부터 n-1까지 반복시킴(n까지 반복시키면 arr[i+1]이 범위 초과됨) 이를 통하여 가장 큰 값은 가장 뒤로 빠지게 됨
for i in range(0, n-1):
    if arr[i] >= arr[i+1]:
        temp = arr[i]
        arr[i] = arr[i+1]
        arr[i+1] = temp
    else:
        continue

print(min(arr), end=" ")
print(arr[n-1]) # 사실 max(arr)해도 상관없지만 그냥 한번 해보고 싶었음