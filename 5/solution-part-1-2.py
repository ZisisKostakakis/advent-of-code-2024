with open("input-test-map.txt") as f:
    file_map = [list(map(int, line.split("|"))) for line in f]

with open("input-test.txt") as f:
    file = [list(map(int, line.split(","))) for line in f]

# For each map, split them and add them on a dictionary
# For each number create a key/value dictionary
# Each number should have the numbers it should be before and after
# {47: {'before': [53], 'after': []}, 53: {'before': [], 'after': [47]}}
mapping = {}
for map in file_map:
    if map[0] not in mapping.keys():
        num1 = {"before": [map[1]], "after": []}
        mapping[map[0]] = num1
    else:
        mapping[map[0]]["before"].append(map[1])

    if map[1] not in mapping.keys():
        num2 = {"before": [], "after": [map[0]]}
        mapping[map[1]] = num2
    else:
        mapping[map[1]]["after"].append(map[0])

total = 0
failed = []
for input in file:
    ordered = True
    for index, number in enumerate(input):
        if not ordered:
            break
        map = mapping[number]

        for n in input[:index]:
            if n in map["before"]:
                ordered = False
                failed.append(input)
                break

    if ordered:
        total += input[int((len(input) - 1) / 2)]
# ---------------------- part 2 below
total_fail = 0
for fail in failed:
    fail_copy = fail.copy()

    ordered = False
    while not ordered:
        ordered = True

        for index, number in enumerate(fail_copy):
            map = mapping[number]

            for n in fail_copy[index + 1 :]:
                if n in map["after"]:
                    misplaced_index = fail_copy.index(n)
                    fail_copy[misplaced_index], fail_copy[index] = (
                        fail_copy[index],
                        fail_copy[misplaced_index],
                    )
                    ordered = False

            for n in fail_copy[:index]:
                if n in map["before"]:
                    misplaced_index = fail_copy.index(n)
                    fail_copy[misplaced_index], fail_copy[index] = (
                        fail_copy[index],
                        fail_copy[misplaced_index],
                    )
                    ordered = False

    total_fail += fail_copy[int((len(fail_copy) - 1) / 2)]
print(total_fail)
