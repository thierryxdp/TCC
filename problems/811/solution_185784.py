def colchao(medidas,H,L):
    if medidas[0] or medidas[1] or medidas[2] < H:
        if medidas[0] or medidas[1] or medidas[2] < L:
            return True
        else:
            return False
    else:
        return False