def eh_quadrada(m):
    '''Função que identifica se uma matriz é quadrada ou não.
    list(list) -> bool'''
    if m == [] or len(m) == len(m[0]):
        return True
    else:
        return False