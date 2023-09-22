def colchao(medidas,H,L):
	G = []
    G.append(H)
    G.append(L)
    A = medidas[0]
	B = medidas[1]
	C = medidas[2]
    h = G[0]
    l = G[1]
	if C > H and B > L:
    	return False
    elif C ^ 2 > (H ^   + L ^ 2):
        return False
    else:
        return True