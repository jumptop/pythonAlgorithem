a = int(input())

for i in range(a):
    print("*" * (i+1))

for j in range(a):
    print(" " * (a - (j+1)), end="")
    print("*" * (j+1))