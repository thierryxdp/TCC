def filtra_pares(n)
	'''
    '''
    
    n1,n2,n3,n4=n
    pares=tuple()
    
    if n1 % 2 == 0:
    	pares += (n1,)
    elif n2 % 2 == 0:
    	pares += (n2,)
    elif n3 % 2 == 0:
        pares += (n3,)
    elif n4 % 2 == 0:
        pares += (n4,)
    return pares