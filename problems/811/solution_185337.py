def colchao(medidas,H,L):
	if medidas[0] <= L:
        if medidas[1] <= H:
            return True
        elif medidas[2] <= H:
            return True
        else:
            return False