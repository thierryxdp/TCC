def colchao(medidas,H,L):
    if medidas[0] <= L and (medidas[1] or medidas[2] <= H):
        return True
    else:
        return False