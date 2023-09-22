def fatorial(n):
	'''Esta função calcula o fatorial de um número inteiro
	int -> int'''
    contador = 1
	fatorial = n

	while contador < n:
		fatorial = fatorial * contador
		contador = contador + 1
	return fatorial