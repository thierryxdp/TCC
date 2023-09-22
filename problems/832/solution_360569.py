def eh_quadrada(matriz):
    '''função responsável por responder se uma matriz é quadrada ou não'''
    if len(matriz)==len(matriz[0]):
        return True
    if matriz==[]:
        return True
    else:
        return False