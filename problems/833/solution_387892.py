def conta_numero(numero, matriz):
    ''' dado um numero inteiro e uma matriz qualquer contendo apenas inteiros
    retorna quantas vezes o numero aparece ao longo da matriz
    int, list(list) --> int '''
    
    
        
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            ocorrencias += 1
            if str(numero) in str(matriz[i][j]):
                
                
	return ocorrencias