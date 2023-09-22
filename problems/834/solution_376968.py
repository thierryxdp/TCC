def media_matriz(matriz):
    total=0
    numeros=0
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            total+=matriz[i][j]
            numeros+=1
    return total/numeros