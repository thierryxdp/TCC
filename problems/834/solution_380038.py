def media_matriz(matriz):
    soma= 0
    for x in range(len(matriz)):
        for y in range(len(matriz[0])):
            soma += matriz[x][y]
            i += 1
    return soma