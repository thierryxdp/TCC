def filtra_pares(x):#Start your python function here
	pares = ()
    
	if x[0]%2 == 0:
   		pares = (x[0],)
    if x[1]%2 == 0:
        pares = pares + (x[1],)
    if x[2]%2 == 0:
        pares = pares + (x[2],)
    if x[3]%2 == 0:
        pares = pares + (x[3],)
    
    return pares