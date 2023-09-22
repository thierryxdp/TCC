def eh_quadrada(matriz):
    '''função responsável por responder se uma matriz é quadrada ou não'''
    A=[]
    if len(matriz)==len(matriz[0]) or matriz==A:
        return True
    else:
        return False