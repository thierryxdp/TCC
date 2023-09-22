def eh_quadrada(m):
    ''' Identifica se uma matriz é quadrada ou não;
    mat -> bool'''
    if m == []:
        return True
    if len(m) == len(m[0]):
        return True
    else:
        return False