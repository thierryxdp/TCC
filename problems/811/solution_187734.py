from math import sqrt
def colchao(medidas,H,L):
	if (medidas[1] < H and medidas[2] < L): 
		return True
	if (medidas[1] > H or medidas[2] > L): 
		return False