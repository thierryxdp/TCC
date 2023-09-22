def soma_h(N):
    '''Dado N como entrada, retorna a funcao de H
    com N termos'''
    i = 1
    H = 0
    for x in range(1,N):
        H = H + 1/N
	return round(H,2)