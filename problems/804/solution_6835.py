def filtra_pares(x):
    resultado=(,)
    
    if x[0]%2==0:
       	resultado+=tuple(x[0])
    if x[1]%2==0:
        resultado+=tuple(x[1])	
    if x[2]%2==0:
        resultado+=tuple(x[2])
    if x[3]%2==0:
        resultado+=tuple(x[3])
        
	return resultado