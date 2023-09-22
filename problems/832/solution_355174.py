def eh_quadrada(b):
    '''identifica se uma matriz é quadrada
    list(list) -> bool'''
    if len(b) == len(b[0]):
        return True
    else:
        return False