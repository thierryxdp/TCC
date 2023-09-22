def media_matriz(matriz):
    soma = 0
    for i in range(0,len(matriz)):
        for j in range(0,len(matriz[0])):
            soma += matriz[i][j]
    media = soma/(len(m)+len(matriz[0]))
    return media