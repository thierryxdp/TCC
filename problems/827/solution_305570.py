def qtd_divisores(n):
	''' funçãoque dado um numero n retorne a quantidade de divisores e n;
	int-->int'''
	divisores=[]
	for numero in range(1,n+1):
		if n%numero==0:
			list.append(divisores,numero)
	return len(divisores)