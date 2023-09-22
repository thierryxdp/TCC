def colchao(medidas,H,L):
	'''Esta função define se um colchão de dimensões AxBxC (medidas)
	em centímetros passa por uma porta de altura (H) e largura(L) inserida
	list,int,int -> bool.'''
    dimensoes=str(medidas)
	dimensoes=str.split(dimensoes)
	B=int(str.strip(dimensoes[1],',')

	if (B<=H):
		return True
	else:
		return False