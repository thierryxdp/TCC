def media_matriz(matriz):
    x = 0
    y = 0
    z = 0
    for i in matriz:
        a = matriz[y]
        for j in i:
            z = z + a[x]
            x = x + 1
        y = y + 1
    return