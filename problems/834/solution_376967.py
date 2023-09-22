def media_matriz(matriz):

    soma = 0
    quantNum = 0

    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            soma += matriz[i][j]
            quantNum += 1

    return round(soma/quantNum,2)