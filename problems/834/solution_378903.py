def media_matriz(matriz):
    x = 0
    y = 0
    z = 0
    for i in matriz:
        a = matriz[y]
        z = z + a[x]
        for j in i:
            x = x + 1
        y = y + 1
    return