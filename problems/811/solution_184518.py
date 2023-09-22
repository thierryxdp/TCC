def colchao(medidas,H,L):
	G = []
    G.append(H)
    G.append(L)
    A = medidas[0]
	B = medidas[1]
	C = medidas[2]
    h = G[0]
    l = G[1]
	if l < B and h < A: 
    	return True
    else:
    	return False