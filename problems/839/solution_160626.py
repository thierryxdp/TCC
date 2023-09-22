def carros (pessoas, cap=5):
	'''calcula a quantidade de carros(com capacidade para 5 pessoas) para transportar n pessoas.
int, int->int'''
	return int(math.ceil(pessoas/cap))