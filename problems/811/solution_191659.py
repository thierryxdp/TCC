def colchao(medidas, H, L): 
    """função que define se colchão passa pela porta
	de acordo com as medidas do mesmo.
    list, int, int -> bool"""

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