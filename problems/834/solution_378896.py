def media_matriz(matriz):
    x = 0
    y = 0
    z = 0
    for i in matriz:
        for j in i:
            a = matriz[y]
            z = z + a[x]
            x = x + 1
        y = y + 1
    return z/x