def conta_numero(numero, matriz)
	'''
    Essa função recebe um int numero e uma matriz e retorna quantas vezes
    numero aparece na matriz
    
    int, list -> int
    '''
    i=0
    contador=0
    while i<len(matriz)
    	j=0
        while j<len(matriz[i]):
            if matriz[i][j]==numero:
                contador+=1
        	j=j+1
        i=i+1
    return contador