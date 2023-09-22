def filtra_pares (tupla):
    t = () 
	for i in range (0,len(tupla)):
        if i//2 == 0:
            t = t + (i,)
    return t