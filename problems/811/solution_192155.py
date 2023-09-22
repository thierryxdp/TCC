def colchao(medidas,H,L):
    ''' ;
    list, int, int -> bool'''
    if medidas[0] > L and medidas[1] < H:
        return True
    elif medidas[0] < L and medidas[1] < H:
        return True
    elif medidas[1] > H and medidas[0] < H:
        return True
    else:
        return False