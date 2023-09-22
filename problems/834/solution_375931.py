def media_matriz(matriz):
    nlinhas=len(matriz)
    ncolunas=len(matriz[0])
    nelementos=nlinhas*ncolunas
    acumulador=0
    indice1=0
    media=acumulador/nelementos
    while indice1<nlinhas:
        indice2=0
        while indice2<ncolunas:
            acumulador=acumulador+matriz[indice1][indice2]
            indice2=indice2+1
        indice1=indice1+1
    return round(media,2)