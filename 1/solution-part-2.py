import numpy as np
file = np.loadtxt("input.txt")
col1, col2 = [], []

for inputs in file:
    col1.append(inputs[0])
    col2.append(inputs[1])
col1 = sorted(col1)
col2 = sorted(col2)
similarity_score = 0

for num1 in col1:
    similarity_score += col2.count(num1) * num1

print(similarity_score)
# Answer is 22014209
