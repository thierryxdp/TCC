def colchao(medidas,H,L):
    if medidas[2] and medidas[3] > H:
        return medidas[3]
    else:
        return medidas[2]