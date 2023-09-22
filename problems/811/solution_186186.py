def colchao2(medidas,H,L):
    if H>=medidas[1]:
        return True
    elif H>=medidas[2]:
        return True
    elif L>=medidas[1]:
        return True
    elif L>=medidas[2]:
        return True
    else:
        return False