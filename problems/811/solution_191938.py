def colchao(medidas,H,L):
    """determina se o colchao passa ou não pela porta"""
    if medidas[1]<(H or L):
    	return True
    else:
        return False