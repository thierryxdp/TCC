def colchao(medidas,H,L):
    A = medidas[0]
	B = medidas[1]
	C = medidas[2]
	if C < L:
    	return True
    elif C < H and B < L:
        return True
    elif C + B < L + H
    	Return True
    else:
        return False