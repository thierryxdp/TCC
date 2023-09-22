def eh_quadrada(matriz):
    '''
    dada uma matriz como argumento, retorna True se for
    quadrada e false senao
    dados de entrada: list
    retorna: bool
    '''
    if len(matriz) == 0:
        return True
    elif len(matriz) != len(matriz[0]):
        return False
    else:
        return True