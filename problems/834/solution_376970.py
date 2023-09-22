def media_matriz(matriz):
    for i in matriz:
        pos=0
        for j in i:
            pos+=matriz[j]
        return pos