def media_matriz(matriz):
    soma = 0
    for x in range(len(matriz)):
        for y in range(len(matriz[x-1])):
            soma += matriz[x-1][y-1]
    return soma/(len(matriz)*len(matriz[0]))