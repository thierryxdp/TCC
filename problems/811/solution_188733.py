def colchao(medidas,H,L):
    (a,b,c)=medidas
    if a>H or a>L:
        return False
    elif b>H or b>L:
        return False
    else:
        return True