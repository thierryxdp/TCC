def qtd_divisores(n):
	'''Funcao que conta quantos divisores o numero num,
    que e passado como entrada, tem.'''
    contador = 0
	for num in range(1, n+1):
		if n % num == 0:
			contador += 1
	return contador