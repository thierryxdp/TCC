def eh_quadrada(matriz):
    '''função para identificar se uma matriz é quadrada;
    list -> bool'''
    for linha in matriz:
        if matriz == []:
            return True
        else:
            if len(matriz) == len(matriz[0]):
                return True
            else:
    return False