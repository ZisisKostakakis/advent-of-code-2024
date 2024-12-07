import re

total = 0
with open("input.txt") as f:
    file = f.read()

# For each row, find the XMAS | SAMX values
result = re.findall((r"SAMX"), file)
total += len(result)
result = re.findall((r"XMAS"), file)
total += len(result)

a = []
temp = []
for f in file:
    if "\n" in f:
        a.append(temp)
        temp = []
        continue
    temp.append(f)
# For each character, check the next 3 rows on the -+1 index
for index, row in enumerate(a):
    for index_row, char in enumerate(row):
        if char in ["X", "S"]:
            right, left, down = char, char, char
            count = 1
            #if index == 2 and index_row == 3:
            #    breakpoint()

            for i in range(index + 1, index + 4):
                try:
                    if index_row - count >= 0 and index + count <= len(row):
                        left += a[i][index_row - count]
                except IndexError:
                    left = ""
                try:
                    if index_row + count <= len(row) and index + count <= len(row):
                        right += a[i][index_row + count]
                except IndexError:
                    right = ""
                try:
                    down += a[i][index_row]
                except IndexError:
                    down = ""

                count += 1
            if right in ["XMAS", "SAMX"]:
                #print("right diagonal at ", index, index_row, right)
                total += 1
            if left in ["XMAS", "SAMX"]:
                #print("left diagonal", index, index_row, left)
                total += 1
            if down in ["XMAS", "SAMX"]:
                #print("down", index, index_row, down)
                total += 1
print(total)
