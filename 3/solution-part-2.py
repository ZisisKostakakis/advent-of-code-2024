import re

with open("input.txt") as f:
    file = f.read()
answer = 0

result = re.findall((r"(?:do\(\)|don't\(\)).*?mul\(\d+,\d+\)|mul\(\d+,\d+\)"), file)
enable = True
disable = False
for entry in result:
    if "don't" in entry:
        print("Skip", entry)
        disable = True
        enable = False
        continue

    if "do" in entry:
        print("Do", entry)
        res = re.findall(r"mul\(\d+,\d+\)", entry)
        numbers = re.findall("\d+", res[0])
        answer += int(numbers[0]) * int(numbers[1])
        enable = True
        disable = False
        continue

    if enable:
        print("Default", entry)
        numbers = re.findall("\d+", entry)
        answer += int(numbers[0]) * int(numbers[1])

print(answer)
