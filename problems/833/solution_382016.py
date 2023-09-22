def conta_numero(n,matriz):
    """Determina se uma matriz é ou não uma matriz quadrada
       lista ~> bool"""
    num = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            elemento = matriz[i][j]
            if elemento == n:
                num += 1
    return num