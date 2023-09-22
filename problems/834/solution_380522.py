def media_matriz(matriz):
    cont = 0
    soma = 0
    for l in range(len(matriz)):
        for c in range(len(matriz[l])):
            soma += matriz[l][c]
            cont += 1
    return soma/cont .00