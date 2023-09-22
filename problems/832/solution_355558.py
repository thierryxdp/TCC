def eh_quadrada(matriz):
    """ função que verifica se a matriz é quadrada"""
    if (len(matriz) == len(matriz[0])) or matriz== []:
        return True
    else:
        return False