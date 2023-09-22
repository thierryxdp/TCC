def colchao(medidas,H,L):
	'''
    	Dadas uma lista, com as medidas do colchao, a altura e a largura 
        da uma porta, a funcao returna True caso seja possivel que o
        colchao passe por ela. caso o contrario, a funcao retorna False.
    '''
    if (medidas[0]<=H and medidas[1]<=L) or (medidas[0]<=L and medidas[1]<=H):
    	return True
    elif (medidas[1]<=H and medidas[2]<=L) or (medidas[1]<=L and medidas[2]<=H):
    	return True
    elif (medidas[0]<=H and medidas[2]<=L) or (medidas[0]<=L and medidas[2]<=H):
    	return True
    else:
    	return False