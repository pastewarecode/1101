f = open("one_hundred.txt")

max_value = "101"
min_value = "1"

missing_numbers = []
all_numbers = set()

#takes all the numbers and splits it up and puts it into a set()
for line in f:
    if len(line) > 1:
        list_nums = line.split()
        for num in list_nums:
            all_numbers.add(int(num))

for r in range(int(min_value), int(max_value)):
    if r not in all_numbers:
        missing_numbers.append(r)             #run through all numbers to find and gather missing numbers together

#determines all the missing numbers
if missing_numbers:      
    for number in missing_numbers:
        print(f"{number} is missing")

#writes out missing numbers in another file
with open("one_hundred_sorted.txt", "w") as sortedFile:
    for number in missing_numbers:
        sortedFile.write(f"{number}\n")