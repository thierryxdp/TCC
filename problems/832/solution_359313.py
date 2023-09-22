def eh_quadrada(matriz:list)->bool:
    '''retorna True se a matriz é quadrada ou vazia'''
    if matriz == []:
        return True
    elif len(matriz) == len(matriz[0]):
        return True
    else:
        return False