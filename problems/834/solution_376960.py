def media_matriz(matriz):
    pos=0
    soma=0
    for i in matriz:
        for j in i:            
        pos+=matriz[j]
    return pos