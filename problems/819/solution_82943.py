def filtraMultiplos(lista, n):
	""" Esta função recebe uma lista de números e retorna seus múltiplos 
	list, int -> list """
	
	multiplos = []
	i = 0

	while contador < len(lista):
		if lista[i] % n == 0:
			multiplos.insert (i,lista[i])
		i += 1

	return multiplos