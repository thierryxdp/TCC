def colchao(medidas,H,L):
	'''
    '''
    if medidas[0]*medidas[1]<H*L:
    	return True
    elif medidas[2]*medidas[1]<H*L:
    	return True
    elif medidas[0]*medidas[2]<H*L:
    	return True
    else:
    	return False