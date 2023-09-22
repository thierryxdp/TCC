def eh_quadrada(matriz):
    nlin=len(matriz)
    ncol=len(matriz[0])
    for i in range(nlin):
        for j in range(ncol):
            if ncol==nlin:
                bol=True
            else:
                bol=False
    if matriz==[]:
        return True
    return bol