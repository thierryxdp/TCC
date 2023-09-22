def eh_quadrada(matriz):
    ''' Essa funcao nos diz se uma matriz e quadrada;list->bool'''
    if len(matriz)==[]:
        return True
    if len(matriz) == len(matriz[0]):
        return True
    else:
        return False