def eh_quadrada(matriz):
    """ essa funçao retorna True se a matriz for quadrada, e false caso nao seja""" 
    if matriz == []:
        return True
    if len(matriz) == len(matriz[0]):
        return True
    else:
        return False