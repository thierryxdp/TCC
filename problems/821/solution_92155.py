def fatorial(n):
    """função que dado um número n calcula o fatorial deste número.
    int -> int"""
	if n == 0:
		return 1
	else:
		resultado = n * fatorial(n - 1)
		return resultado