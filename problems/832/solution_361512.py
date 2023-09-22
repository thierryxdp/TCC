def eh_quadrada(matriz):
    """ a função recebe uma matriz e retorna se ela é quadrada
    ou não 
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