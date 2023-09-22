def colchao(medidas,H,L):
	'''Esta função define se um colchão de dimensões AxBxC (medidas)
	em centímetros passa por uma porta de altura (H) e largura(L) inserida
	list,int,int -> bool.'''
	
   	medidas=str(medidas)
	A = int(medidas[1])
	B = int(medidas[4])
	C = int(medidas[7])

	if (L>=B and H>=C):
		return True 
	else:
		return False