#dado um inteiro retorna quantos números são divisiveis por ele
#int-->int
def qtd_divisores(n):
	x=0
	for i in range(1,n//2+1):
		if n%i==0:
			x=x+1
	if n==0:
		return 0
	else:
		return x+1