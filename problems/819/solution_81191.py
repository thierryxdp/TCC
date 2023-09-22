def filtraMultiplos (lista,n): 
    lista1 = []
    i=0
    while n % lista[i] == 0 :
        lista1[i] = lista1[i] + lista[i]
        i = i+1
		return lista1