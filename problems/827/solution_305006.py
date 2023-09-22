def qtd_divisores(n):
	def divisor(x):
		return(n%x==0)
	divisores=list(filter(divisor,range(1,n+1))
	return(len(divisores))