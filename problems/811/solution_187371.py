def colchao(medidas, H, L):
    if medidas[0] <= H or medidas[0] <= L:
        return True
    if medidas[1] <= H or medidas[1] <= L:
        return True
    if medidas[2] <= H or medidas[2] <= L:
        return True
    else:
        return False