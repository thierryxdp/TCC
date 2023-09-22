def colchao(medidas, H, L):
"""define se um colchão com (medidas) passa ou não pela porta H*L
"""
if medidas[1] <= H:
	return True
if medidas[1] <= L:
	return True
if medidas[2] <= H:
	return True
if medidas[2] <= L:
	return True
else:
	return False