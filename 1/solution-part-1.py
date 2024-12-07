import numpy as np
file = np.loadtxt("input.txt")
col1, col2 = [], []

for inputs in file:
    col1.append(inputs[0])
    col2.append(inputs[1])
col1 = sorted(col1)
col2 = sorted(col2)
distance = 0

for num1, num2 in zip(col1, col2):
    distance += abs(num1 - num2)

print(distance)
# Answer is 1938424
