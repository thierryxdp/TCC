def colchudo(medidas, H, L):
    if medidas[0] <= L:
        return True
    if medidas[1] <= H:
        return True
    if medidas[2] <= L:
        return True
    else:
        return False