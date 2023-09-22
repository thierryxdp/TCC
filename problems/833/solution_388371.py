def conta_numero(n, matrix):
    c = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            c += 1 if n == matrix[i][j] else 0
    return c