def media_matriz(A):
    for i in range(len(A)):
        soma = 0
        for j in range(len(A[0])):
            soma += A[i][j]
    return soma