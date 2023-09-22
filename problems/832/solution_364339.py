def eh_quadrada(matriz):
    """Essa funcao identifica se a matriz dada como entrada e quadrada
    list->bool"""
    if matriz==[]:
        return True
    nlin=len(matriz)
    ncol=len(matriz[0])
    for i in range(nlin):
        for j in range(ncol):
            if ncol==nlin:
                bol=True
            else:
                bol=False
    return bol