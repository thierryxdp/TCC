def colchao(lista,H,L):
	'''função que diz se um colchão passa na porta dados os parametros'''
	'''lista,int,int->bool'''
	A=lista[0]
	B=lista[1]

	if (B<=H and A<=L) or (B<=L and A<=H):
		return True 
	else:
		return False