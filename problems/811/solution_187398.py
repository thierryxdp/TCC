def colchao (medidas, H, L):
    '''Retorna False se a medida do colchão for maior que a porta e retorna true se a medida do colchão fpr menor que a porrta'''
    #list, float, float--> bool
    if medida[1] >= H:
        return False
    if medida[1] >= L:
        return False
    if medida[2] >= H:
        return False
    if medida[2] >= L:
        return False
    Else:
        True