def eh_quadrada(matriz):
    a=True
    for i in range(len(matriz)):
        if len(matriz[i])!=len(matriz):
            a=False
    return a