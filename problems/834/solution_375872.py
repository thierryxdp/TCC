def media_matriz(m):
    '''
    Esta função recebe uma matriz e retorna um valor float representando a média de todos os elementos
    da matriz fornecida.
    
    Parametros
    ----------
    m (list) : matriz
    '''
    b = len(m)*len(m[0])
    a = 0
    for i in m:
        for j in i:
            a += j
    return round(a/b, 2)