def eh_quadrada(m):
    '''retorna se uma matriz é quadrada ou não;
    mat->bool'''
    
    if m == [] or len(m) == len(m[0]):
        return True
    else:
        return False