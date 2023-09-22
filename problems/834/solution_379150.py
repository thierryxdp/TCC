def media_matriz(matriz):
    '''
    	Funcao recebe uma matriz de inteiros não vazia
        e retorna a media de todos os seus numeros com 
        precisao de duas casas decimais.
        list -> float
        
    '''
    
    nLin = len(matriz)
    nCol = len(matriz[0])
    soma = 0
    media = 0
    
    for i in range(nLin):
        for j in range(nCol):
            soma += matriz[i][j]
    media = media + round((soma)/(nLin*nCol),2)
    return media