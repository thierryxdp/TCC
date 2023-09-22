def filtraMultiplos (lista, n):
    multiplos = list()
    i = 0 
    while i<len(lista):
        if lista[i] % n == 0:
            multiplos += n
        i += 1
        
		return list.multiplos