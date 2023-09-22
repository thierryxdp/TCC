def eh_quadrada(b):
    '''identifica se uma matriz é quadrada
    matriz -> bool'''
    if b == []:
        return True
    if len(b) == len(b[0]):
        return True
    else:
        return False