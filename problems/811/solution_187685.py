def colchao(medidas,H,L):
    ''' recebe as medidas de um colchao e as medidas de uma porta e e verifica se o colchao consegue passar pela porta
    list,float,float -> boolean'''
    if (medidas[1] < h and medidas[2] < l) or (medidas[2]< sqrt(h**2 + l**2)):
		return True
	if (medidas[1] > h or medidas[2] > l) or (medidas[2] or sqrt(h**2 + l**2)):
		return False