def maiores(lista,n):
	'''funcao que recebe uma lista de numeros int e um numero n int
    	e retorna outra lista com todos os numeros maiores que n de forma crescente
		int,int=>int'''
	maiores = list()
	lista.sort()
	for c in lista:
		if c >= n:
		maiores.append(c)
	return maiores