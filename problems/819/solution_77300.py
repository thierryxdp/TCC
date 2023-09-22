def filtra_multiplos (lista, n):
	''' funcao para filtrar os multiplos de um numero n;
lista , int , float , complex -> lista '''
	lista = ''
    multiplos = lista[:]
	i = 0
	while i < len(multiplos):
		if list[multiplos]%n == 0:
			multiplos = multiplos + 1
			return multiplos