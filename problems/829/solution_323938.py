def soma_h(N):
    '''Função que recebe um inteiro e retorna um valor com n termos,
    onde n é inteiro e dado como entrada.
    int ->int'''
    H = 0
    for i in range(1, N+1):
        H += 1/i
	return round(H, 2)