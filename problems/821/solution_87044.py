def fatorial(n):
    '''Função que dado um numero retorna o fatorial de n por meio de loop
Entrada(int)
Saída(int)'''
	fat=1
	while n > 1:
		fat=fat*n
		n=n-1
	return fat