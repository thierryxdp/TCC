def colchao (medidas, H, L):
    areac = medidas[0]*medidas[1]*medidas[2]
    areap = H*L
    if areac >= areap:
        return True
    else:
        return False