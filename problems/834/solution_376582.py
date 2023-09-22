def media_matriz(matriz):
    soma = 0
    cont = 0
    for i in len(matriz):
        for j in len(matriz[0]):
            soma += matriz[i][j]
            cont += 1
    mdeia = soma/cont
    return round(media,2)