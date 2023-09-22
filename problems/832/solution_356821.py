def eh_quadrada(matriz):
    '''Dada uma matriz, retorna True se for quadrada e False se não for.
    list -> bool'''
    if len(matriz) != len(matriz[0]):
        return False
    else:
        return True