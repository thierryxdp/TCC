def media_matriz(mat):
    soma = 0
    soma1 = 0
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            soma = soma + mat[i][j]
    return soma/len(mat[i])*4