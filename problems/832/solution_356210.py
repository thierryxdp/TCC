def eh_quadrada(matriz):
    '''Função que, dada uma matriz, retorna True caso seja uma matriz quadrada e False, caso contrário; list(list) -> bool.'''
    if len(matriz) == 0:
        return True
    elif len(matriz) == len(matriz[0]):
        return True
    else:
        return False