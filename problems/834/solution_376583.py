def media_matriz(matriz):
    soma = 0
    cont = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[0]0):
            soma += matriz[i][j]
            cont += 1
    mdeia = soma/cont
    return round(media,2)