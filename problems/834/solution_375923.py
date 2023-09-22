def media_matriz(matriz):
    indice=0
    nlinhas=len(matriz)
    ncolunas=len(matriz[0])
    acumulador=0
    for lista in range(nlinhas):
        for elemento in range(ncolunas):
            acumulador=acumulador+elemento
            indice=indice+1
    nelementos=nlinhas*ncolunas
    return acumulador/nelementos