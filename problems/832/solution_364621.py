def eh_quadrada(m):
    """Função que recebe uma matriz e informa se ela
é quadrada ou não
signature: matrix --> bool
"""
    qli = len(m)
    qco = len(m[0])
    if qli == qco or qli and qco == 0:
        return True
    else:
        return False