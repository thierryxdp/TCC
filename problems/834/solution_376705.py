def media_matriz(matriz):
    soma=0
    x=len(matriz)
    y=len(matriz[0])
    for i in range(x):
        for j in range(y):
            soma=soma+(matriz([i][j]))
    media = (soma/x*y)
    return "%.2f" % media