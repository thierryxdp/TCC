def colchao(medidas, H , L):
    '''diz se o colchao passa pela porta ou nao''' 
	[A, B, C] = medidas
	if A and B > H and L:
        return False
	else:
        return True