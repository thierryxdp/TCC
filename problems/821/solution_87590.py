def fatorial(n):
	"""Função que dada um número inteiro calcula o fatorial desse 
	numero; int->int"""
    i=1
    x=1
    while i<=n:
    	x=i*(x)
        i=i+1
    return x