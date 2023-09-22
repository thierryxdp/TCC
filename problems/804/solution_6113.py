def filtra_pares(e):
	'''Esta função recebe 4 elementos inteiros (e) e 
	retorna uma tupla contendo apenas os elementos pares da original.
	str -> tupla'''
    
	n1=int(e[0])%2
	n2=int(e[1])%2
	n3=int(e[2])%2
	n4=int(e[3])%2

 	if(n1==0 and n2==0 and n3==0):
		if(n4==0):
			return e
		else: 
			return n1+n2+n3
        
	elif(n2==0):
		if(n3==0):
			return n2+n3
		elif(n4==0):
			return n2+n4
		else:
			n2
	else: 
		return n1