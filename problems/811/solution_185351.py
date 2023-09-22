medidas = [A,B,C]
def colchao(medidas,H,L):
    if medidas[1] or medidas[2] > H or L:
        return True
    else:
        return False