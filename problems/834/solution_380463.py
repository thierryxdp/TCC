def media_matriz(matriz):
    total = 0
    soma = 0
    for i in matriz:
        for j in matriz:
            total+=1
            soma+=matriz[i][j]
    return soma