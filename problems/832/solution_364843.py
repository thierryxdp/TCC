def eh_quadrada(matriz):
    '''função para identificar se uma matriz é quadrada;
    list -> bool'''
    if len(matriz) == 1 and len(matriz[0]) == 0:#matriz vazia
        return True
    else:
        return False