def filtra_pares(lista):
    lista = [2]
    lista1 = filter(lambda x: x % 2 == 0,lista) 
	return list(lista1)