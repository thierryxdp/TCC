def eh_quadrada(matriz):
    '''Funcao que indentifica se uma matriz e quadrada
    list -> booleano
    '''
    x = len(matriz)
    y = len(matriz[0])
    if x == y:
        return True
    else:
        return False