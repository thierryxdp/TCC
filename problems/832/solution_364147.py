def eh_quadrada(matriz):
    """ Funçao que identifica se uma matriz é quadrada"""
    
    nlin=len(matriz)
    ncol=len(matriz[0])
    
    for i in range(nlin):
        for j in range(ncol):
            if nlin==ncol:
                return True
    return False