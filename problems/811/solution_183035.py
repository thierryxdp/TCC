def colchao(medidas,H,L):
    c = medidas[0]
    l = medidas[1]
    h = medidas[2]
    if medidas[1] > H and medidas[2] > L:
        return False
    else:
        return True