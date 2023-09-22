def filtraMultiplos(lista:list,n:int)-> bool:
    '''Filtra os múltiplos de um número n contidos na lista revebida'''
	return list(filter(lambda numeros % n == 0, lista))