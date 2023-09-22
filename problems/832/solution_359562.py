def eh_quadrada(matriz):
    '''Função que identifica se uma matriz é quadrada ou não.
   Parâmetros: list -> bool'''
    if matriz == []:
        return True
    nlin = len(matriz)
    ncol = len(matriz[0])
    for i in range(nlin):
        for j in range(ncol):
            if range(nlin) == range(ncol):
                return True
            else:
                return False