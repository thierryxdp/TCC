def media_matriz(matriz):
    qtd = 0
    soma = 0
    for i range(len(matriz)):
        for j in range(len(matriz[0])):
            soma += matriz[i][j]
             qtd +=1
    return round(soma/qtd,2)