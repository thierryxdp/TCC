def media_matriz(matriz):
    soma=0
    x=len(matriz)
    y=len(matriz[0])
    for i in range(x):
        for j in range(y):
            z=matriz([i][j])
            soma=soma+z
    media = (soma/x*y)
    return "%.2f" % media