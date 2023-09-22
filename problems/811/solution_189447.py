def colchao(medidas,H,L):
    medida = medidas[0],medidas[1],medidas[2]
    if medidas[0]<=H and medidas[1]<=L:
        return True
    if medidas[1]<=H and medidas[2]<=L:
        return True