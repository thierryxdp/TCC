def fatorial(n):
	"""Função em que dado um número inteiro n retorna seu fatorial.
	int ->int."""
	i=n
	f=n
	while i!=1:
		f=f*(i-1)
		i=i-1
	return f