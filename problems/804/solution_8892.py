def filtra_pares (tupla):
    t = () 
	for i in range (0,len(tupla)):
        if tupla[i]%2 == 0:
            t = t + (tupla[i],)
    return t