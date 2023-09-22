def filtraMultiplos(lista,n):
    listaf = list()
    num_lista = len(lista)
    i = 0
    while(i < num_lista):
        if lista[i]%n == 0:
            listaf += (lista[i],)
		i += 1
	return listaf