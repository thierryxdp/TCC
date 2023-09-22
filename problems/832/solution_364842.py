def eh_quadrada(matriz):
    '''função para identificar se uma matriz é quadrada;
    list -> bool'''
    if len(matriz) == len(matriz[0]): #matriz vazia
        return True
    else:
        return False