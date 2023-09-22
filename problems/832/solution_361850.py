def eh_quadrada(matriz):
    nlin=len(matriz)
    ncol=len(matriz[0])
    for i in range(nlin):
        for j in range(ncol):
            if nlin==ncol:
                return 'é quadrada'
    return 'não é quadrada'