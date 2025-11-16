a = int(input())

for i in range(a):
    print(' ' * ((a - i) - 1), end="")
    print("*" * (2 * i+1))

for j in range(a):
    for x in range(a - j - 1):
        print(' ', end="")
    for y in range(2 * j + 1):
        print("*", end="")
    print()

for i in range(a):
    print(' ' * i, end='')
    print("*" * (2 * (a - i) - 1))