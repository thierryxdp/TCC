def soma_h(N):
	'''Recebe uma numero inteiro (N) e calcula o 
	somatorio H = 1 + 1/2 + 1/3 + 1/4 + ... + 1/N

	int -> float
	'''
	lista_soma = [1]
	for numero in range(2, N+1):
		lista_soma.append((numero)**-1)
		somatorio = sum(lista_soma)
	return round(somatorio, 2)