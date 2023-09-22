def bolos(a, b, c):
	''' Dadas 'a' xícaras de farinha de trigo, 'b' ovos e 'c' colheres de sopa de leite, determina a maior quantidade
		de bolos possíveis de se fazer com os ingredientes '''
	return min(a//2, b//3, c//5)