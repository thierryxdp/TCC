def media_matriz(matriz):
    nlinhas=len(matriz)
    ncolunas=len(matriz[0])
    acumulador=0
    for lista in range(nlinhas):
        for elemento in lista:
            acumulador=acumulador+elemento
    return acumulador