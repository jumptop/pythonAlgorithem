print("몇줄: ", end=' ')
n = int(input())

# for i in range(0, n):
#     print(" " * i + "*" * (n-i))

#? 이걸 기대하고 만든게 아닌데 역피라미드가 되버림;;
for i in range(0, n):
    print(" " * i, end=' ')
    for j in range(0, n-i):
        print("*", end=' ')
    print("")