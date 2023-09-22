filtraMultiplos(lista, n):
    '''
    Dada uma lista e um numero n, retorna uma lista com os elementos
    que sao multiplos de n.
    '''
    i = 0
    filtrada = []
    
    while i < len(lista): 
        if lista[i] % n:
            filtrada.append(lista[i])
		i += 1
	return filtrada