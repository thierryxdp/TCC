def colchao(medidas,H,L):
    if L>=medidas[1] and H>=medidas[0]:
        return True
    elif L>=medidas[1] and H>=medidas[2]:
        return True
    elif L>=medidas[0] and H>=medidas[1]:
        return True
    else:
        return False