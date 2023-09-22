def media_matriz(matriz):
    nlinhas=len(matriz)
    ncolunas=len(matriz[indice])
    acumulador=0
    indice=0
    for lista in range(nlinhas):
        for elemento in range(ncolunas):
            acumulador=acumulador+elemento
            indice=indice+1
    return acumulador