def eh_quadrada(matriz):
    '''Identifica e retorna se a matriz dada é quadrada ou não.'''
    '''list->bool'''
    if len(matriz) == len(matriz[0]):
        return True
    elif [] in matriz:
        return True
    else:
        return False