def media_matriz(matriz):
    x = 0
    y = 0
    for i in matriz:
        for j in i:
            x = x + i[y]
            y = y + 1
    return x/j