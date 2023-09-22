def media_matriz(matriz):
    soma = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            soma += matriz[i][j]
    qtd = len(matriz) + len(matriz[0])
    return round( soma / qtd, 2 )