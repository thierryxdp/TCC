def conta_numero(numero,matriz):
    '''
    	Funcao recebe um numero inteiro e uma
        matriz de tamanho qualquer, conta e retorna
        quantas vezes o numero dado aparece na matriz.
        int, list -> int
        
    '''
    nLin = len(matriz)
    nCol = len(matriz[0])
    repete = 0
    
    for i in range(nLin):
        for j in range(nCol):
            if matriz[i][j] == numero:
                repete += 1
    return repete