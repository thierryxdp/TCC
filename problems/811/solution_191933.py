def colchao(medidas,H,L):
    """determina se o colchao passa ou não pela porta"""
    if (medidas[0]or medidas[1]or medidas[2])>H and medidas[0]or medidas[1]or medidas[2])>L:
    	return True
    else:
        return False