def media_matriz(matriz):
    soma=0
    media=0
    nlin=len(matriz)
    ncol=len(matriz[0])
    for i in range(nlin):
        for j in range(ncol):
              soma+=matriz[i][j]
            denominador=(range(lin)*range(ncol))
            media=soma/denominador
    return round(media,2)