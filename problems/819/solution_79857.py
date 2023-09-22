def filtraMultiplos(lista, n):
	multiplos = []
	contador = 0
	while contador < len(lista):
		if lista[contador] % n == 0:
			multiplos.insert(contador, lista[contador]) #insert não dá retorno
		contador = contador + 1
	return multiplos