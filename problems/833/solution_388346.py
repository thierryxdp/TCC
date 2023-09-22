def num_count(n, matrix):
    c = 0
    for i in range(len(matrix[0])):
        for j in range(len(matrix)):
            c += 1 if n == matrix[i][j] else 0
    return c