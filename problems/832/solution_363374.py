def eh_quadrada(m):
    ''' identifica se a matriz é quadrada ou não.
    list(list) --> bool'''
    
    n = len(m)
    m = len(m[0])
    
    return n == m