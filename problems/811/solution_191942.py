def colchao(medidas,H,L):
    """determina se o colchao passa ou não pela porta"""
    if H>(medidas[1] or medidas[2]) and L>(medidas[1] or medidas[2]):
    	return True
    else:
        return False