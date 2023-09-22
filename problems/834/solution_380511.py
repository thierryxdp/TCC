def media_matriz(matriz):
    soma = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            soma = soma + matriz[i][j]
    matriz = len(matriz[0]) + len(matriz[1]) + len(matriz[2]) + len(matriz[3]) + len(matriz[4])
    media = soma / matriz
    return media