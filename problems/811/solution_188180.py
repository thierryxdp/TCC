'''
Lista, int, int -> Boolean
'''
def colchao(medidas,H,L):
	'''
	Ao inserir uma lista com as dimensões do colchão e da porta,
	o código retorna se será possível passar o colchão pela porta.
	'''
    if H > L:
        if medidas[1] <= H:
        	return True
    	else:
        	return False
	else:
        if medidas[1] <= L:
        	return True
    	else:
        	return False