def filtraMultiplos(lista_numeros,n):
	"""filtra os múltiplos de um número n
       int -> list"""
    lista_multiplos = []
    i = 0
    
    while i < len(lista_numeros):
    
    	if lista_numeros[i] % n == 0:
			lista_multiplos.append(lista_numeros[i])
        i += 1
	return lista_multiplos