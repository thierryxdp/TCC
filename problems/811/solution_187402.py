def colchao (medidas, H, L):
    '''Retorna False se a medida do colchão for maior que a porta e retorna true se a medida do colchão for menor que a porta'''
    #list, float, float--> bool
    if medidas[1] <= H:
        return True
    if medidas[1] <= L:
        return True
    if medidas[2] <= H:
        return True
    if medidas[2] <= L:
        return True
    else:
        False