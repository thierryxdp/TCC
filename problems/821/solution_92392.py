def fatorial(numero):
	"""funcao calcula o fatorial de um numero inteiro qualquer int--> int"""
	contador = 1
	fatorial = numero
	while contador < numero:
		fatorial = fatorial * contador
		contador = contador + 1
	return fatorial