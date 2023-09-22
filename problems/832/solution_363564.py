def eh_quadrada (matriz):
    ''' dada uma matriz, identifica se ela é ou não quadrada'''
    nlin=len(matriz)
    ncol=len(matriz[0])
    for i in range (nlin):
        for j in range(ncol):
            if nlin==ncol:
                return True
    return False