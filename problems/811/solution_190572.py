def colchao(medidas,H,L):
    if medidas[0] <= L:
        return True
    if medidas[1] <= H and medidas[2] <= H:
        return True
    else:
        return False