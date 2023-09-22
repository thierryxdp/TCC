from math import sqrt
def colchao(medidas,H,L):
	if (medidas[1] < H and medidas[2] < L) or (medidas[2]< sqrt(H**2 + L**2)):
		return True
	if (medidas[1] > H or medidas[2] > L) or (medidas[2] > sqrt(H**2 + L**2)):
		return False