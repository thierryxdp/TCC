def eh_quadrada(matriz):
    '''Identifique se uma matriz é quadrada ou não; sem list -> bool'''
    if matriz==[]:
        return True
    for i in range(len(matriz)):
            if len(matriz)==len(matriz[i]):
                return True
    else:
        return False