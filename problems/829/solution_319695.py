def soma_h(N):
	'''Função que dado um número inteiro N calcula a soma da série harmônica e retorna
	o valor com 2 casas decimais.
	Entrada: int
	Saída: float.'''
	soma=0

	for i in range(1, N+1):
		soma+=1/i
	return round(soma, 2)