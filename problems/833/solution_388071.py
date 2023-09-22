def conta_numero(numero, matriz):
    '''
    	Funcao que dado um numero inteiro e uma matriz de inteiros
        de tamanho qualquer, conta e retorna quantas vezes aquele 
        numero aparece na matriz.
    '''
    c = 0 
    for i in matriz:
    	for j in matriz[0]:
            
        	c += 1
    return c