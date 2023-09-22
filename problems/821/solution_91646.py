def fatorial(n):
	"""Retornar o fatorial de n; int=>int"""
    resultado = 1
    i = 1
	while i <= n:
        resultado*= i
        i=i+1
    return resultado