def soma_h(n):
	"""funcao que calcula o valor de h para o valor n dado de entrada;int->int"""
	soma=0
	for i in range(1,n+1):
		soma=soma+(1/i)
	return round(soma,2)