# Esta função define se colchão passa pela porta de acordo com as medidas do colchão.
# list, float, float--> bool"""
def colchao(medidas, H, L):
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