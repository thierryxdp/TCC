def primo(n):
	'''função que dado um número inteiro n positivo verifique se este
	é primo ou não; int-->bool'''
	if n==1 or n==2:
		return True
	for numero in range(2,n):
		n/numero
		if n%numero==0:
		    return False
	else:
		return True