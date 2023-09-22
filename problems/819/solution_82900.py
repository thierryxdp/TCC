def filtraMultiplos(lista, n):
	'''Esta função recebe uma lista e um número (n) e 
    retorna uma lista com números múmtiplos do número (n)
	list, int -> list'''
	multiplos = []
	contador = 0
	while contador < len(lista):
	if lista[contador] % n == 0:
	multiplos.insert(contador, lista[contador])
	contador = contador + 1

	return multiplos