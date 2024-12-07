import re

with open("input.txt") as f:
    file = f.read().strip()
answer = 0
result = re.findall(("mul\(\d+,\d+\)"), file)
for entry in result:
    numbers = re.findall("\d+", entry)
    answer += int(numbers[0]) * int(numbers[1])
print(answer)
