def eh_quadrada(matriz):
    '''
       Dada uma matriz retorna True se a matriz for quadrada
       ou retorna False se a matriz não for quadrada.
       list -> bool
    '''
    nlin = len(matriz)
    ncol = len(matriz[0])
    quadrada = True
    for i in range(nlin):
        if i == 0:
            quadrada = True
        for j in range(ncol):
            if i == j:
                quadrada = True
            if i != j:
                quadrada = False
    return quadrada