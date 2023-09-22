def eh_quadrada(matriz):
    '''
    Função para identificar se uma matriz é quadrada;
    list(list) -> bool
    '''

    if len(matriz) == len(matriz[0]):
        return True
    elif matriz == []:
        return False
    else:
        return False