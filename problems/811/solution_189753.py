def colchao(medidas,H,L):
	'''Essa função retorna com base nas medidas da porta, se o 
    colchao passa por ela
    list,float,float=>bool'''
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