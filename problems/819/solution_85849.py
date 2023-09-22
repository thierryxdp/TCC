def filtraMultiplos(lista, n):
"""fun¸c~ao que recebe lista e retorna lista
com n´umeros m´ultiplos do n´umero n
list, int--> list"""

	multiplos = []
	contador = 0
    
		while contador < len(lista):
			if lista[contador] % n == 0:
				multiplos.insert(contador, lista[contador])
				contador = contador + 1
                
		return multiplos