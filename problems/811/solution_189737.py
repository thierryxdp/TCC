def colchao(medidas,H,L):
    if medidas[0] <= L and medidas[1] <= L or medidas[2] <= H and medidas[0] <= L or medidas[2] <= H and medidas[1] <= L:
        return True
    else:
        return False