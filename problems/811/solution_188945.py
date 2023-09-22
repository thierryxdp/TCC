def colchao(medidas,H,L):
    [A ,B ,C] = medidas
    if medidas[1]=H:
        return True
    if medidas[1]<H:
        return True
    if medidas[2]<L:
        return True
    else:
        return False