def eh_quadrada(matriz):
    '''Recebe uma matriz e retorna se ela é quadrada ou não.
    (list -> bool)'''
    if matriz[0] == None:
        return True
    if len(matriz) == len(matriz[0]):
        return True
    else:
        return False