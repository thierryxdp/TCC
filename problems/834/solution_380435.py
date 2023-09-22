def media_matriz (matriz):
    ''' dado um numero inteiro e uma matriz qualquer contendo apenas inteiros
    retorna quantas vezes o numero aparece ao longo da matriz
    int, list(list) --> int '''
    
    media = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if str(matriz) in str(matriz[i][j]):
                   media += str(matriz[i][j])
                
                
	return media