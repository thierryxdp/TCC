def filtraMultiplos (lista , n):
    lista2 = []
    i = 0
    while i in lista:
        if i % n ==0:
        	lista2 = lista2 + lista[i]
    	i = i + 1
    return lista2