def colchao(medidas,H,L):
    """determina se o colchao passa ou não pela porta"""
    if (H>(medidas[1]) and L>(medidas[2]))or (H>(medidas[2]) and L>(medidas[1])):
    	return True
    else:
        return False