with open("input.txt") as f:
    file = [list(map(int, line.split())) for line in f]

safe = 0
safe_list = []

for inputs in file:
    increase, decrease = False, False

    for index, number in enumerate(inputs):
        # If the index equals the length of list we are done with no interuptions its safe
        if index == len(inputs) - 1:
            safe += 1
            safe_list.append(1)
            continue

        # If the previous number is smaller than the next
        # And the previous number - next <=3 and >=1
        if (
            number < inputs[index + 1]
            and abs(number - inputs[index + 1]) <= 3
            and abs(number - inputs[index + 1]) >= 1
            and not decrease
        ):
            increase = True
            continue

        # If the previous number is smaller than the next
        # And the previous number - next <=3 and >=1
        elif (
            number > inputs[index + 1]
            and abs(number - inputs[index + 1]) <= 3
            and abs(number - inputs[index + 1]) >= 1
            and not increase
        ):
            decrease = True
            continue
        else:
            # Break conditions did not meet
            safe_list.append(0)
            break

print(safe) # Answer is 246
