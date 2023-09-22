def eh_quadrada(matriz:list)->bool:
    '''retorna True se a matriz é quadrada ou vazia'''
    if len(matriz) == len(matriz[0]):
        return True
    elif matriz == []:
        return True
    else:
        return False