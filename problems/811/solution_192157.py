def colchao(medidas,H,L):
    ''' ;
    list, int, int -> bool'''
    if medidas[1] < L and medidas[0] < H:
        return True
    else:
        return False