def colchao(medidas,H,L):
	A = medidas[0]
    B = medidas[1]
    C = medidas[2]

    if H>= A and L>=B:
        return True
    if H>=B and L>=A:
        return True
    else:
        return False