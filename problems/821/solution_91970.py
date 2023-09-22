#dado um número natural n calcula o fatorial desse número
#int-->int
def fatorial(n):
	x=0
	for f in range(1,n+1):
		x=x+n*f
	return x