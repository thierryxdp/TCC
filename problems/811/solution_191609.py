def colchao(medidas, H, L):
    '''dadas as medidas da porta e do colchao, 
    retorna true se passa pela porta, ou retorna
    False se nao passa pela porta
    list, float, float -> bool
    '''
    if medidas[1] <= H:
        return True
    if medidas[1] <= L:
        return True
    if medidas[2] <= H:
        return True
    if medidas[2] <= L:
        return True
    else:
        return False