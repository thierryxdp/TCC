def colchao(medidas,H,L):
    A=medidas[0]
    B=medidas[1]
    C=medidas[2]
    if (H>=medidas[2] and L>=medidas[1]):
        return True
    if (L>=medidas[1] and H>=medidas[0]):
        return True
    if (L>=medidas[0] and H>=medidas[1]):
        return True
    else:
        False