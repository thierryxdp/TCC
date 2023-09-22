def eh_quadrada(m):
    ''' Essa função identifica se determinada matriz
    é quadrada;
    list -> bool. '''
    if m == list():
        return True
    n = len(m)
    m = len(m[0])
    resultado = n == m
    return resultado