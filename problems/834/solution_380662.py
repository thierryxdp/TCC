def media_matriz(matriz):
    qtd = len(matriz)*len(matriz[0])
    soma = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            soma += matriz[i][j]
    media = soma/qtd
    return media