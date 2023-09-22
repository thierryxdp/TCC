def filtra_pares(tp):
	'''
	Dado uma tupla de 4 numeros inteiros como entrada
	é devolvida uma tupla formada pelas entradas pares.
	tuple -> tuple
    '''
	temp = ()
	if not (tp[0] % 2):
		temp += (tp[0],)
	
	if not (tp[1] % 2):
		temp += (tp[1],)
    
	if not (tp[2] % 2):
		temp += (tp[2],)
    
	if not (tp[3] % 2):
		temp += (tp[3],)
    
	return temp