def eh_quadrada(matriz):
    '''
    Função para identificar se uma matriz é quadrada;
    list(list) -> string
    '''

    if matriz == []:
        return True
    elif len(matriz) == len(matriz[0]):
        return True
    else:
        return False