def media_matriz(matriz):
    num=0
    contador=0
    for i in matriz:
        for aij in i:
            num = num + aij
            contador=contador + 1
    return num/contador