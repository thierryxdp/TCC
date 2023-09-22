def eh_quadrada(matriz):
    '''Retorna um valor booleano que identifica se uma matriz é quadrada ou não;
    list(list) -> bool'''
    if len(matriz) == len(matriz[0]) or matriz == [[]]:
        return True
    else:
        return False