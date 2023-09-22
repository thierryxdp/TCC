def colchao(medidas,H,L):
    if medidas[0] <= H and medidas[1] <= L:
        return True
    if medidas[0] <= H and medidas[2] <= L:
        return True
    if medidas[1] <= H and medidas[0] <= L:
        return True
    if medidas[1] <= H and medidas[2] <= L:
        return True
    if medidas[2] <= H and medidas[0] <= L:
        return True
    if medidas[2] <= H and medidas[1] <= L:
        return True
    else:
        return False