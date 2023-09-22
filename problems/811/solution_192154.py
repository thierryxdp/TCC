def colchao(medidas,H,L):
    ''' ;
    list, int, int -> bool'''
    if medidas[0] > L:
        return False
    elif medidas[1] > H:
        return False
    else:
        return True