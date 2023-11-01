f = open("one_hundred.txt")

max_value = ""
min_value = "99999"

for line in f:
    if len(line) > 1:
        list_nums = line.split()
        for num in list_nums:
            if num < min_value:
                min_value = num
            if num > max_value:
                max_value = num

print(f"{min_value}, {max_value}")
f.seek(0)

for line in f:
    if len(line) > 1:
        list_nums = line.split()
        for num in list_nums:
            for r in range(int(min_value), int(max_value)):
                if r != num:
                    print(f"{r} is not present")