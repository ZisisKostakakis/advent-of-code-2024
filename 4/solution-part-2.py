total = 0
with open("input.txt") as f:
    file = f.read()

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
        if char in ["M", "S"]:
            try:
                left, right = char, a[index][index_row+2]
            except IndexError:
                continue
            count = 1

            #if index == 0 and index_row == 1:
            #    breakpoint()

            for i in range(index + 1, index + 3):
                try:
                    if index_row + count <= len(row) and index + count <= len(row):
                        left += a[i][index_row + count]
                except IndexError:
                    left = ""
                try:
                    if index_row + 2 - count >= 0 and index + count <= len(row):
                        right += a[i][index_row + 2 - count]
                except IndexError:
                    right = ""

                count += 1

            if left in ["MAS", "SAM"]:
                if right in ["MAS", "SAM"]:
                    #print("X-MAX found at ", index, index_row)
                    total += 1
print(total)
