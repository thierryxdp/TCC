def colchao(medidas,H,L):
	'''Essa função define se o colchão passa pela porta de
    de acordo com as medidas do colchão
list-bool'''
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