def media_matriz(M):
    '''Função que dada uma matriz M de inteiros não vazia,
retorna a média de todos os números de M;
	list -> int'''
    m=0
    for i in range(len(M)):
        for j in range(len(M[0])):
            m=m+M[i][j]
    return round(m/2,2)