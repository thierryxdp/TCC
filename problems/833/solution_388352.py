def conta_numero(n, matrix):
    c = 0
    for i in range(len(matrix[0])):
        for j in range(len(matrix)):
            if n == matrix[i]:
                c +=1 
        return c