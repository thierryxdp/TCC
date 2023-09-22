def colchao (medidas, H, L):
    """ 
    list, int, int -> bool"""
    A = medidas[0]
    B = medidas[1]
    if A <= min (H,L) and B <= max (H,L):
        return True
    else:
        return False