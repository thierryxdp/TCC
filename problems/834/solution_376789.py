media_matriz(matriz):
    soma=0
    qtd=0
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            soma+=matriz[i][j]
            qtd+=1
    return soma/qtd