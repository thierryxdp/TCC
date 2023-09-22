def colchao(medidas,H,L):
	'''Esta função define se um colchão de dimensões AxBxC (medidas)
	em centímetros passa por uma porta de altura (H) e largura(L) inserida
	list,int,int -> bool.'''
	
   	dimensoes=str(medidas)
	A = int(dimensoes[1])
	B = int(dimensoes[4])
	C = int(dimensoes[7])

	if (L>=B and H>=C):
		return True 
	else:
		return False