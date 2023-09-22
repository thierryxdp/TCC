def bolos(A,B,C):
    '''retorna o numero de bolos possiveis para se fazer com a quantidade de ingredientes disponilizados'''
    return int(min(A/2, B/3, C/5))