def eh_quadrada(matriz):
    '''função responsável por responder se uma matriz é quadrada ou não'''
    A=[]
    if matriz==[]:
        return True
    if len(matriz)==len(matriz[0]):
        return True
    else:
        return False