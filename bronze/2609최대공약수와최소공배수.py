a, b = map(int, input().split())

max_int = max(a, b)
min_int = min(a, b)

la_max_int = max_int
la_min_int = min_int

remain = max_int % min_int

while (True):
    if remain == 0:
        greatest_common_divisor = min_int
        break

    max_int = min_int
    min_int = remain

    remain = max_int % min_int

lasts_common_divisor = (la_max_int * la_min_int) / (greatest_common_divisor)

print(greatest_common_divisor)
print(int(lasts_common_divisor))

