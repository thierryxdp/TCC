def colchao(medidas,H,L):
    if medidas[1] > H:
        return False
    if medidas[1] > L:
        return False
    if medidas[2] > H:
    	return False
    if medidas[2] > L:
    	return False
    if medidas[1] < H:
        return True
    if medidas[1] < L:
        return True
    if medidas[2] < H:
        return True
    if medidas[2] < L:
        return True