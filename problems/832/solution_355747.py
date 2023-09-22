def eh_quadrada(matriz):
    '''Retorna True se a matriz for quadrada e False caso não seja
    list -> bool'''
    if matriz == [[]]:
        return True
    if len(matriz) != len(matriz[0]):
        return False
    else:
        return True