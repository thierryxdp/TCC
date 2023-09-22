def filtraMultiplos (lista, n):
    multiplos = []
    contador = 0
    indice = 0
    while contador < len (lista):
        if n % lista [indice] == 0:
            multiplos = multiplos + [(indice),]
			contador = contador + 1
			indice = indice + 1
	return multiplos