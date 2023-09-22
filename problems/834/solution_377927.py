def media_matriz(matriz):
    ''' Dado uma matriz de interios nao vazia, retorna a 
    	media de todos os numeros da matriz
        list -> float
	'''
    n_linhas = len(matriz)
    n_col = len(matriz[0])
    total_elem = n_linhas + n_col
    for i in range(n_linhas):
        for j in range(n_col):
            soma = matriz[i] + matriz[j]
    media = soma/total_elem
    return media