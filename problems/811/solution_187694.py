from math import sqrt
def colchao(medidas,H,L):
    ''' recebe as medidas de um colchao e as medidas de uma porta e e verifica se o colchao consegue passar pela porta
    list,float,float -> boolean'''
    if (medidas[1] < H and medidas[2] < L) or (medidas[2]< sqrt(H**2 + L**2)):
		return True
	if (medidas[1] > H or medidas[2] > L) or (medidas[2] > sqrt(H**2 + L**2)):
		return False