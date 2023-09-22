def eh_quadrada(matriz):
    '''retorna True se uma matriz for quadrada e False caso contrario
    list->bool'''
    if matriz==[]:
        return True
    elif len(matriz)==len(matriz[0]):
        return True
    else:
        return False