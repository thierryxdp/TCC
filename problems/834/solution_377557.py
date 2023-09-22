def media_matriz(m):
    ''' Função que determina a média dos elementos de uma dda matriz m
    list -> float '''
    soma = 0
    n = len(m)*len(m[0])
    for i in list(range(len(m))):
    	for j in list(range(len(m[0]))):
            soma = soma + m[i][j]
    return round(soma/n, 2)