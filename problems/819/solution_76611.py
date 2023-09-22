def filtraMultiplos(lista, x) :
	multi = []
	for i in range(len(lista))-1:
		if lista[i]//x == 0 :
			multi.append(lista[i])

	return multi