def colchao(medidas,H,L):
    if H > L:
        if medidas[1] <= H:
        	return True
    	else:
        	return False
	else:
        if medidas[1] <= L:
        	return True
    	else:
        	return False