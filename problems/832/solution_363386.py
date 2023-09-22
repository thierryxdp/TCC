def eh_quadrada(m):
    '''indica se a matriz é ou não quadrada'''
    if m == list():
        return True
    
    n= len(m)
    m= len(m[0])
    
    return n == m