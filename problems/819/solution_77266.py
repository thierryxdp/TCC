def filtra_multiplos (x, n):
	''' funcao para filtrar os multiplos de um numero n;
lista , int , float , complex -> lista '''
	multiplos = ''
	i = 0
	while i < len(n):
		if x%n == 0:
			multiplos = multiplos + n[1]
			return multiplos