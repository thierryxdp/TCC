def soma_h(N):
    '''Dado N como entrada, retorna a funcao de H
    com N termos'''
    H = 0
    for x in range(1,N+1):
        H = H + 1/x
	return round(H,2)