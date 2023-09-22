def filtraMultiplos (lista , n):
    lista2 = []
    i = 0
    for i in lista:
        if i % n ==0:
        	lista2.append(i)
    	i = i + 1
    return lista2