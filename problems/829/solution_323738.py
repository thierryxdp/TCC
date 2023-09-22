def soma_h(N):
	'''Esta função calcula a soma de frações com
	N termos onde cada fração tem denominador igual
	a sua posição na soma
	int -> float'''
	lista_soma = [1]
    
	for numero in range(2, N+1):
		lista_soma.append((numero)**-1)
		soma = sum(lista_soma)
	return round(soma, 2)