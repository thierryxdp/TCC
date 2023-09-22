def media_matriz(mat):
    qtd=0
    soma=0
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            soma+=mat[i][j]
            qtd+=1
    return round(soma/qtd,2)