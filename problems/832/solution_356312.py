def eh_quadrada(matriz):
    '''Retorna uma função booleana que indentifica se uma dada matriz é quadrada
    list -> bool'''
    if matriz == []:
        return True
    elif len(matriz) == len(matriz[0]):
        return True
    else:
        return False