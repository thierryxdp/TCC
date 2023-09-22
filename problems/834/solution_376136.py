def media_matriz (matriz):
    total = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            total = total + j
    return total/(i*j)