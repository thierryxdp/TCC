def media_matriz(matriz):
    total = 0
    soma = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            total+=1
            soma+=matriz[i][j]
    return (soma/total):,.2f