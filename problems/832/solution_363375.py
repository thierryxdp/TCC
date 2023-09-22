def eh_quadrada(m):
    ''' identifica se a matriz é quadrada ou não.
    list(list) --> bool'''
    
    # se a matriz é vazia, então é quadrada
    if m == list():
        return True
    
    n = len(m)
    m = len(m[0])
    
    return n == m