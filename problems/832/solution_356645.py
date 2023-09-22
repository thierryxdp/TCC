def eh_quadrada(matriz):
    '''funcao booleana que identifica se uma matriz e quadrada
    int->bool'''
    if matriz==[] or len(matriz)==len(matriz[0]):
        return True
    else:
        return False