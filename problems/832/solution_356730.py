def eh_quadrada(matriz):
    '''Retorna True se a matriz for quadrada e False se não for
      list -> bool'''
    if matriz == []:
        return True
    elif len(matriz) == len(matriz[0]):
        return True
    else:
        return False