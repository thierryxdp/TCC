def colchao(medidas,H,L):
    ''' ;
    list, int, int -> bool'''
    if medidas[0] < L and medidas[1] < H:
        return True
    else:
        return False