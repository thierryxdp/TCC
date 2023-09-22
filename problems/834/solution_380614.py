def media_matriz(A):
    soma=0
    for i in range(len(A)):
        for j in range(len(A[0])):
            soma=soma + A[i][j]
    return soma/(len('oi')*len('oile'))