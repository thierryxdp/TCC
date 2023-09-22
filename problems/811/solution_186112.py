def colchao(medidas,H,L):
    a,b,c=medidas
    if a>H or a>L:
        return False
    if b>H and b>L:
        return False
    else:
        return True