def colchao(medidas,H,L):
    if medidas[0] <= L and medidas[1] <= H :
        return medidas[0] <= L
    else :
        return medidas[2] > L