def media_matriz(matriz):
    soma=0
    total=0
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            soma+=matriz[i][j]
            total+=1
    med=soma/total
    return round(med,2)