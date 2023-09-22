def eh_quadrada(matriz):
    '''funçao que identifica se a matriz é quadrada;list -> bool'''
    if len(matriz) == len(matriz[0]):
        return True
    elif (matriz) == []:
        return True
    else:
        return False