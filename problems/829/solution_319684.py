def soma_h(N):
    '''
    Calcula a soma do inverso de [1, N] com duas casas decimais.
    
    Entrada/Saida:
    int -> float
    '''
    H = 0
    for i in range(1, N + 1):
        H += 1/i
	return round(H, 2)