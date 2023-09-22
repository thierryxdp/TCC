def eh_quadrada(m):
    '''verifica se a matriz é quadrada'''
    if m == list():
        return True
    n = len(m)
    m = len(m[0])
    
    return n == m