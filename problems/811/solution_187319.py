def colchao (medidas, H, L):
    """ 
    list, int, int -> bool"""
    A = medidas[0]
    B = medidas[1]
    if A < L and B < H:
        return True
    else:
        return False