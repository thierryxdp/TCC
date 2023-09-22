def eh_quadrada(n):
    '''Função que identifica se uma matriz é quadrada.
    list ->bool'''
    if len(n)==len(n[0]):
        return True
    else:
        return False