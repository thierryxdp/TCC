def colchao(medidas,H,L):
    if medidas[1]<H and medidas[2]<L:
        return True
    elif medidas[1]<L and medidas [2] < H:
        return True
    else:
        return False