def conta_numero(numero, matriz):
    '''
    	Funcao que dado um numero inteiro e uma matriz de inteiros
        de tamanho qualquer, conta e retorna quantas vezes aquele 
        numero aparece na matriz.
    '''
    i = 0
    j = 0 
    c = 0 
    for linha in matriz:
    	for coluna in matriz[i]:
            if matriz[i][j] == numero:
                c += 1
            j += 1
		i += 1    
    return c