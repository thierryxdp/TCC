def filtra_pares(tupla):
	t1 = list(tupla)
    
    for num in range(0:4):
        
    if t1[0] % 2 != 0:
        t1.remove(t1[0])
    
    t2 = tuple(t1)  
	return t2