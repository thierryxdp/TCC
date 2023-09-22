def eh_quadrada(m):
    ''' retorna se uma matriz é quadrada ou não.
    list(list) --> bool '''
    
    if m == list():
        return True
    
    m = len(m)
    m = len(m[0])
    
    return m == m