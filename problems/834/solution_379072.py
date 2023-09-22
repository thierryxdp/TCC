def media_matriz(matriz):
    
    soma = 0
    elementos = (len(matriz))*(len(matriz[0]))
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            soma += matriz[i][j]
        return round((soma/elementos),2)