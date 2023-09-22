def eh_quadrada(matriz:list):
    '''Função que identifica e retorna se uma matriz é quadrada
    ou não. Vale ressaltar que a matriz deve, necessariamente,
    ser inserida em formato de lista.
    list -> bool'''
    if matriz == []:
        return True
    if len(matriz) == len(matriz[0]):
        return True
    else:
        return False