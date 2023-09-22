def colchao(medidas,H,L):
    A=medidas[0]
    B=medidas[1]
    C=medidas[2]
    if (H>=C and L>=B):
        return True
    if (L>=B and H>=A):
        return True
    if (L>=A and H>=B):
        return True
    else:
        False