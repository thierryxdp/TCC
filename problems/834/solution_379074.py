def media_matriz(matriz):
    
    soma = 0
    elementos = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            soma += matriz[i][j]
            elementos += 1
    return round((soma/elementos),2)