media_matriz(matriz):
    somatorio = 0
    elementos = 0
    for i in range(len(matriz)):
        somatorio += sum(matriz[1])
        elementos += len(matriz[i])
        media = round(somatorio / elementos, 2)
    return media