def filtraMultiplos(lista, n):
	""" Esta função recebe uma lista de números e retorna seus múltiplos 
	list, int -> list """
	
	multiplos = []
	contador  = 0

	while contador < len(lista):
		lista[contador] % == 0
		multiplos.insert (contador,lista[contador])
		contador += 1

	return multiplos