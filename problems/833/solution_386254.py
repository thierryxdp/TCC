def conta_numero(numero,matriz):
    '''
    	Funcao recebe um numero inteiro e uma
        matriz de tamanho qualquer, conta e retorna
        quantas vezes o numero dado aparece na matriz.
        int, list -> int
        
    '''
	repete = 0
    
    if matriz == []:
        return repete
    else:
        for i in range(len(matriz)):
            for j in range(len(matriz[0])):
                if matriz[i][j] == numero:
                    repete += 1
        return repete