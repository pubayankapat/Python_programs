n = int (input())
matrix = []

for i in range(n):
    matrix.append([int(ele) for ele in input().split()])

for i in range(n):
    for j in range(n):
        if j < i:
            temp = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = temp

for i in range(n):
    print(matrix[i])