def eh_quadrada(m):
    """Função que recebe uma matriz e informa se ela
é quadrada ou não
signature: matrix --> bool
"""
    qli = len(m)
    qco = len(m[0])
    if qli == qco:
        return [True, qli, qco]
    if m == []:
    	return [True, qli, qco]
    else:
        return [False, qli, qco]