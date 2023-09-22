def colchao(medidas,H,L):
	'''Função que define se o colchão passará pelas 
    portas dadas suas medidas'''
    '''list => bool'''
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