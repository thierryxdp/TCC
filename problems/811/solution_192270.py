def colchao (medidas,H,L):
    '''diz se um colchão passa pela porta, sendo H(altura porta), L(largura porta), medidas(lista com medidas do colchão)'''
    if medidas[1]< L and medidas[0]< H:
    	return True
    if medidas[0]< L and medidas[1]< H:
    	return True
    	elif medidas[0]= L and medidas[1]= H:
    	return True
    else:
    	return False