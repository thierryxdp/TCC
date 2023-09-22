def comparacao(x,y,h,l):
	return x <= h and y <= l

def colchao(medidas,H,L):
	if comparacao(medidas[0], medidas[1], H,L) or comparacao(medidas[1], medidas[2], H,L) or comparacao(medidas[0], medidas[1], H,L) or comparacao(medidas[1], medidas[0], H,L) or comparacao(medidas[2], medidas[1], H,L) or comparacao(medidas[0], medidas[2], H,L):
		return True
	else:
		return False