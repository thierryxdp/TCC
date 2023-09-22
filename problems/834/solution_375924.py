def media_matriz(matriz):
    nlinhas=len(matriz)
    ncolunas=len(matriz[0])
    nelementos=nlinhas*ncolunas
    acumulador=0
    
    
    for lista in range(nlinhas):
        for elemento in range(ncolunas):
            acumulador=acumulador+elemento
    return acumulador/nelementos