#dado um número natural n calcula o fatorial desse número
#int-->int
def fatorial(n):
	x=1
	for f in range(1,n+1):
		x*=f
	return x