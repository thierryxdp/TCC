def eh_quadrada(m):
    ''' Esta função verifica se a matriz é quadrada
    list -> bool'''
    return True if len(m) == 0 else len(m) == len(m[0])