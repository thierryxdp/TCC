def colchao (medidas, H, L):
    '''Retorna False se a medida do colchão for maior que a porta e retorna true se a medida do colchão fpr menor que a porrta'''
    #list, float, float--> bool
    if medidas[1] >= H:
        return False
    if medidas[1] >= L:
        return False
    if medidas[2] >= H:
        return False
    if medidas[2] >= L:
        return False
    else:
        True