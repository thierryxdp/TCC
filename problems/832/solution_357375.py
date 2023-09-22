def eh_quadrada(matriz):
    '''A função recebe uma matriz e retorna se é quadrada (True) ou não (False).
    list -> bool'''
    if matriz==[]:
        return True
    else:
        nlin=len(matriz)
        ncol=len(matriz[0])
        if nlin==ncol:
            return True
        else:
            return False