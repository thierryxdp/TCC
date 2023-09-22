def colchao(medidas,H,L):
	n = (medidas[0] <= L) and (medidas[1] or medidas[2] <= H)
    return n