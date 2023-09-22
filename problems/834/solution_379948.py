def media_matriz(matriz):
    contador=0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            contador+=matriz[i][j]
    total_num=len(matriz)*len(matriz[0])
    return round(contador/total_num,2)