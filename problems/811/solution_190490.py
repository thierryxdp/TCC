def colchao(medidas,H,L):
    if min(medidas)<H or min(medidas)<L:
        return True
    elif max(medidas)>L or max(medidas)>H:
        return False
    else:
        return False