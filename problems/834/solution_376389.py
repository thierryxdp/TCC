def media_matriz(matriz):
    numeros = 0
    soma = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            soma += matriz[i][j]
            numeros += 1
    return round(soma/numeros, 2)