def filtra_pares(tupla):
	t1 = list(tupla)
    
    if t1[0] % 2 != 0:
        t1.remove(t1[0])
        
   	elif t1[1] % 2 != 0:
        t1.remove(t1[1])
	elif t1[2] % 2 != 0:
    	t1.remove(t1[2])    
    elif t1[3] % 2 != 0:
        t1.remove(t1[3])
    return t1