def colchao(medidas,H,L):
    ''' ;
    list, int, int -> bool'''
    if medidas[1] > L and medidas[0] < H:
        return True
    elif medidas[1] < L and medidas[0] < H:
        return True
    elif medidas[0] > H and medidas[1] < H:
        return True
    else:
        return False