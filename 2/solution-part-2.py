# Couple of things to know
# The difference between current and next number should be >= 1 and <=3
# The order should be either increasing or decreasing
# We can now tolerate a single failure point
#
# Solution
# Keep the existing logic from part 1
# For every failure append it to the failure list as a tuple
# consisting of (input: list, current_index: int, next_index: int)
#
# Now that we know of the problematic list and the position of the issue
# We can remove the current index and retry the list. If it passes continue
# If the list still have issue, delete the next index instead and try again
# If that passes continue else mark it as failure - do nothing
# If that fails then try the first index of the list (edge - case)


def fuck_off(lst: list, safe: int, fails: list):
    for inputs in lst:
        increase, decrease = False, False

        for index, number in enumerate(inputs):
            # If the index equals the length of list we are done with no interuptions its safe
            if index == len(inputs) - 1:
                safe += 1
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
                fails.append((inputs, index, index + 1))
                break

    return safe, fails


def filter_failures_with_extra_conditions(fails: list, safe: int):
    # pop = []
    for fail in fails:
        temp = fail[0].copy()
        del temp[fail[1]]
        safe_temp = safe
        safe, _ = fuck_off([temp], safe, [])

        if safe > safe_temp:
            # pop.append(fail)
            continue
        elif safe == safe_temp:
            temp = fail[0].copy()
            del temp[fail[2]]
            safe_temp = safe
            safe, _ = fuck_off([temp], safe, [])
            # if safe > safe_temp:
            #    pop.append(fail)

        if safe == safe_temp:
            temp = fail[0].copy()
            del temp[0]
            safe_temp = safe
            safe, _ = fuck_off([temp], safe, [])
            # if safe > safe_temp:
            #    pop.append(fail)

    # for p in pop:
    #    fails.remove(p)
    # with open("fails.txt", "w") as f:
    #    for line in fails:
    #        f.write(f"{ line }\n")
    return safe


def main() -> None:
    with open("input.txt") as f:
        file = [list(map(int, line.split())) for line in f]

    safe, fails = 0, []
    safe, fails = fuck_off(file, safe, fails)

    answer = filter_failures_with_extra_conditions(fails, safe)

    print(answer)  # Answer is 248


if __name__ == "__main__":
    main()
