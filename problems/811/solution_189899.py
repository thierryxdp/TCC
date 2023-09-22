def colchao(medidas, H, L):
    medidas = medidas[A, B, C]
    if A <= H or A <= L:
        return True
    elif B <= H or B <= L:
        return True
    if C <= H or C <= L:
        return True
    else:
        return False