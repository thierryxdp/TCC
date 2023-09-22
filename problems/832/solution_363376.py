def eh_quadrado (m):
    ''' list (list) --> bool'''
    if m == list():
        return True 
    
    n = len(m)
    m = len(m[0])
    
    return n == m